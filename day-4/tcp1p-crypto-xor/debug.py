from Crypto.Util.number import *
import random

flag = b"TCP1P{testing_flag}"

key_1 = int(''.join(str(random.randint(0, 9)) for _ in range(128)))
key_2 = int(''.join(str(random.randint(0, 9)) for _ in range(128)))
key_xor = key_1 ^ key_2

cipher = bytes_to_long(flag) ^ key_2
# print([cipher, key_1, key_xor])

print(f"{key_1 = }")
print(f"{key_2 = }")
print(f"{key_xor = }")
print(f"{cipher = }")

assert key_1 ^ key_xor == key_2
assert cipher ^ key_2 == bytes_to_long(flag)