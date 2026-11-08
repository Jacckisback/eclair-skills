<?php
// SPDX-License-Identifier: AGPL-3.0-only
// Éclair Skills v1.2 experimental member identity; public email flows require opt-in and audit.
declare(strict_types=1);

namespace EclairMemberDirectory;

defined('ECLAIR') || exit;

use Eclair\Store;

/** Separate, explicitly opted-in MEMBER identity domain; never grants Eclair admin/editor access. */
final class MemberAccounts
{
    private const INDEX = 'ext/member-directory/email_index';
    private const MIN_PASSWORD_BYTES = 12;
    private const MAX_PASSWORD_BYTES = 1024;
    private const MAX_MEMBERS = 1000; // File-backed prototype only; migrate at scale.

    public static function normalizeEmail(string $email): string
    {
        $email = strtolower(trim($email));
        if (strlen($email) > 254 || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new \InvalidArgumentException('Invalid member email');
        }
        return $email;
    }

    /** Provision only from an explicitly authenticated, rate-limited, trusted service; returns public profile. */
    public static function provision(string $email, string $password): array
    {
        $email = self::normalizeEmail($email);
        self::checkPassword($password);
        // Hash outside the exclusive store lock: expensive operations must not block other writers.
        $hash = password_hash($password, self::algorithm());
        return Store::locked(static function () use ($email, $hash): array {
            $index = Store::read(self::INDEX, []);
            if (!is_array($index)) {
                throw new \RuntimeException('Member index invalid');
            }
            if (count($index) >= self::MAX_MEMBERS) {
                throw new \RuntimeException('Prototype member capacity reached: use transactional storage');
            }
            $key = hash('sha256', $email);
            if (isset($index[$key])) {
                throw new \DomainException('Member already exists');
            }
            $id = bin2hex(random_bytes(16));
            $m = ['id' => $id, 'email' => $email, 'password_hash' => $hash, 'state' => 'pending',
                'roles' => ['member'], 'epoch' => 1, 'created_at' => time(), 'updated_at' => time()];
            // Commit under one lock. Best-effort cleanup if index persistence fails;
            // the full multi-file atomicity contract remains a future SQL/storage milestone.
            Store::write('ext/member-directory/member_' . $id, $m);
            $index[$key] = $id;
            try {
                Store::write(self::INDEX, $index);
            } catch (\Throwable $e) {
                Store::delete('ext/member-directory/member_' . $id);
                throw $e;
            }
            return self::profile($m);
        });
    }

    /** Issue a short-lived email proof. The caller MUST deliver this token to the account's mailbox. */
    public static function issueVerification(string $memberId): string
    {
        return Store::locked(static function () use ($memberId): string {
            $m = self::find($memberId);
            if ($m === null || $m['state'] !== 'pending') {
                throw new \DomainException('Member is not pending');
            }
            $token = bin2hex(random_bytes(32));
            $m['verification'] = ['hash' => hash('sha256', $token), 'expires' => time() + 1800];
            Store::write('ext/member-directory/member_' . $memberId, $m);
            // NEVER show this in an admin HTML page or log it. External trusted email delivery is not included.
            return $token;
        });
    }

    /** Confirm proof delivered out-of-band and set the member's OWN password; consume proof exactly once. */
    public static function confirmVerification(string $memberId, string $token, string $password): array
    {
        self::checkPassword($password);
        if (!preg_match('/^[a-f0-9]{64}$/D', $token)) {
            throw new \DomainException('Invalid verification proof');
        }
        // Preflight the opaque proof before invoking an expensive Argon2/bcrypt hash.
        // This is NOT authorization: the check is repeated under the exclusive lock below.
        $check = self::find($memberId);
        if (($check['state'] ?? '') !== 'pending' || !self::proofValid($check['verification'] ?? null, $token)) {
            throw new \DomainException('Invalid or expired verification proof');
        }
        $hash = password_hash($password, self::algorithm());
        return Store::locked(static function () use ($memberId, $token, $hash): array {
            $m = self::find($memberId);
            $proof = $m['verification'] ?? null;
            if ($m === null || $m['state'] !== 'pending' || !is_array($proof)
                || !is_string($proof['hash'] ?? null)
                || !is_int($proof['expires'] ?? null) || $proof['expires'] < time()
                || !hash_equals($proof['hash'], hash('sha256', $token))) {
                throw new \DomainException('Invalid or expired verification proof');
            }
            $m['password_hash'] = $hash;
            $m['state'] = 'active';
            unset($m['verification']);
            $m['epoch']++;
            $m['updated_at'] = time();
            Store::write('ext/member-directory/member_' . $memberId, $m);
            return self::profile($m);
        });
    }

