<?php
// SPDX-License-Identifier: AGPL-3.0-only
// Éclair Skills v1.2 — experimental member identity; email flows opt-in and gated.
declare(strict_types=1);
defined('ECLAIR') || exit;

require_once __DIR__ . '/lib/MemberTransport.php';
require_once __DIR__ . '/lib/MemberAccounts.php';
require_once __DIR__ . '/lib/MemberSessions.php';
require_once __DIR__ . '/lib/MemberPermissions.php';
require_once __DIR__ . '/lib/MemberPublic.php';
require_once __DIR__ . '/lib/MemberEnroll.php';

return new class {
    // Public GET/POST handlers call a dedicated, isolated member controller.
    // They require the v1.1 experimental core contract; unchanged Éclair 2.0 rejects POST.
    public function loginPage(array $ctx): array { return \EclairMemberDirectory\MemberPublic::loginPage($ctx); }
    public function login(array $ctx): array { return \EclairMemberDirectory\MemberPublic::login($ctx); }
    public function profilePage(array $ctx): array { return \EclairMemberDirectory\MemberPublic::profilePage($ctx); }
    public function logout(array $ctx): array { return \EclairMemberDirectory\MemberPublic::logout($ctx); }

    // Explicitly opt-in; POST is behind the experimental core TLS + CSRF contract.
    public function signupPage(array $ctx): array { return \EclairMemberDirectory\MemberEnroll::signupPage($ctx); }
    public function signup(array $ctx): array { return \EclairMemberDirectory\MemberEnroll::signup($ctx); }
    public function verifyPage(array $ctx): array { return \EclairMemberDirectory\MemberEnroll::verifyPage($ctx); }
    public function verify(array $ctx): array { return \EclairMemberDirectory\MemberEnroll::verify($ctx); }
    public function recoverPage(array $ctx): array { return \EclairMemberDirectory\MemberEnroll::recoverPage($ctx); }
    public function recover(array $ctx): array { return \EclairMemberDirectory\MemberEnroll::recover($ctx); }
    public function resetPage(array $ctx): array { return \EclairMemberDirectory\MemberEnroll::resetPage($ctx); }
    public function reset(array $ctx): array { return \EclairMemberDirectory\MemberEnroll::reset($ctx); }

    /** Admin GET only. Core checks users permission; no public member data is rendered. */
    public function adminPage(array $user, array $ctx): array
    {
        if (!\Eclair\Auth::can('users')) {
            throw new \DomainException('Permission denied');
        }
        $html = '<section class="card"><h2>Membres publics (prototype)</h2>'
            . '<p>Ces comptes ne peuvent pas accéder à l’administration. Inscription et récupération publiques désactivées par défaut ; les emails ne doivent être activés qu’après audit.</p>'
            . '<form method="post" action="' . e(\Eclair\Req::base() . '/'
                . \Eclair\Settings::get('admin_path', 'admin') . '/x/member-directory/create') . '">'
            . \Eclair\Security::csrfField()
            . '<label>Email du membre <input type="email" name="email" maxlength="254" required></label>'
            . '<button type="submit">Créer un compte en attente</button></form></section>';
        $members = \EclairMemberDirectory\MemberAccounts::listProfiles(30);
        $action = e(\Eclair\Req::base() . '/' . \Eclair\Settings::get('admin_path', 'admin') . '/x/member-directory/disable');
        $html .= '<section class="card"><h2>Comptes enregistrés (30 premiers)</h2><ul>';
        foreach ($members as $member) {
            $html .= '<li>' . e($member['email']) . ' — ' . e($member['state']);
            if ($member['state'] !== 'disabled') {
                $html .= ' <form method="post" action="' . $action . '">'
                    . \Eclair\Security::csrfField()
                    . '<input type="hidden" name="id" value="' . e($member['id']) . '">'
                    . '<button type="submit">Désactiver</button></form>';
            }
            $html .= '</li>';
        }
        $html .= '</ul></section>';
        return ['title' => 'Comptes membres', 'html' => $html];
    }

    /** Trusted administrator only. No password chosen by the admin; pending members cannot log in. */
    public function create(array $user, array $ctx): array
    {
        $this->requireSafeAdminPost();
        // A temporary unguessable password prevents authentication until a separate verified enrollment flow exists.
        $password = bin2hex(random_bytes(32));
        \EclairMemberDirectory\MemberAccounts::provision(\Eclair\Req::input('email'), $password);
        return ['redirect' => 'x/member-directory', 'message' => 'Compte en attente créé. Connexion non disponible.'];
    }

    /** Users permission is rechecked beyond the admin route guard; epoch revokes member sessions. */
    public function disable(array $user, array $ctx): array
    {
        $this->requireSafeAdminPost();
        \EclairMemberDirectory\MemberAccounts::disable(\Eclair\Req::input('id'));
        return ['redirect' => 'x/member-directory', 'message' => 'Compte désactivé.'];
    }

    public function migrate(string $id, array $ctx): void
    {
        if ($id === '001-directory' && \Eclair\Store::read($ctx['data'] . '/meta') === null) {
            \Eclair\Store::write($ctx['data'] . '/meta', ['schema' => 1]);
        }
    }

    private function requireSafeAdminPost(): void
    {
        if (\Eclair\Req::method() !== 'POST' || !\Eclair\Auth::can('users') || !\Eclair\Security::checkCsrf()) {
            throw new \DomainException('Admin POST security check failed');
        }
    }
};
