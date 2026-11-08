<?php
// SPDX-License-Identifier: AGPL-3.0-only
// Isolated contract tests. Does NOT run the real Éclair CMS.
declare(strict_types=1);
namespace Eclair {
    final class Store {
        private static array $items = [];
        public static function read(string $key, mixed $default = null): mixed { return self::$items[$key] ?? $default; }
        public static function write(string $key, mixed $data): void { self::$items[$key] = $data; }
        public static function delete(string $key): void { unset(self::$items[$key]); }
        public static function locked(callable $callback): mixed { return $callback(); }
        public static function keys(): array { return array_keys(self::$items); }
    }
    final class Req {
        public static array $input = [];
        public static string $method = 'GET';
        public static function input(string $name, string $default=''): string { return (string)(self::$input[$name]??$default); }
        public static function method(): string { return self::$method; }
        public static function base(): string { return ''; }
        public static function isHttps(): bool { return false; }
    }
    final class Auth { public static bool $authorized=true; public static function can(string $area): bool { return $area==='users' && self::$authorized; } }
    final class Settings { public static function get(string $key, mixed $default=null): mixed { return $key==='admin_path'?'gestion':$default; } }
    final class Security {
        public static bool $csrf=true;
        public static function checkCsrf(): bool { return self::$csrf; }
        public static function csrfField(): string { return '<input type="hidden" name="_csrf" value="TEST">'; }
    }
}
namespace {
    define('ECLAIR', true);
    function e(string $input): string { return htmlspecialchars($input, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'); }
    $mod = dirname(__DIR__) . '/examples/extensions/member-directory';
    foreach (['MemberAccounts','MemberSessions','MemberPermissions'] as $class) require_once $mod . '/lib/' . $class . '.php';
    $ext = require $mod . '/extension.php';
    use EclairMemberDirectory\MemberAccounts as Accounts;
    use EclairMemberDirectory\MemberSessions as Sessions;
    use EclairMemberDirectory\MemberPermissions as Permissions;
    function check(bool $pass, string $message): void {
        static $n=0; $n++;
        if (!$pass) {fwrite(STDERR, "FAIL [$n] $message\n");exit(1);}
        $GLOBALS['checks']=$n;
    }
    function reject(callable $f, string $message): void {
        try {$f();check(false,$message);} catch (\InvalidArgumentException|\DomainException|\RuntimeException $e) { check(true,$message); }
    }
    $ctx=['data'=>'ext/member-directory','settings'=>[],'lang'=>'fr','id'=>'member-directory'];
    $ext->migrate('001-directory',$ctx);
    check(\Eclair\Store::read('ext/member-directory/meta')['schema']===1,'initial migration');
    $ext->migrate('001-directory',$ctx);
    check(count(\Eclair\Store::keys())===1,'migration idempotent');
    check(method_exists($ext,'adminPage'),'native admin GET handler');
    check(method_exists($ext,'create'),'native admin POST create handler');
    check(method_exists($ext,'disable'),'native admin POST disable handler');
    check(method_exists($ext,'login'),'experimental public POST login handler exists');
    $view=$ext->adminPage([],$ctx);
    check(str_contains($view['html'],'/_csrf')||str_contains($view['html'],'name="_csrf"'),'admin form has CSRF input');
    check(str_contains($view['html'],'/gestion/x/member-directory/create'),'admin form link scoped');
    \Eclair\Auth::$authorized=false;
    reject(fn()=> $ext->adminPage([],$ctx),'reject unauthorized admin GET');
    \Eclair\Auth::$authorized=true;
    \Eclair\Req::$method='POST';
    \Eclair\Security::$csrf=false;
    \Eclair\Req::$input=['email'=>'one@example.com'];
    reject(fn()=> $ext->create([],$ctx),'reject CSRF invalid create');
    \Eclair\Security::$csrf=true;
    \Eclair\Auth::$authorized=false;
    reject(fn()=> $ext->create([],$ctx),'reject nonadmin create');
    \Eclair\Auth::$authorized=true;
    \Eclair\Req::$method='GET';
    reject(fn()=> $ext->create([],$ctx),'reject GET modifying account');
    \Eclair\Req::$method='POST';
    $r=$ext->create([],$ctx);
    check(($r['redirect']??null)==='x/member-directory','admin provision return redirect');
    check(Accounts::findByEmail('one@example.com')!==null,'admin created record');
    $listHtml=$ext->adminPage([],$ctx)['html'];
    check(str_contains($listHtml,'one@example.com'),'authorized admin can list member');
    check(str_contains($listHtml,'/gestion/x/member-directory/disable'),'authorized admin can disable member via POST');
    $m=Accounts::findByEmail('one@example.com');
    check(($m['state']??null)==='pending','pending by default');
    check(($m['roles']??null)===['member'],'member role only');
    check(!isset(Accounts::profile($m)['password_hash']),'no password in profile');
    check(Accounts::authenticate('one@example.com','anything')===null,'pending account cannot authenticate');
    check(!in_array('members/email_index',\Eclair\Store::keys(),true),'no legacy global member index');
    check(!in_array('users',\Eclair\Store::keys(),true),'admin user registry untouched');
    foreach (\Eclair\Store::keys() as $key) check(str_starts_with($key,'ext/member-directory/'),'data module-isolated: '.$key);
    reject(fn()=> $ext->create([],$ctx),'duplicate email refused');
    reject(fn()=>Accounts::provision('bad-email','a very long password'),'bad email refused');
    reject(fn()=>Accounts::provision('two@example.com','tiny'),'weak password length refused');
    $profile=Accounts::provision('two@example.com','complex password 123456');
    check($profile['state']==='pending','direct provision still pending');
    reject(fn()=>Sessions::create($profile),'pending cannot create session');
    $proof=Accounts::issueVerification($profile['id']); // emulate delivery to mailbox (not implemented)
    check(strlen($proof)===64 && ctype_xdigit($proof),'email proof is random 256 bits');
    check(Accounts::find($profile['id'])['verification']['hash']!==$proof,'verification proof not stored as plaintext');
    reject(fn()=>Accounts::confirmVerification($profile['id'],'invalid','new complex password 123'),'bad email proof rejected');
    Accounts::confirmVerification($profile['id'],$proof,'complex password 123456');
    reject(fn()=>Accounts::confirmVerification($profile['id'],$proof,'complex password 123456'),'email proof is single use');
    $expired=Accounts::provision('expired@example.com','long random password 123456');
    $expiredToken=Accounts::issueVerification($expired['id']);
    $record=Accounts::find($expired['id']);
    $record['verification']['expires']=time()-1;
    \Eclair\Store::write('ext/member-directory/member_'.$expired['id'],$record);
    reject(fn()=>Accounts::confirmVerification($expired['id'],$expiredToken,'complex password 123456'),'expired email proof rejected');
    $active=Accounts::authenticate('two@example.com','complex password 123456');
    check(is_array($active)&&$active['state']==='active','trusted activation/authentication succeeds');
    check(Accounts::authenticate('two@example.com','wrong')===null,'wrong password denied');
    check(Accounts::authenticate('nobody@example.com','wrong')===null,'unknown email denied');
    $token=Sessions::create($active);
    check(strlen($token)===64 && ctype_xdigit($token),'session token 256 bits hex');
    check(Sessions::resolve($token)['member']['id']===$active['id'],'valid session resolves');
    check(!in_array($token, array_map('strval',\Eclair\Store::keys()),true),'plaintext token not stored in key');
    check(Sessions::verifyCsrf($token,Sessions::resolve($token)['csrf']),'valid CSRF accepted');
    check(!Sessions::verifyCsrf($token,str_repeat('0',64)),'invalid CSRF rejected');
    check(Sessions::resolve('forged')===null,'forged session token rejected');
    $perm=new Permissions();
    $perm->grant('member','lms:course-read','own');
    check(!$perm->allows($token,'lms:course-read'),'own grant requires owner id');
    check($perm->allows($token,'lms:course-read',$active['id']),'owner access allowed');
    check(!$perm->allows($token,'lms:course-read',$m['id']),'other member access denied');
    check(!$perm->allows('forged','lms:course-read',$active['id']),'forged token never grants access');
    check(!$perm->allows($token,'commerce:orders-read',$active['id']),'unknown capability denied');
    reject(fn()=> $perm->grant('admin','shop:refund','any'),'admin is forbidden member role');
    reject(fn()=> $perm->grant('member','lms:course-read','own'),'duplicate policy rejected');
    reject(fn()=>Accounts::setRoles($active['id'],['admin']),'cannot assign Eclair admin role');
    Accounts::setRoles($active['id'],['student']);
    check(Sessions::resolve($token)===null,'role change revokes session by epoch');
    $next=Accounts::authenticate('two@example.com','complex password 123456');
    $fresh=Sessions::create($next);
    \Eclair\Req::$input=['id'=>$active['id']];
    $ext->disable([],$ctx);
    check(Accounts::find($active['id'])['state']==='disabled','admin disabled member');
    check(Sessions::resolve($fresh)===null,'disabled member session invalid');
    check(Accounts::authenticate('two@example.com','complex password 123456')===null,'disabled cannot authenticate');
    reject(fn()=>Sessions::create($active),'stale profile cannot create session');
    \Eclair\Security::$csrf=false;
    reject(fn()=> $ext->disable([],$ctx),'disable requires CSRF');
    reject(fn()=>Sessions::setCookie(str_repeat('a',64)),'TLS required for member cookies');
    echo 'PASS: '.$GLOBALS['checks'].' isolated PHP assertions — Member Directory (not real Éclair HTTP integration)'.PHP_EOL;
}