    /** Roll back a new, still-pending signup if the server failed to hand its email to the transport.
     * Never callable from public request parameters. Delete the index first, leaving at worst an unreferenced file.
     */
    public static function discardUndelivered(string $memberId): void
    {
        Store::locked(static function () use ($memberId): void {
            $m = self::find($memberId);
            if ($m === null || $m['state'] !== 'pending') {
                return;
            }
            $index = Store::read(self::INDEX, []);
            $key = hash('sha256', $m['email']);
            if (!is_array($index) || ($index[$key] ?? '') !== $memberId) {
                return;
            }
            unset($index[$key]);
            Store::write(self::INDEX, $index);
            Store::delete('ext/member-directory/member_' . $memberId);
        });
    }

    /** Only a trusted mail-flow may issue a recovery proof; no proof is ever logged or returned to a browser. */
    public static function issueReset(string $memberId): string
    {
        return Store::locked(static function () use ($memberId): string {
            $m = self::find($memberId);
            if ($m === null || ($m['state'] ?? '') !== 'active') {
                throw new \DomainException('Active member required');
            }
            $token = bin2hex(random_bytes(32));
            $m['reset'] = ['hash' => hash('sha256', $token), 'expires' => time() + 900];
            Store::write('ext/member-directory/member_' . $memberId, $m);
            return $token;
        });
    }

    /** Consumes reset proof atomically, rotates password and revokes all previous sessions via epoch. */
    public static function confirmReset(string $memberId, string $token, string $newPassword): array
    {
        self::checkPassword($newPassword);
        if (!preg_match('/^[a-f0-9]{64}$/D', $token)) {
            throw new \DomainException('Invalid reset proof');
        }
        // Reject bad/expired proofs before costly password hashing; recheck under lock.
        $check = self::find($memberId);
        if (($check['state'] ?? '') !== 'active' || !self::proofValid($check['reset'] ?? null, $token)) {
            throw new \DomainException('Invalid or expired reset proof');
        }
        $hash = password_hash($newPassword, self::algorithm());
        return Store::locked(static function () use ($memberId, $token, $hash): array {
            $m = self::find($memberId);
            $proof = $m['reset'] ?? null;
            if ($m === null || ($m['state'] ?? '') !== 'active' || !is_array($proof)
                || !is_string($proof['hash'] ?? null) || !is_int($proof['expires'] ?? null)
                || $proof['expires'] < time()
                || !hash_equals($proof['hash'], hash('sha256', $token))) {
                throw new \DomainException('Invalid or expired reset proof');
            }
            $m['password_hash'] = $hash;
            unset($m['reset']);
            $m['epoch']++;
            $m['updated_at'] = time();
            Store::write('ext/member-directory/member_' . $memberId, $m);
            return self::profile($m);
        });
    }

    public static function disable(string $memberId): array
    {
        return self::mutate($memberId, static function (array $m): array {
            $m['state'] = 'disabled';
            return $m;
        });
    }

    /** Role assignments must come from trusted business logic, never from request bodies. */
    public static function setRoles(string $memberId, array $roles): array
    {
        $roles = self::validateRoles($roles);
        return self::mutate($memberId, static function (array $m) use ($roles): array {
            $m['roles'] = $roles;
            return $m;
        });
    }

    public static function changePassword(string $memberId, string $password): array
    {
        self::checkPassword($password);
        $hash = password_hash($password, self::algorithm());
        return self::mutate($memberId, static function (array $m) use ($hash): array {
            $m['password_hash'] = $hash;
            return $m;
        });
    }

