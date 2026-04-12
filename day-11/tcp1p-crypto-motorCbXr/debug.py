import os
import struct

FLAG = b"RAMADAN{test_flagtest_flagtest_flagAB}"
assert FLAG.startswith(b"RAMADAN{") and FLAG.endswith(b"}")

KEY_SIZE = 8
KEY = os.urandom(KEY_SIZE)

p64 = lambda x: struct.pack('<Q', x)
u64 = lambda x: struct.unpack('<Q', x)[0]

def encrypt(plaintext, key):
    padlen = 8
    
    plaintext += bytes([padlen] * padlen)
    print(f'{plaintext = }')
    print(f'{len(plaintext) = }')
    # always ada tambahan "\x08\x08\x08\x08\x08\x08\x08\x08"
    # len plaintextnya jadi 96 + 8 = 104

    iv = os.urandom(KEY_SIZE)
    print(f'{iv = }')
    ciphertext = iv
    
    # dibagi jadi 13 block
    for i in range(0, len(plaintext), KEY_SIZE):
        print(f'block ke-{i//KEY_SIZE + 1}')
        p_block = plaintext[i:i+KEY_SIZE]
        print(f'{p_block = }')
        c_block = p64(u64(iv) ^ u64(p_block) ^ u64(key))
        print(f'{c_block = }')
        ciphertext += c_block
        iv = c_block

    print(p64(u64(ciphertext[:8]) ^ u64(b'RAMADAN{') ^ u64(ciphertext[8:16])) == KEY)
    
    return ciphertext

def decrypt(ciphertext, key):
    iv, ciphertext = ciphertext[:KEY_SIZE], ciphertext[KEY_SIZE:]

    plaintext = b''
    for i in range(0, len(ciphertext), KEY_SIZE):
        c_block = ciphertext[i:i+KEY_SIZE]
        p_block = p64(u64(iv) ^ u64(c_block) ^ u64(key))
        plaintext += p_block
        iv = c_block

    return plaintext.rstrip(plaintext[-1:])

if __name__ == '__main__':
    FLAG = FLAG.ljust(96, b'A')
    print(f'{FLAG = }') # panjangnya 96
    print(f'{KEY = }')
    
    ENC_FLAG = encrypt(FLAG, KEY)
    
    print("Nih Bang!, pecahin yak:", ENC_FLAG)
    assert decrypt(ENC_FLAG, KEY) == FLAG

