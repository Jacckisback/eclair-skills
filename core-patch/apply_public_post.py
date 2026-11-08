#!/usr/bin/env python3
"""Reviewable, non-destructive experimental Éclair 2.0 public POST patch.

Requires clean Git *feature* branch; refuses main/master, unexpected source anchors, wrong version.
Use --check first. Does not automatically publish or merge anything.
"""
from pathlib import Path
import argparse, subprocess, sys

p=argparse.ArgumentParser()
p.add_argument('--checkout',type=Path,required=True)
p.add_argument('--apply',action='store_true',help='write a checked patch to a clean feature branch')
args=p.parse_args()
root=args.checkout.resolve()
def git(*cmd):
    v=subprocess.run(['git','-C',str(root),*cmd],capture_output=True,text=True)
    if v.returncode: raise RuntimeError(v.stderr.strip() or 'Git failed')
    return v.stdout.strip()
if not (root/'eclair/index.php').exists(): raise SystemExit('Not an Éclair repository root')
if "define('ECLAIR_VERSION', '2.0.0')" not in (root/'eclair/index.php').read_text():
    raise SystemExit('Refusing: expected Éclair 2.0.0')
if args.apply:
    if git('branch','--show-current') in ('main','master',''): raise SystemExit('Refusing main/master/detached HEAD')
    if git('status','--porcelain'): raise SystemExit('Refusing dirty worktree')

file=root/'eclair/app/lib/Extensions.php'
s=file.read_text()
needle="""    /** Route publique d'une capacité active : page rendue dans le thème, en-têtes SEO et de sécurité du noyau. */
    public static function route(string $path): void
    {
        foreach (self::active() as $id => $m) {
            foreach ($m['routes']['public'] as $r) {
                if ($r['path'] === $path && in_array(Req::method(), ['GET', 'HEAD'], true)) {
                    $page = self::call($id, $r['handler'], [self::context($id)]);
                    if (is_array($page) && is_string($page['content'] ?? null)) {
                        Site::extension($path, $page, $r['cache']);
                    }
                }
            }
        }
    }
"""
replacement="""    /** Experimental public routes: POST is never cached, TLS and stateless CSRF mandatory. */
    public static function route(string $path): void
    {
        foreach (self::active() as $id => $m) {
            foreach ($m['routes']['public'] as $r) {
                if ($r['path'] !== $path) {
                    continue;
                }
                $method = Req::method();
                if ($r['method'] === 'POST' && $method === 'POST') {
                    // Never accept an arbitrary client X-Forwarded-Proto header as TLS proof.
                    $https = strtolower((string) ($_SERVER['HTTPS'] ?? ''));
                    $directTls = in_array($https, ['on', '1', 'true'], true)
                        || (string) ($_SERVER['SERVER_PORT'] ?? '') === '443';
                    $trustedProxy = defined('ECLAIR_MEMBER_TRUSTED_PROXY_IP') ? ECLAIR_MEMBER_TRUSTED_PROXY_IP : '';
                    $remoteIp = (string) ($_SERVER['REMOTE_ADDR'] ?? '');
                    $proxyTls = is_string($trustedProxy) && filter_var($trustedProxy, FILTER_VALIDATE_IP) !== false
                        && filter_var($remoteIp, FILTER_VALIDATE_IP) !== false
                        && inet_pton($trustedProxy) === inet_pton($remoteIp)
                        && strtolower((string) ($_SERVER['HTTP_X_FORWARDED_PROTO'] ?? '')) === 'https';
                    if (!$directTls && !$proxyTls) {
                        Http::send('HTTPS required', 403, ['Cache-Control: private, no-store']);
                    }
                    if (!Security::checkFormToken()) {
                        Http::send('Form proof expired', 419, ['Cache-Control: private, no-store']);
                    }
                    header('Cache-Control: private, no-store');
                    header('X-Robots-Tag: noindex, nofollow');
                    $response = self::call($id, $r['handler'], [self::context($id)]);
                    if (is_array($response) && isset($response['redirect'])) {
                        $to = (string) $response['redirect'];
                        if (!preg_match('~^/[a-z0-9][a-z0-9/-]{0,99}$~D', $to)) {
                            Http::send('Invalid redirect', 500, ['Cache-Control: private, no-store']);
                        }
                        Http::redirect(path_to($to), 303);
                    }
                    if (is_array($response)) {
                        $status = (int) ($response['status'] ?? 500);
                        if (!in_array($status, [200, 400, 401, 403, 409, 422, 429, 500, 503], true)) {
                            $status = 500;
                        }
                        Http::send((string) ($response['body'] ?? 'Request failed'), $status, [
                            'Content-Type: text/plain; charset=utf-8', 'Cache-Control: private, no-store',
                            'X-Robots-Tag: noindex, nofollow', 'X-Content-Type-Options: nosniff',
                        ]);
                    }
                    Http::send('Request failed', 500, ['Cache-Control: private, no-store']);
                }
                if ($r['method'] === 'GET' && in_array($method, ['GET', 'HEAD'], true)) {
                    $page = self::call($id, $r['handler'], [self::context($id)]);
                    if (is_array($page) && is_string($page['content'] ?? null)) {
                        Site::extension($path, $page, $r['cache']);
                    }
                }
            }
        }
    }
"""
assert s.count(needle)==1, 'Core public route anchor changed, aborting'
s2=s.replace(needle,replacement)
# POST public routes are allowed only with cache=false. GET routes keep original validation.
a="""        foreach ($m['routes']['public'] as $r) {
            if (!preg_match('~^/[a-z0-9][a-z0-9/-]{0,99}$~', $r['path'])"""
b="""        foreach ($m['routes']['public'] as $r) {
            if (!in_array($r['method'], ['GET', 'POST'], true) || ($r['method'] === 'POST' && $r['cache'])) {
                $errors[] = 'Public POST routes must use cache=false and GET/POST only.';
            }
            if (!preg_match('~^/[a-z0-9][a-z0-9/-]{0,99}$~', $r['path'])"""
assert s2.count(a)==1, 'Core validation anchor changed, aborting'
s2=s2.replace(a,b)

schema=root/'docs/schemas/extension.schema.json'
t=schema.read_text()
old='"method": { "enum": ["GET"] }'
new='"method": { "enum": ["GET", "POST"] }'
assert t.count(old)==1, 'Schema anchor changed, aborting'
t2=t.replace(old,new)
# Restrict GET/POST pairs to exact same route semantics with distinct methods; activation already rejects competing modules.
print('Patch anchors validated. Target: Éclair 2.0.0; public POST+CSRF+TLS+no-store.')
if args.apply:
    file.write_text(s2)
    schema.write_text(t2)
    print('Modified Extensions.php and extension.schema.json on the feature branch. Run all official tests.')
else: print('Dry-run only. Re-run with --apply on a clean feature branch to change files.')
