import os
from pwn import xor
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = os.urandom(16)
iv = os.urandom(16)
cipher = AES.new(key, AES.MODE_CBC, iv)

pt = b"TCP1P{test_flag}TCP1P{test_flag}TCP1P{test_flag}TCP1P{test_flag}"

ori_ct = cipher.encrypt(pt)
print(f'{ori_ct = }')

padded_ct = pad(ori_ct, 16)
print(f'{padded_ct = }')

ct = xor(padded_ct, key)
print(f"{iv = }")
print(f"{ct = }")

print(xor(ct[-16:], b'\x10'*16) == key)