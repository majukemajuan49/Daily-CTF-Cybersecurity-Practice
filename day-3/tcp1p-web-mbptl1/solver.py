import requests
import re

BASE_URL = "http://gzcli.1pc.tf:40731/index.php"

res = requests.get(BASE_URL)
print(res.text)
flag_format = "MBPTL-1{.*}"
flag = re.findall(flag_format, res.text)[0]
print(flag)

# MBPTL-1{c54fece87eff31e3e3eba57f82e33616}