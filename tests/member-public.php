<?php
// SPDX-License-Identifier: AGPL-3.0-only
// Experimental isolated member HTTP tests; NOT real CMS integration.
declare(strict_types=1);
namespace Eclair {
    final class Store {
        private static array $db = [];
        public static function read(string $key, mixed $default=null):mixed { return self::$db[$key] ?? $default; }
        public static function write(string $key,mixed $value):void {self::$db[$key]=$value;}
        public static function delete(string $key):void {unset(self::$db[$key]);}
        public static function locked(callable $c):mixed {return $c();}
        public static function keys():array {return array_keys(self::$db);}
    }
    final class Req {
        public static string $verb='GET'; public static bool $https=true; public static array $fields=[];
        public static function isHttps():bool{return self::$https;}
        public static function method():string{return self::$verb;}
        public static function input(string $key,string $default=''):string{return (string)(self::$fields[$key]??$default);}
        public static function ipPrefix():string{return '192.0.2.0';}
        public static function base():string{return '';}
    }
    final class RateLimit {
        public static array $calls=[]; public static array $quota=[];
        public static function attempt(string $key,int $max,int $window,int $block=900):bool {
            self::$calls[]=$key;
            self::$quota[$key]=(self::$quota[$key]??0)+1;
            return self::$quota[$key]<=$max;
        }
        public static function release(string $key):void {self::$quota[$key]=max(0,(self::$quota[$key]??0)-1);}
    }
    final class Security {
        public static bool $valid=true;
        public static function formField():string { return '<input type="hidden" name="_ft" value="opaque">'; }
        public static function checkFormToken():bool{return self::$valid;}
    }
    final class Http {
        public static function redirect(string $url,int $code=302):never {throw new \TestRedirect($url,$code);}
    }
}
namespace {
    define('ECLAIR',true); $_SERVER['HTTPS']='on'; $_SERVER['SERVER_PORT']='80';
    class TestRedirect extends \Exception {public function __construct(public string $target,public int $status) {parent::__construct('redirect');}}
    function e(string $s):string{return htmlspecialchars($s,ENT_QUOTES|ENT_SUBSTITUTE,'UTF-8');}
    $dir=dirname(__DIR__).'/examples/extensions/member-directory';
    foreach(['MemberTransport','MemberAccounts','MemberSessions','MemberPermissions','MemberPublic'] as $file) require_once $dir.'/lib/'.$file.'.php';
    $ext=require $dir.'/extension.php';
    use Eclair\Req;
    use Eclair\Security;
    use Eclair\RateLimit;
    use EclairMemberDirectory\MemberAccounts as A;
    use EclairMemberDirectory\MemberSessions as S;
    $n=0;
    function check(bool $passed,string $label):void {global $n;$n++;if(!$passed){fwrite(STDERR,"FAIL [$n] $label\n");exit(1);}}
    function denied(callable $fn,string $label):void { try {$fn();check(false,$label);}catch(\DomainException|\RuntimeException $e){check(true,$label);} }
    $ctx=['id'=>'member-directory','data'=>'ext/member-directory','settings'=>[],'lang'=>'fr'];
    $v=$ext->loginPage($ctx);
    check(($v['noindex']??false)===true,'login form noindex');
    check(str_contains($v['content'],'name="_ft"'),'login form anti CSRF');
    check(str_contains($v['content'],'method="post"'),'login form uses POST');
    check(!str_contains($v['content'],'/admin'),'member form never includes admin paths');
    Req::$https=false; $_SERVER['HTTPS']='off';
    denied(fn()=> $ext->loginPage($ctx),'login GET requires TLS');
    Req::$https=true; $_SERVER['HTTPS']='on';
    Req::$verb='POST';
    Req::$fields=['email'=>'student@example.com','password'=>'correct long password'];
    Security::$valid=false;
    denied(fn()=> $ext->login($ctx),'login refuses CSRF');
    Security::$valid=true;
    Req::$https=false; $_SERVER['HTTPS']='off';
    denied(fn()=> $ext->login($ctx),'login refuses HTTP');
    Req::$https=true; $_SERVER['HTTPS']='on';
    Req::$fields=['email'=>str_repeat('a',255).'@example.com','password'=>'correct long password'];
    check(($ext->login($ctx)['status']??0)===401,'oversized email rejected');
    Req::$fields=['email'=>'student@example.com','password'=>str_repeat('x',1025)];
    check(($ext->login($ctx)['status']??0)===401,'oversized password rejected');
    Req::$fields=['email'=>'student@example.com','password'=>'correct long password'];
    $res=$ext->login($ctx);
    check(($res['status']??0)===401,'unknown member refused');
    check(count(RateLimit::$calls)===2,'network and account throttles called');
    $pending=A::provision('student@example.com','correct long password');
    check(($ext->login($ctx)['status']??0)===401,'pending member denied');
    $proof=A::issueVerification($pending['id']);
    A::confirmVerification($pending['id'],$proof,'correct long password');
    $logged=$ext->login($ctx);
    check(($logged['redirect']??'')==='/membres/espace','active member successful login');
    check(!array_key_exists('member_id',$logged),'login never returns user id in response');
    $sessionKeys=array_values(array_filter(\Eclair\Store::keys(),fn($k)=>str_starts_with($k,'ext/member-directory/session_')));
    check(count($sessionKeys)===1,'member session stored separately');
    $raw=A::authenticate('student@example.com','correct long password');
    $token=S::create($raw);
    $_COOKIE[S::COOKIE]=$token;
    Req::$verb='GET';
    $profile=$ext->profilePage($ctx);
    check(str_contains($profile['content'],'student@example.com'),'private profile contains own identity');
    check(($profile['noindex']??false)===true,'private profile noindex');
    check(str_contains($profile['content'],'name="_member_csrf"'),'logout form has session CSRF');
    $profile2=A::provision('other@example.com','other correct password');
    check(!str_contains($profile['content'],'other@example.com'),'profile does not leak other member');
    Req::$verb='POST'; Req::$fields=['_member_csrf'=>str_repeat('f',64)];
    check(($ext->logout($ctx)['status']??0)===403,'invalid logout member token refused with 403');
    Req::$fields=['_member_csrf'=>S::resolve($token)['csrf']];
    $logout=$ext->logout($ctx);
    check(($logout['redirect']??'')==='/membres/connexion','logout returns to login');
    check(S::resolve($token)===null,'logout revokes server session');
    $_COOKIE[S::COOKIE]='fake'; Req::$verb='GET';
    try{$ext->profilePage($ctx);check(false,'unauthenticated profile redirect');}
    catch(TestRedirect $e){check($e->target==='/membres/connexion' && $e->status===303,'unauthenticated profile redirected to login');}
    Req::$verb='POST';Req::$fields=['email'=>'student@example.com','password'=>'incorrect long password'];
    $bad=$ext->login($ctx);check(($bad['status']??0)===401,'bad password rejected');
    for($i=0;$i<8;$i++){$bad=$ext->login($ctx);}
    check(($bad['status']??0)===401,'throttled error remains generic');
    check(max(RateLimit::$quota)>6,'throttling activated');
    Req::$verb='GET';
    denied(fn()=> $ext->login($ctx),'login cannot have GET side effects');
    Req::$https=false; $_SERVER['HTTPS']='off';
    denied(fn()=> $ext->profilePage($ctx),'private GET requires TLS');
    echo "PASS: $n isolated public-auth assertions (NOT real HTTP/TLS integration)\n";
}
