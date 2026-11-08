<?php
// SPDX-License-Identifier: AGPL-3.0-only
declare(strict_types=1);
defined('ECLAIR') || exit;

return new class {
    public function page(array $ctx): array
    {
        $name = (string) ($ctx['settings']['title'] ?? 'Éclair Skills');
        return [
            'title' => $name,
            'description' => 'Démonstration d’une fonction Éclair 2.0.',
            'content' => '<h1>' . e($name) . '</h1><p>Fonction facultative validée par le noyau.</p>',
        ];
    }

    public function adminPage(array $user, array $ctx): array
    {
        return [
            'title' => 'Skill Sample',
            'html' => '<section class="card"><p>' . e((string) ($ctx['settings']['title'] ?? 'Éclair Skills')) . '</p></section>',
        ];
    }

    public function migrate(string $id, array $ctx): void
    {
        if ($id !== '001-init') {
            return;
        }
        $key = (string) $ctx['data'] . '/demo';
        if (\Eclair\Store::read($key) === null) {
            \Eclair\Store::write($key, ['created' => time()]);
        }
    }
};
