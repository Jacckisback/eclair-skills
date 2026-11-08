<?php
// SPDX-License-Identifier: AGPL-3.0-only
// Experimental member HTTP controller for Éclair CMS 2.0 + proposed public POST contract.
declare(strict_types=1);
namespace EclairMemberDirectory;
defined('ECLAIR') || exit;

use Eclair\Req;
use Eclair\Security;
use Eclair\Http;
use Eclair\RateLimit;

/** Only activated, email-verified members can log in. Never confuses members with CMS administrators. */
final class MemberPublic
{
    private const SIGNIN = '/membres/connexion';
    private const SPACE = '/membres/espace';
    private const SIGNOUT = '/membres/deconnexion';

    /** Non-cacheable public form; core's Security::formField writes a stateless CSRF cookie. */
    public static function loginPage(array $ctx): array
    {
        self::requireHttpsGet();
        $html = '<h1>Connexion membre</h1><form method="post" action="' . e(self::url(self::SIGNIN)) . '">'
            . Security::formField()
            . '<label>Adresse email<input type="email" name="email" maxlength="254" autocomplete="username" required></label>'
            . '<label>Mot de passe<input type="password" name="password" maxlength="1024" autocomplete="current-password" required></label>'
            . '<button type="submit">Se connecter</button></form>';
        if (($ctx['settings']['registration_enabled'] ?? false) === true) {
            $html .= '<p><a href="' . e(self::url('/membres/inscription')) . '">Créer un compte</a></p>';
        }
        if (($ctx['settings']['recovery_enabled'] ?? false) === true) {
            $html .= '<p><a href="' . e(self::url('/membres/recuperation')) . '">Mot de passe oublié ?</a></p>';
        }
        return self::page('Connexion membre', $html);
    }

    /** Called only by an explicitly declared, uncached POST route, never from GET. */
    public static function login(array $ctx): array
    {
        self::requirePost();
        $email = Req::input('email');
        $password = Req::input('password');
        // Reject oversized inputs before deriving account keys or running an expensive password hash.
        if (strlen($email) > 254 || strlen($password) > 1024 || $password === '') {
            return self::error('Identifiants incorrects ou compte indisponible.');
        }
        $network = 'member-login-ip:' . Req::ipPrefix();
        $account = 'member-login-account:' . hash('sha256', strtolower(trim($email)));
        // Reserve attempts before expensive password hashing. Do not leak account existence.
        if (!RateLimit::attempt($network, 30, 900, 900) || !RateLimit::attempt($account, 6, 900, 900)) {
            return self::error('Connexion impossible. Réessaie plus tard.');
        }
        $member = MemberAccounts::authenticate($email, $password);
        if ($member === null) {
            return self::error('Identifiants incorrects ou compte indisponible.');
        }
        $token = MemberSessions::create($member);
        MemberSessions::setCookie($token);
        RateLimit::release($network);
        RateLimit::release($account);
        return ['redirect' => self::SPACE];
    }

    /** Private page; an anonymous visitor is redirected to the login form. */
    public static function profilePage(array $ctx): array
    {
        self::requireHttpsGet();
        $token = self::cookie();
        $s = MemberSessions::resolve($token);
        if ($s === null) {
            Http::redirect(self::url(self::SIGNIN), 303);
        }
        $name = e((string) $s['member']['email']);
        $html = '<h1>Mon espace</h1><p>Connecté : ' . $name . '</p>'
            . '<form method="post" action="' . e(self::url(self::SIGNOUT)) . '">'
            . Security::formField()
            . '<input type="hidden" name="_member_csrf" value="' . e((string) $s['csrf']) . '">'
            . '<button type="submit">Se déconnecter</button></form>';
        return self::page('Mon espace membre', $html);
    }

    /** Requires BOTH the core double-submit form proof and authenticated member-specific proof. */
    public static function logout(array $ctx): array
    {
        self::requirePost();
        $token = self::cookie();
        if (!MemberSessions::verifyCsrf($token, Req::input('_member_csrf'))) {
            return ['status' => 403, 'body' => 'Action refused'];
        }
        MemberSessions::revoke($token);
        MemberSessions::clearCookie();
        return ['redirect' => self::SIGNIN];
    }

    private static function page(string $title, string $html): array
    {
        return ['title' => $title, 'description' => '', 'content' => $html, 'noindex' => true];
    }

    private static function error(string $reason): array
    {
        // Return an error response with a safe, generic body. The core POST dispatcher sets no-store.
        return ['status' => 401, 'body' => $reason];
    }

    private static function requireHttpsGet(): void
    {
        if (!MemberTransport::isSecure() || !in_array(Req::method(), ['GET','HEAD'], true)) {
            throw new \DomainException('Member pages require HTTPS GET');
        }
    }

    private static function requirePost(): void
    {
        if (!MemberTransport::isSecure() || Req::method() !== 'POST' || !Security::checkFormToken()) {
            throw new \DomainException('Public POST: HTTPS/CSRF required');
        }
    }

    private static function cookie(): string
    {
        $value = $_COOKIE[MemberSessions::COOKIE] ?? '';
        return is_string($value) ? $value : '';
    }

    private static function url(string $path): string
    {
        return rtrim(Req::base(), '/') . $path;
    }
}
