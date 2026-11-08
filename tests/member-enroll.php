<?php
// SPDX-License-Identifier: AGPL-3.0-only
// Isolated prototype tests only: fake Mail / Security / Store, not a live Eclair deployment.
declare(strict_types=1);
namespace Eclair {
    final class Store {
        public static array $db=[];
        public static function read(string $key,mixed $fallback=null):mixed{return self::$db[$key]??$fallback;}
        public static function write(string $key,mixed $data):void{self::$db[$key]=$data;}
        public static function delete(string $key):void{unset(self::$db[$key]);}
        public static function locked(callable $fn):mixed{return $fn();}
    }
    final class Req {
        public static string $method='GET';public static bool $https=true;public static array $fields=[];public static array $query=[];
        public static function method():string{return self::$method;}
        public static function isHttps():bool{return self::$https;}
        public static function input(string $key,string $fallback=''):string{return is_string(self::$fields[$key]??null)?self::$fields[$key]:$fallback;}
        public static function query(string $key,string $fallback=''):string{return is_string(self::$query[$key]??null)?self::$query[$key]:$fallback;}
        public static function ipPrefix():string{return '192.0.2.0';}
        public static function base():string{return '';}
    }
    final class Security {
        public static bool $valid=true;
        public static function checkFormToken():bool{return self::$valid;}
        public static function formField():string{return '<input type="hidden" name="_ft" value="mockproof">';}
    }
    final class RateLimit {
        public static array $counts=[];public static array $calls=[];
        public static function attempt(string $key,int $max,int $window,int $block=900):bool {
            self::$counts[$key]=(self::$counts[$key]??0)+1;
            self::$calls[]=$key;
            return self::$counts[$key]<=$max;
        }
        public static function release(string $key):void{self::$counts[$key]=max(0,(self::$counts[$key]??0)-1);}
    }
    final class Settings {
        public static string $url='https://verified.example.test';public static bool $verified=true;
        public static function get(string $key,mixed $fallback=null):mixed{return $key==='url'?self::$url:$fallback;}
        public static function verified():bool{return self::$verified;}
    }
    final class Mail {
        public static array $sent=[];public static bool $ok=true;
        public static function send(string $to,string $subject,string $body,string $replyTo=''):bool {
            self::$sent[]=['to'=>$to,'subject'=>$subject,'body'=>$body];return self::$ok;
        }
    }
}
namespace {
    define('ECLAIR',true); $_SERVER['HTTPS']='on'; $_SERVER['SERVER_PORT']='80';
    function e(string $s):string{return htmlspecialchars($s,ENT_QUOTES|ENT_SUBSTITUTE,'UTF-8');}
    $dir=dirname(__DIR__).'/examples/extensions/member-directory';
    foreach(['MemberTransport','MemberAccounts','MemberSessions','MemberPermissions','MemberPublic','MemberEnroll'] as $name){require_once $dir.'/lib/'.$name.'.php';}
    $extension=require $dir.'/extension.php';
    use Eclair\Req; use Eclair\Security; use Eclair\Settings; use Eclair\Mail;
    use EclairMemberDirectory\MemberAccounts as Account;
    use EclairMemberDirectory\MemberSessions as Session;
    $n=0;
    function ok(bool $result,string $name):void{global $n;$n++;if(!$result){fwrite(STDERR,"FAIL $n $name\n");exit(1);}}
    function throws(callable $fn,string $name):void{try{$fn();ok(false,$name);}catch(\DomainException|\InvalidArgumentException $e){ok(true,$name);}}
    function post(array $fields):void{Req::$method='POST';Req::$fields=$fields;}
    function get(array $query=[]):void{Req::$method='GET';Req::$query=$query;Req::$fields=[];}
    function tokenFromMail():array{
        $mail=end(Mail::$sent);preg_match('~https://[^\s]+~',$mail['body'],$m);
        $url=$m[0]??'';parse_str((string)parse_url($url,PHP_URL_QUERY),$params);
        return ['url'=>$url,'id'=>$params['id']??'', 'token'=>$params['token']??''];
    }
    $off=['id'=>'member-directory','lang'=>'fr','data'=>'ext/member-directory','settings'=>['registration_enabled'=>false,'recovery_enabled'=>false]];
    $on=$off;$on['settings']=['registration_enabled'=>true,'recovery_enabled'=>true];
    get(); throws(fn()=> $extension->signupPage($off),'signup off by default');
    throws(fn()=> $extension->recoverPage($off),'recovery off by default');
    $p=$extension->signupPage($on);
    ok($p['noindex']===true,'signup form noindex');
    ok(str_contains($p['content'],'name="_ft"'),'signup form double submit proof');
    ok(str_contains($p['content'],'type="email"'),'signup accepts email');
    ok(Mail::$sent===[],'GET does not send email');
    Req::$https=false; $_SERVER['HTTPS']='off';throws(fn()=> $extension->signupPage($on),'GET requires TLS');Req::$https=true; $_SERVER['HTTPS']='on';
    post(['email'=>'new.member@example.test']);Security::$valid=false;
    throws(fn()=> $extension->signup($on),'POST rejects invalid CSRF');Security::$valid=true;
    Req::$https=false; $_SERVER['HTTPS']='off';throws(fn()=> $extension->signup($on),'POST requires TLS');Req::$https=true; $_SERVER['HTTPS']='on';
    Settings::$verified=false;throws(fn()=> $extension->signup($on),'unverified canonical site rejected');Settings::$verified=true;
    Settings::$url='http://verified.example.test';throws(fn()=> $extension->signup($on),'http canonical rejected');
    Settings::$url='https://evil.example.test@verified.example.test';throws(fn()=> $extension->signup($on),'canonical credentials rejected');
    Settings::$url='https://verified.example.test';
    $r=$extension->signup($on);ok($r['status']===200,'signup responds generically');
    ok(count(Mail::$sent)===1,'signup sends one verification message');
    $mail=tokenFromMail();ok(str_starts_with($mail['url'],'https://verified.example.test/membres/verification?'),'uses canonical URL');
    ok(preg_match('/^[a-f0-9]{64}$/',$mail['token'])===1,'mail proof has 256 bits');
    $id=$mail['id'];$pending=Account::find($id);
    ok(($pending['state']??'')==='pending','member starts pending');
    ok(!isset($pending['verification']['token']),'raw proof is not persisted');
    ok($pending['verification']['hash']===hash('sha256',$mail['token']),'only digest stored');
    post(['email'=>'new.member@example.test']);$duplicate=$extension->signup($on);
    ok($duplicate['status']===200,'duplicate not disclosed');ok(count(Mail::$sent)===1,'duplicate does not send');
    get(['id'=>$id,'token'=>$mail['token']]);$verifyForm=$extension->verifyPage($on);
    ok(str_contains($verifyForm['content'],'name="token"'),'verify GET merely displays secure form');
    ok(Account::find($id)['state']==='pending','GET does not verify');
    post(['id'=>$id,'token'=>str_repeat('a',64),'password'=>'long valid password']);
    ok($extension->verify($on)['status']===400,'wrong verification proof rejected');
    post(['id'=>$id,'token'=>$mail['token'],'password'=>'short']);
    ok($extension->verify($on)['status']===400,'weak password rejected');
    post(['id'=>$id,'token'=>$mail['token'],'password'=>'long valid password']);
    ok($extension->verify($on)['redirect']==='/membres/connexion','verified member redirect');
    ok(Account::find($id)['state']==='active','verified member activated');
    ok(!isset(Account::find($id)['verification']),'proof consumed');
    ok($extension->verify($on)['status']===400,'verification proof single use');
    ok(Account::authenticate('new.member@example.test','long valid password')!==null,'verified password works');
    $session=Session::create(Account::authenticate('new.member@example.test','long valid password'));
    ok(Session::resolve($session)!==null,'member session valid before reset');
    get();$resetForm=$extension->recoverPage($on);
    ok(str_contains($resetForm['content'],'name="_ft"'),'recovery form CSRF');
    post(['email'=>'unknown@example.test']);$r=$extension->recover($on);
    ok($r['status']===200,'unknown account generic');ok(count(Mail::$sent)===1,'unknown account sends nothing');
    post(['email'=>'new.member@example.test']);$r=$extension->recover($on);
    ok($r['status']===200,'known account generic same status');ok(count(Mail::$sent)===2,'known account recovery mail sent');
    $reset=tokenFromMail();ok(str_starts_with($reset['url'],'https://verified.example.test/membres/reinitialisation?'),'recovery link canonical');
    ok(!isset(Account::find($id)['reset']['token']),'raw recovery proof not persisted');
    get(['id'=>$id,'token'=>$reset['token']]);$newForm=$extension->resetPage($on);
    ok(str_contains($newForm['content'],'name="_ft"'),'reset page CSRF');
    ok(Session::resolve($session)!==null,'GET does not reset account');
    post(['id'=>$id,'token'=>$reset['token'],'password'=>'a replacement password']);
    ok($extension->reset($on)['redirect']==='/membres/connexion','reset success redirect');
    ok(Session::resolve($session)===null,'reset invalidates prior sessions');
    ok(Account::authenticate('new.member@example.test','long valid password')===null,'old password denied');
    ok(Account::authenticate('new.member@example.test','a replacement password')!==null,'new password works');
    ok($extension->reset($on)['status']===400,'reset proof single use');
    $disabled=Account::provision('disabled@example.test','long valid password');
    Account::disable($disabled['id']);
    throws(fn()=>Account::issueReset($disabled['id']),'disabled account cannot receive reset proof');
    post(['id'=>$id,'token'=>str_repeat('a',10240),'password'=>'long valid password']);
    ok($extension->reset($on)['status']===400,'oversized proof rejected');
    post(['email'=>str_repeat('a',350)]);
    ok($extension->signup($on)['status']===200,'oversized email generic');
    // Direct TLS vs spoofed proxy headers: bypass must require an explicitly trusted REMOTE_ADDR.
    get(); $_SERVER['HTTPS']='off'; $_SERVER['SERVER_PORT']='80';
    $_SERVER['REMOTE_ADDR']='192.0.2.11'; $_SERVER['HTTP_X_FORWARDED_PROTO']='https';
    ok(!\EclairMemberDirectory\MemberTransport::isSecure(),'spoofed forwarded HTTPS not trusted');
    throws(fn()=> $extension->signupPage($on),'spoofed X-Forwarded-Proto cannot serve auth page');
    define('ECLAIR_MEMBER_TRUSTED_PROXY_IP','192.0.2.10');
    ok(!\EclairMemberDirectory\MemberTransport::isSecure(),'different proxy IP rejected');
    $_SERVER['REMOTE_ADDR']='192.0.2.10';
    ok(\EclairMemberDirectory\MemberTransport::isSecure(),'explicitly trusted proxy HTTPS allowed');
    $_SERVER['HTTP_X_FORWARDED_PROTO']='http';
    ok(!\EclairMemberDirectory\MemberTransport::isSecure(),'trusted proxy without HTTPS marker rejected');
    $_SERVER['HTTPS']='on';unset($_SERVER['HTTP_X_FORWARDED_PROTO']);
    get();throws(fn()=> $extension->verify($on),'GET cannot verify');
    ok(count(Mail::$sent)===2,'no unexpected mail from invalid calls');
    // SMTP transport rejects registration: pending account must not permanently reserve email.
    Mail::$ok=false;
    post(['email'=>'failed.delivery@example.test']);
    $failed=$extension->signup($on);
    ok($failed['status']===200,'failed SMTP stays generic');
    ok(Account::findByEmail('failed.delivery@example.test')===null,'failed mail rolls back pending email index');
    ok(count(Mail::$sent)===3,'mail transport was attempted');
    Mail::$ok=true;
    echo "PASS: $n isolated member enrollment/recovery assertions (not full HTTP, SMTP or CMS tests)\n";
}
