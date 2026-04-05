import requests
import re

BASE_URL = "http://gzcli.1pc.tf:40731/index.php"

res = requests.get(BASE_URL)
header = res.headers
print(header)

flag = header.get('X-MBPTL')
print(flag)

# MBPTL-2{2538dc5426d2e3ca16957a091bf8c0f3}