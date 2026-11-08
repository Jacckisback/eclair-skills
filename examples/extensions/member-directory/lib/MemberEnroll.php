<?php
// SPDX-License-Identifier: AGPL-3.0-only
// Éclair Skills v1.2 — experimental public signup, verification and account recovery.
declare(strict_types=1);

namespace EclairMemberDirectory;

defined('ECLAIR') || exit;

use Eclair\Mail;
use Eclair\RateLimit;
use Eclair\Req;
use Eclair\Security;
use Eclair\Settings;

/**
 * Fail-closed opt-in public enrolment. No side effects in GET handlers.
 * The transport sends links only to the email address stored on the server.
 * This is a file-backed prototype: not ready for real customers until full HTTP/SMTP audit.
 */
final class MemberEnroll
{
    private const REGISTER = '/membres/inscription';
    private const VERIFY = '/membres/verification';
    private const RECOVER = '/membres/recuperation';
    private const RESET = '/membres/reinitialisation';
    private const LOGIN = '/membres/connexion';

    public static function signupPage(array $ctx): array
    {
        self::requireSecureGet();
        self::enabled($ctx, 'registration_enabled');
        $content = '<h1>Créer un compte</h1><form method="post" action="' . e(self::local(self::REGISTER)) . '">'
            . Security::formField()
            . '<label>Email<input name="email" type="email" autocomplete="email" maxlength="254" required></label>'
            . '<button type="submit">Recevoir le lien de vérification</button></form>';
        return self::page('Inscription', $content);
    }

    public static function signup(array $ctx): array
    {
        self::requireSecurePost();
        self::enabled($ctx, 'registration_enabled');
        self::mailReady();
        $email = Req::input('email');
        if (strlen($email) > 254) {
            return self::generic();
        }
        try { $email = MemberAccounts::normalizeEmail($email); }
        catch (\InvalidArgumentException) { return self::generic(); }
        $key = 'member-signup-email:' . hash('sha256', $email);
        if (!RateLimit::attempt('member-signup-ip:' . Req::ipPrefix(), 8, 3600, 3600)
            || !RateLimit::attempt($key, 2, 86400, 86400)) {
            return self::generic();
        }
        // No account existence disclosure. Never email existing accounts as part of signup.
        if (MemberAccounts::findByEmail($email) !== null) {
            return self::generic();
        }
        try {
            $member = MemberAccounts::provision($email, bin2hex(random_bytes(32)));
            $proof = MemberAccounts::issueVerification($member['id']);
            $link = self::absolute(self::VERIFY, $member['id'], $proof);
            // Fail closed for non-delivery; account remains pending for administrator recovery.
            $sent = Mail::send($email, 'Vérification de votre inscription',
                "Pour confirmer votre email et choisir un mot de passe, ouvrez ce lien (30 minutes) :\n" . $link .
                "\n\nSi vous n'avez rien demandé, ignorez ce message.");
            if (!$sent) {
                MemberAccounts::discardUndelivered($member['id']);
            }
        } catch (\DomainException) {
            // Concurrent duplicate registration: indistinguishable from an existing account.
        }
        return self::generic();
    }

    public static function verifyPage(array $ctx): array
    {
        self::requireSecureGet();
        self::enabled($ctx, 'registration_enabled');
        [$id, $token] = self::proofFromQuery();
        $html = '<h1>Vérifier mon adresse</h1><form method="post" action="' . e(self::local(self::VERIFY)) . '">'
            . Security::formField() . self::hiddenProof($id, $token)
            . '<label>Choisir un mot de passe (12 caractères minimum)<input type="password" name="password" minlength="12" maxlength="1024" autocomplete="new-password" required></label>'
            . '<button type="submit">Activer mon compte</button></form>';
        return self::page('Vérification de compte', $html);
    }

    public static function verify(array $ctx): array
    {
        self::requireSecurePost();
        self::enabled($ctx, 'registration_enabled');
        if (!RateLimit::attempt('member-verify-ip:' . Req::ipPrefix(), 12, 3600, 3600)) {
            return self::failProof();
        }
        $id = Req::input('id'); $token = Req::input('token'); $password = Req::input('password');
        if (!self::validProof($id, $token) || strlen($password) > 1024) {
            return self::failProof();
        }
        try {
            MemberAccounts::confirmVerification($id, $token, $password);
        } catch (\DomainException|\InvalidArgumentException) {
            return self::failProof();
        }
        return ['redirect' => self::LOGIN];
    }

    public static function recoverPage(array $ctx): array
    {
        self::requireSecureGet();
        self::enabled($ctx, 'recovery_enabled');
        return self::page('Mot de passe oublié',
            '<h1>Mot de passe oublié</h1><form method="post" action="' . e(self::local(self::RECOVER)) . '">'
            . Security::formField()
            . '<label>Email<input type="email" name="email" maxlength="254" autocomplete="email" required></label>'
            . '<button type="submit">Recevoir un lien</button></form>');
    }

