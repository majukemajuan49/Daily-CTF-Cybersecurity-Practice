import random

flag = "TCP1P{test_flag}"

def enc(flag):
    c = ""
    key_1 = random.randint(0, 64)
    key_2 = random.randint(0, 64)
    print(f"key_1: {key_1}, key_2: {key_2}")
    for i, chr in enumerate(flag):
        if (i % 2 == 0):
            c += ("A" * (ord(chr) * key_1)) + "\n"
        if (i % 2 == 1):
            c += ("B" * (ord(chr) * key_2)) + "\n"
    return c

cipher = enc(flag)
print(cipher)

print(len(cipher.split("\n")) - 1 == len(flag))