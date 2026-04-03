from base64 import b64decode as b64d

enc = open("flag.txt").read().strip()
dec = enc
i = 0

while "{" not in dec:
    i += 1
    dec = b64d(dec).decode()
    
print(dec)

# ABCTF{pr3tty_b4s1c_r1ght?}