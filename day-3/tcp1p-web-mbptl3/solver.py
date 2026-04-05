import requests
import re

BASE_URL_ADMIN = "http://gzcli.1pc.tf:40796"
res = requests.get(BASE_URL_ADMIN)
print(res.text)

flag_format = "MBPTL-3{.*}"
flag = re.findall(flag_format, res.text)[0]
print(flag)

# MBPTL-3{561fcbc74844bcc32731cfb3508c86d1}