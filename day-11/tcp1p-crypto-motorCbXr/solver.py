import os
import struct

KEY_SIZE = 8

p64 = lambda x: struct.pack('<Q', x)
u64 = lambda x: struct.unpack('<Q', x)[0]

def decrypt(ciphertext, key):
    iv, ciphertext = ciphertext[:KEY_SIZE], ciphertext[KEY_SIZE:]

    plaintext = b''
    for i in range(0, len(ciphertext), KEY_SIZE):
        c_block = ciphertext[i:i+KEY_SIZE]
        p_block = p64(u64(iv) ^ u64(c_block) ^ u64(key))
        plaintext += p_block
        iv = c_block

    return plaintext.rstrip(plaintext[-1:])

ciphertext = bytes.fromhex('a6d869161e868078527902778bb36050aca976082df6ba6b550a126ba3ec244fac93043e2dffb968551d1169a3e7244880cd593433d2cb5a676c3e55a3e7244880cd593433d2cb5a676c3e55a3e7244880cd593433d2cb5a676c3e55a3e7244880cd593433d2cb5a2e25771ceaae6d01')

KEY = p64(u64(ciphertext[:8]) ^ u64(b'RAMADAN{') ^ u64(ciphertext[8:16]))

FLAG = decrypt(ciphertext, KEY).decode()
print(FLAG)
# RAMADAN{X0R_w1th_CBC_n0w_y0u_g3t_n3w_l3ss0n}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# RAMADAN{X0R_w1th_CBC_n0w_y0u_g3t_n3w_l3ss0n}