<?php
// SPDX-License-Identifier: AGPL-3.0-only
// Éclair Skills v1.0 — separate member sessions, not Eclair admin sessions.
declare(strict_types=1);

namespace EclairMemberDirectory;

defined('ECLAIR') || exit;

use Eclair\Store;
use Eclair\Req;

final class MemberSessions
{
    public const COOKIE = '__Host-eclair_member';
    public const IDLE_SECONDS = 1800;
    public const ABSOLUTE_SECONDS = 43200;

    /** Token must only be returned to TLS cookie code, never exposed in HTML/logs/URLs. */
    public static function create(array $member): string
    {
        if (($member['state'] ?? null) !== 'active' || !is_string($member['id'] ?? null)
            || !preg_match('/^[a-f0-9]{32}$/D', $member['id'])) {
            throw new \DomainException('Only active members can have a session');
        }
        // Do not trust a stale profile (e.g. disabled immediately after login).
        return Store::locked(static function () use ($member): string {
            $current = MemberAccounts::find($member['id']);
            if ($current === null || ($current['state'] ?? '') !== 'active'
                || ($current['epoch'] ?? null) !== ($member['epoch'] ?? null)) {
                throw new \DomainException('Member changed: refuse session');
            }
            $token = bin2hex(random_bytes(32));
            $now = time();
            Store::write(self::key($token), ['member_id' => $member['id'], 'epoch' => $member['epoch'],
                'csrf' => bin2hex(random_bytes(32)), 'issued' => $now, 'seen' => $now]);
            return $token;
        });
    }

    /** Returns public member + CSRF token internally; callers must not serialize CSRF to public APIs. */
    public static function resolve(string $token): ?array
    {
        if (!self::validToken($token)) {
            return null;
        }
        $key = self::key($token);
        $session = Store::read($key, null);
        if (!is_array($session)) {
            return null;
        }
        $now = time();
        if (!self::live($session, $now)) {
            Store::delete($key);
            return null;
        }
        $m = MemberAccounts::find((string) ($session['member_id'] ?? ''));
        if ($m === null || ($m['state'] ?? '') !== 'active'
            || ($m['epoch'] ?? null) !== ($session['epoch'] ?? null)) {
            Store::delete($key);
            return null;
        }
        if ($now - (int) $session['seen'] >= 300) {
            // Never recreate a session that was revoked concurrently.
            $valid = Store::locked(static function () use ($key, $now): bool {
                $fresh = Store::read($key, null);
                if (!is_array($fresh) || !self::live($fresh, $now)) {
                    return false;
                }
                $fresh['seen'] = $now;
                Store::write($key, $fresh);
                return true;
            });
            if (!$valid) {
                return null;
            }
        }
        return ['member' => MemberAccounts::profile($m), 'csrf' => $session['csrf']];
    }

    /** Verify CSRF only after authenticating the actual member token. Never accept caller-forged session arrays. */
    public static function verifyCsrf(string $sessionToken, string $csrfToken): bool
    {
        $resolved = self::resolve($sessionToken);
        return $resolved !== null && is_string($resolved['csrf'] ?? null)
            && strlen($csrfToken) === 64 && hash_equals($resolved['csrf'], $csrfToken);
    }

    public static function revoke(string $token): void
    {
        if (self::validToken($token)) {
            Store::locked(static fn() => Store::delete(self::key($token)));
        }
    }

    /** On role/password/state changes, MemberAccounts increments epoch, invalidating ALL prior sessions. */
    public static function setCookie(string $token): void
    {
        if (!self::validToken($token) || !MemberTransport::isSecure() || headers_sent()) {
            throw new \RuntimeException('Member session cookies require TLS, valid token and unsent headers');
        }
        setcookie(self::COOKIE, $token, ['expires' => 0, 'path' => '/', 'secure' => true,
            'httponly' => true, 'samesite' => 'Lax']);
        header('Cache-Control: private, no-store');
    }

    public static function clearCookie(): void
    {
        if (!MemberTransport::isSecure() || headers_sent()) {
            throw new \RuntimeException('Member logout cookies require TLS and unsent headers');
        }
        setcookie(self::COOKIE, '', ['expires' => time() - 3600, 'path' => '/', 'secure' => true,
            'httponly' => true, 'samesite' => 'Lax']);
        header('Cache-Control: private, no-store');
    }

    private static function live(array $s, int $now): bool
    {
        return is_int($s['issued'] ?? null) && is_int($s['seen'] ?? null)
            && $s['issued'] <= $now && $s['seen'] <= $now
            && $now - $s['issued'] < self::ABSOLUTE_SECONDS
            && $now - $s['seen'] < self::IDLE_SECONDS
            && is_string($s['csrf'] ?? null) && preg_match('/^[a-f0-9]{64}$/D', $s['csrf']) === 1;
    }

    private static function validToken(string $token): bool
    {
        return preg_match('/^[a-f0-9]{64}$/D', $token) === 1;
    }

    private static function key(string $token): string
    {
        return 'ext/member-directory/session_' . hash('sha256', $token);
    }
}
