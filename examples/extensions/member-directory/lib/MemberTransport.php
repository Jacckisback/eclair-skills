<?php
// SPDX-License-Identifier: AGPL-3.0-only
// Experimental member-auth transport safety: do not trust client-supplied proxy headers.
declare(strict_types=1);

namespace EclairMemberDirectory;

defined('ECLAIR') || exit;

final class MemberTransport
{
    public static function isSecure(): bool
    {
        // Prefer the actual server-side TLS indication, never a user-controlled Forwarded header.
        $https = strtolower((string) ($_SERVER['HTTPS'] ?? ''));
        if (in_array($https, ['on', '1', 'true'], true)
            || (string) ($_SERVER['SERVER_PORT'] ?? '') === '443') {
            return true;
        }
        // Behind a TLS-terminating reverse proxy, allow ONLY its explicitly configured IP.
        // It must overwrite X-Forwarded-Proto from clients. Never infer trust from Host.
        $trusted = defined('ECLAIR_MEMBER_TRUSTED_PROXY_IP') ? ECLAIR_MEMBER_TRUSTED_PROXY_IP : '';
        $remote = (string) ($_SERVER['REMOTE_ADDR'] ?? '');
        return is_string($trusted) && filter_var($trusted, FILTER_VALIDATE_IP) !== false
            && filter_var($remote, FILTER_VALIDATE_IP) !== false
            && inet_pton($trusted) === inet_pton($remote)
            && strtolower((string) ($_SERVER['HTTP_X_FORWARDED_PROTO'] ?? '')) === 'https';
    }
}
