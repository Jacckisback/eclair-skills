<?php
declare(strict_types=1);
/**
 * Verifies that this copy of Éclair Skills is exactly the one signed by the maintainer.
 *
 *   php scripts/verify_signature.php            # verify the repository it lives in
 *   php scripts/verify_signature.php /path/to/eclair-skills
 *
 * Checks, in order:
 *   1. SIGNATURE.json is a valid Ed25519 signature by the PINNED maintainer key below
 *      (the same public key as Éclair CMS's updater), with the eclair-skills context;
 *   2. the signed payload names this repository and the SHA-256 of SHA256SUMS.json;
 *   3. every file listed in SHA256SUMS.json exists with the same SHA-256;
 *   4. no extra file and no symbolic link is present (outside .git and caches).
 *
 * Exit code 0 = authentic and intact. Anything else = do not install.
 * The public key is pinned in this file on purpose: never trust the key written in
 * SIGNATURE.json. Compare this constant with Éclair CMS (eclair/app/lib/Update.php, KEY).
 */

const PUBLIC_KEY = 'H+pk0ph+U+csV7aoGTUZp8hsWBrjvtxavotdKqJuYEs=';
const CONTEXT = 'eclair-skills/release/1:';
const REPOSITORY = 'Jacckisback/eclair-skills';
const IGNORED = ['SHA256SUMS.json', 'SIGNATURE.json'];

function fail(string $msg): never
{
    fwrite(STDERR, "✗ $msg\n✗ DO NOT INSTALL: this copy is not the one signed by the maintainer.\n");
    exit(1);
}

$root = rtrim($argv[1] ?? dirname(__DIR__), '/');
if (!function_exists('sodium_crypto_sign_verify_detached')) {
    fail('PHP sodium extension required to verify the signature.');
}
$sigFile = $root . '/SIGNATURE.json';
if (!is_file($sigFile)) {
    fail('SIGNATURE.json missing (unsigned copy).');
}
$sig = json_decode((string) file_get_contents($sigFile), true);
if (!is_array($sig) || ($sig['format'] ?? '') !== 'eclair-skills/signature/1' || !is_string($sig['payload'] ?? null)) {
    fail('SIGNATURE.json has an unknown format.');
}
$key = base64_decode(PUBLIC_KEY, true);
$raw = base64_decode((string) ($sig['signature'] ?? ''), true);
if (!is_string($raw) || strlen($raw) !== SODIUM_CRYPTO_SIGN_BYTES
    || !sodium_crypto_sign_verify_detached($raw, CONTEXT . $sig['payload'], $key)) {
    fail('Signature invalid for the pinned maintainer key.');
}
$payload = json_decode($sig['payload'], true);
if (!is_array($payload) || ($payload['repository'] ?? '') !== REPOSITORY || ($payload['sums_file'] ?? '') !== 'SHA256SUMS.json') {
    fail('Signed payload does not describe this repository.');
}
$sumsPath = $root . '/SHA256SUMS.json';
if (!is_file($sumsPath) || !hash_equals((string) $payload['sums_sha256'], hash_file('sha256', $sumsPath))) {
    fail('SHA256SUMS.json differs from the signed one.');
}
$sums = json_decode((string) file_get_contents($sumsPath), true);
if (!is_array($sums)) {
    fail('SHA256SUMS.json unreadable.');
}

$found = [];
$it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($root, FilesystemIterator::SKIP_DOTS), RecursiveIteratorIterator::SELF_FIRST);
foreach ($it as $file) {
    $rel = substr($file->getPathname(), strlen($root) + 1);
    $parts = explode('/', $rel);
    if (in_array('.git', $parts, true) || in_array('__pycache__', $parts, true) || str_ends_with($rel, '.pyc')) {
        continue;
    }
    if ($file->isLink()) {
        fail("Symbolic link refused: $rel");
    }
    if ($file->isFile() && !in_array($rel, IGNORED, true)) {
        $found[$rel] = true;
    }
}
foreach ($sums as $rel => $digest) {
    $p = $root . '/' . $rel;
    if (!is_file($p)) {
        fail("Missing file: $rel");
    }
    if (!hash_equals((string) $digest, hash_file('sha256', $p))) {
        fail("Modified file: $rel");
    }
    unset($found[$rel]);
}
if ($found) {
    fail('Unexpected file(s): ' . implode(', ', array_keys($found)));
}
printf("✓ Authentic: Éclair Skills %s, %d files, signed %s by key %s\n",
    $payload['version'] ?? '?', count($sums), $payload['signed_at'] ?? '?', PUBLIC_KEY);
