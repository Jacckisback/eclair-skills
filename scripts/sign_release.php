<?php
declare(strict_types=1);
/**
 * Signs the Éclair Skills release with the maintainer's Ed25519 key (libsodium).
 *
 *   python3 scripts/check_release.py --write      # 1. refresh SHA256SUMS.json
 *   ECLAIR_SIGNING_KEY=… php scripts/sign_release.php   # 2. sign → SIGNATURE.json
 *   php scripts/verify_signature.php              # 3. verify
 *
 * What is signed: a small JSON payload containing the SHA-256 of SHA256SUMS.json,
 * which itself lists the SHA-256 of every file of the repository. One signature
 * therefore covers every skill, script, example and document.
 *
 * Domain separation: the signed message is CONTEXT . payload. The Éclair CMS updater
 * only accepts messages prefixed with "eclair-cms/annonce/2:" (or a raw JSON
 * announcement for very old sites), so a skills signature can never be replayed as a
 * CMS update announcement, and vice versa.
 *
 * The private key is read from the environment, never written to disk or printed,
 * and wiped from memory after use.
 */

const CONTEXT = 'eclair-skills/release/1:';
const REPOSITORY = 'Jacckisback/eclair-skills';

$root = dirname(__DIR__);
if (!function_exists('sodium_crypto_sign_detached')) {
    fwrite(STDERR, "✗ PHP sodium extension required.\n");
    exit(1);
}
$secret = base64_decode((string) getenv('ECLAIR_SIGNING_KEY'), true);
putenv('ECLAIR_SIGNING_KEY');
if (!is_string($secret) || strlen($secret) !== SODIUM_CRYPTO_SIGN_SECRETKEYBYTES) {
    fwrite(STDERR, "✗ ECLAIR_SIGNING_KEY missing or not a base64 Ed25519 secret key (64 bytes). Nothing signed.\n");
    exit(1);
}
$sumsPath = $root . '/SHA256SUMS.json';
if (!is_file($sumsPath)) {
    fwrite(STDERR, "✗ SHA256SUMS.json missing: run python3 scripts/check_release.py --write first.\n");
    exit(1);
}
$catalog = json_decode((string) file_get_contents($root . '/catalog.json'), true, 32, JSON_THROW_ON_ERROR);
$payload = json_encode([
    'repository' => REPOSITORY,
    'version' => (string) $catalog['catalog_version'],
    'skills' => count($catalog['skills']),
    'sums_file' => 'SHA256SUMS.json',
    'sums_sha256' => hash_file('sha256', $sumsPath),
    'signed_at' => gmdate('Y-m-d\TH:i:s\Z'),
], JSON_UNESCAPED_SLASHES | JSON_THROW_ON_ERROR);

$publicKey = sodium_crypto_sign_publickey_from_secretkey($secret);
$signature = sodium_crypto_sign_detached(CONTEXT . $payload, $secret);
sodium_memzero($secret);

$out = [
    'format' => 'eclair-skills/signature/1',
    'algorithm' => 'Ed25519 (libsodium crypto_sign_detached)',
    'context' => CONTEXT,
    'public_key' => base64_encode($publicKey),
    'payload' => $payload,
    'signature' => base64_encode($signature),
];
file_put_contents($root . '/SIGNATURE.json', json_encode($out, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . "\n");
echo "✓ SIGNATURE.json written (public key " . base64_encode($publicKey) . ")\n";