    /** No unauthenticated login route is exposed; caller MUST enforce throttling and HTTPS. */
    public static function authenticate(string $email, string $password): ?array
    {
        // Uniform error for unknown, pending, disabled or incorrect-password accounts.
        try {
            $m = self::findByEmail(self::normalizeEmail($email));
        } catch (\InvalidArgumentException $e) {
            return null;
        }
        if ($m === null || ($m['state'] ?? '') !== 'active') {
            // Run a dummy verify to reduce trivial account enumeration timing.
            password_verify($password, self::dummyHash());
            return null;
        }
        return password_verify($password, $m['password_hash']) ? self::profile($m) : null;
    }

    public static function find(string $id): ?array
    {
        if (!preg_match('/^[a-f0-9]{32}$/D', $id)) {
            return null;
        }
        $m = Store::read('ext/member-directory/member_' . $id, null);
        return is_array($m) && ($m['id'] ?? null) === $id ? $m : null;
    }

    public static function findByEmail(string $email): ?array
    {
        $index = Store::read(self::INDEX, []);
        if (!is_array($index)) {
            throw new \RuntimeException('Member index invalid');
        }
        $id = $index[hash('sha256', $email)] ?? null;
        return is_string($id) ? self::find($id) : null;
    }

    /** Admin-only service caller MUST authorize users right before presenting any email address. */
    public static function listProfiles(int $limit = 30): array
    {
        $limit = max(1, min(100, $limit));
        $index = Store::read(self::INDEX, []);
        if (!is_array($index)) {
            throw new \RuntimeException('Member index invalid');
        }
        $out = [];
        foreach ($index as $id) {
            if (!is_string($id) || ($m = self::find($id)) === null) {
                continue;
            }
            $out[] = self::profile($m);
            if (count($out) >= $limit) {
                break;
            }
        }
        return $out;
    }

    public static function profile(array $m): array
    {
        return ['id' => (string) $m['id'], 'email' => (string) $m['email'],
            'state' => (string) $m['state'], 'roles' => $m['roles'], 'epoch' => (int) $m['epoch']];
    }

    private static function mutate(string $memberId, callable $fn): array
    {
        return Store::locked(static function () use ($memberId, $fn): array {
            $m = self::find($memberId);
            if ($m === null) {
                throw new \DomainException('Unknown member');
            }
            $m = $fn($m);
            // All account changes revoke existing sessions, including membership/roles changes.
            $m['epoch']++;
            $m['updated_at'] = time();
            Store::write('ext/member-directory/member_' . $memberId, $m);
            return self::profile($m);
        });
    }

    private static function validateRoles(array $roles): array
    {
        if (!array_is_list($roles) || count($roles) > 12 || !$roles) {
            throw new \InvalidArgumentException('Invalid roles list');
        }
        foreach ($roles as $role) {
            if (!is_string($role) || !preg_match('/^[a-z][a-z0-9_-]{0,39}$/D', $role)
                || in_array($role, ['admin', 'editor', 'administrator', 'superuser', 'root'], true)) {
                throw new \InvalidArgumentException('Forbidden member role');
            }
        }
        if (count(array_unique($roles)) !== count($roles)) {
            throw new \InvalidArgumentException('Duplicate member roles');
        }
        return $roles;
    }

    /** Validates only server-side proof metadata; caller still rechecks within Store::locked(). */
    private static function proofValid(mixed $proof, string $token): bool
    {
        return is_array($proof) && is_string($proof['hash'] ?? null)
            && is_int($proof['expires'] ?? null) && $proof['expires'] >= time()
            && hash_equals($proof['hash'], hash('sha256', $token));
    }

    private static function checkPassword(string $password): void
    {
        $bytes = strlen($password);
        if ($bytes < self::MIN_PASSWORD_BYTES || $bytes > self::MAX_PASSWORD_BYTES || str_contains($password, "\0")) {
            throw new \InvalidArgumentException('Password length/format not accepted');
        }
        if (self::algorithm() === PASSWORD_BCRYPT && $bytes > 72) {
            throw new \InvalidArgumentException('Password too long for bcrypt');
        }
    }

    private static function algorithm(): string|int
    {
        return defined('PASSWORD_ARGON2ID') ? PASSWORD_ARGON2ID : PASSWORD_BCRYPT;
    }

    private static function dummyHash(): string
    {
        return '$2y$10$uZ5udnZzoBO3UlYHQ4Uq5u8mWqsDPwKSf6Jbu/mEBOt.HWxqRRdDm';
    }
}
