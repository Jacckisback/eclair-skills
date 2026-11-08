<?php
// SPDX-License-Identifier: AGPL-3.0-only
// Éclair Skills v1.0 — explicit member-only RBAC/ownership policy.
declare(strict_types=1);

namespace EclairMemberDirectory;

defined('ECLAIR') || exit;

/** No default grants. Define one capability per action/resource and require owner for "own" rules. */
final class MemberPermissions
{
    /** @var array<string,array<string,'own'|'any'>> */
    private array $rules = [];

    public function grant(string $role, string $capability, string $scope): void
    {
        if (!preg_match('/^[a-z][a-z0-9_-]{0,39}$/D', $role)
            || in_array($role, ['admin', 'editor', 'administrator', 'superuser', 'root'], true)) {
            throw new \InvalidArgumentException('Invalid member role');
        }
        if (!preg_match('/^[a-z][a-z0-9-]{0,39}:[a-z][a-z0-9._-]{0,80}$/D', $capability)) {
            throw new \InvalidArgumentException('Capability must have a module prefix: action');
        }
        if ($scope !== 'own' && $scope !== 'any') {
            throw new \InvalidArgumentException('Scope must be own or any');
        }
        if (isset($this->rules[$role][$capability])) {
            throw new \DomainException('Duplicate policy rule');
        }
        $this->rules[$role][$capability] = $scope;
    }

    /** Only an actual member SESSION token conveys authentication; never accept a caller-supplied profile or ID. */
    public function allows(string $sessionToken, string $capability, ?string $resourceOwnerId = null): bool
    {
        $resolved = MemberSessions::resolve($sessionToken);
        $member = $resolved['member'] ?? null;
        if ($member === null || ($member['state'] ?? '') !== 'active'
            || !is_string($member['id'] ?? null) || !preg_match('/^[a-f0-9]{32}$/D', $member['id'])
            || !is_array($member['roles'] ?? null)) {
            return false;
        }
        // Never trust roles/state supplied by a request. Re-read the canonical member record.
        $actual = MemberAccounts::find($member['id']);
        if ($actual === null || ($actual['state'] ?? '') !== 'active'
            || ($actual['epoch'] ?? null) !== ($member['epoch'] ?? null)) {
            return false;
        }
        foreach ($actual['roles'] as $role) {
            if (!is_string($role)) {
                continue;
            }
            $scope = $this->rules[$role][$capability] ?? null;
            if ($scope === 'any') {
                return true;
            }
            if ($scope === 'own' && $resourceOwnerId !== null
                && hash_equals($member['id'], $resourceOwnerId)) {
                return true;
            }
        }
        return false;
    }
}