    public static function recover(array $ctx): array
    {
        self::requireSecurePost();
        self::enabled($ctx, 'recovery_enabled');
        self::mailReady();
        $email = Req::input('email');
        if (strlen($email) > 254) { return self::generic(); }
        try { $email = MemberAccounts::normalizeEmail($email); }
        catch (\InvalidArgumentException) { return self::generic(); }
        if (!RateLimit::attempt('member-recover-ip:' . Req::ipPrefix(), 8, 3600, 3600)
            || !RateLimit::attempt('member-recover-email:' . hash('sha256', $email), 2, 86400, 86400)) {
            return self::generic();
        }
        $member = MemberAccounts::findByEmail($email);
        if ($member !== null && ($member['state'] ?? '') === 'active') {
            $proof = MemberAccounts::issueReset($member['id']);
            // Never use a request Host header to construct recovery URLs.
            Mail::send($member['email'], 'Réinitialisation de mot de passe',
                "Pour choisir un nouveau mot de passe, ouvrez ce lien (15 minutes) :\n"
                . self::absolute(self::RESET, $member['id'], $proof)
                . "\n\nSi vous n'avez rien demandé, ignorez ce message.");
        }
        return self::generic();
    }

    public static function resetPage(array $ctx): array
    {
        self::requireSecureGet();
        self::enabled($ctx, 'recovery_enabled');
        [$id, $token] = self::proofFromQuery();
        return self::page('Nouveau mot de passe',
            '<h1>Choisir un nouveau mot de passe</h1><form method="post" action="' . e(self::local(self::RESET)) . '">'
            . Security::formField() . self::hiddenProof($id, $token)
            . '<label>Mot de passe (12 caractères minimum)<input type="password" name="password" minlength="12" maxlength="1024" autocomplete="new-password" required></label>'
            . '<button type="submit">Réinitialiser</button></form>');
    }

    public static function reset(array $ctx): array
    {
        self::requireSecurePost();
        self::enabled($ctx, 'recovery_enabled');
        if (!RateLimit::attempt('member-reset-ip:' . Req::ipPrefix(), 12, 3600, 3600)) {
            return self::failProof();
        }
        $id = Req::input('id'); $token = Req::input('token'); $password = Req::input('password');
        if (!self::validProof($id, $token) || strlen($password) > 1024) {
            return self::failProof();
        }
        try {
            MemberAccounts::confirmReset($id, $token, $password);
        } catch (\DomainException|\InvalidArgumentException) {
            return self::failProof();
        }
        return ['redirect' => self::LOGIN];
    }

    private static function mailReady(): void
    {
        // A verified canonical HTTPS URL is required; never build token URLs from Host headers.
        $url = (string) Settings::get('url');
        if (!str_starts_with($url, 'https://') || !Settings::verified()
            || !filter_var($url, FILTER_VALIDATE_URL)
            || parse_url($url, PHP_URL_USER) !== null || parse_url($url, PHP_URL_PASS) !== null
            || parse_url($url, PHP_URL_QUERY) !== null || parse_url($url, PHP_URL_FRAGMENT) !== null) {
            throw new \DomainException('Verified HTTPS canonical URL required for email links');
        }
    }

    private static function absolute(string $route, string $memberId, string $token): string
    {
        return rtrim((string) Settings::get('url'), '/') . $route . '?id=' . rawurlencode($memberId) . '&token=' . rawurlencode($token);
    }

    private static function enabled(array $ctx, string $feature): void
    {
        if (($ctx['settings'][$feature] ?? false) !== true) {
            throw new \DomainException('Member email flow not enabled');
        }
    }

    private static function requireSecureGet(): void
    {
        if (!MemberTransport::isSecure() || !in_array(Req::method(), ['GET','HEAD'], true)) {
            throw new \DomainException('HTTPS GET required');
        }
    }

    private static function requireSecurePost(): void
    {
        if (!MemberTransport::isSecure() || Req::method() !== 'POST' || !Security::checkFormToken()) {
            throw new \DomainException('HTTPS POST with CSRF required');
        }
    }

    private static function proofFromQuery(): array
    {
        $id = Req::query('id'); $token = Req::query('token');
        return self::validProof($id, $token) ? [$id, $token] : ['', ''];
    }

    private static function validProof(string $id, string $token): bool
    {
        return preg_match('/^[a-f0-9]{32}$/D', $id) === 1 && preg_match('/^[a-f0-9]{64}$/D', $token) === 1;
    }

    private static function hiddenProof(string $id, string $token): string
    {
        return '<input type="hidden" name="id" value="' . e($id) . '">'
            . '<input type="hidden" name="token" value="' . e($token) . '">';
    }

    private static function page(string $title, string $html): array
    {
        return ['title' => $title, 'description' => '', 'content' => $html, 'noindex' => true];
    }

    private static function generic(): array
    {
        return ['status' => 200, 'body' => 'Si votre adresse est éligible, un email vous sera envoyé.'];
    }

    private static function failProof(): array
    {
        return ['status' => 400, 'body' => 'Lien expiré ou invalide. Demandez un nouveau lien.'];
    }

    private static function local(string $route): string
    {
        return rtrim(Req::base(), '/') . $route;
    }
}
