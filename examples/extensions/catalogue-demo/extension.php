<?php
// SPDX-License-Identifier: AGPL-3.0-only
declare(strict_types=1);
defined('ECLAIR') || exit;
/**
 * Démonstrateur du contrat officiel eclair-extension/1 : catalogue vitrine GET seulement.
 * Zéro prix transactionnel, commande, panier, paiement ou donnée personnelle.
 */
return new class {
    public function page(array $ctx): array
    {
        $products = [
            ['name' => 'Atelier — édition découverte', 'detail' => 'Exemple de fiche vitrine : sans vente en ligne.'],
            ['name' => 'Atelier — édition complète', 'detail' => 'Seule la présentation est illustrée dans cette démo.'],
        ];
        $html = '<h1>Catalogue de démonstration</h1><ul class="catalogue-demo">';
        foreach ($products as $product) {
            $html .= '<li><h2>' . e($product['name']) . '</h2><p>' . e($product['detail']) . '</p></li>';
        }
        $html .= '</ul><p>Aucune commande ni paiement n’est disponible ici.</p>';
        return [
            'title' => 'Catalogue de démonstration',
            'description' => 'Catalogue vitrine Éclair 2.0, sans transaction.',
            'content' => $html,
            'noindex' => true,
        ];
    }
};
