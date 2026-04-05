from pwn import xor

class ABC:
    def __init__(self, key):
        self.vals = [i for i in key]
        
    def turn(self):
        self.vals = [self.vals[-1]] + self.vals[:-1]
        
    def decrypt(self, msg):
        keystream = []
        while len(keystream) < len(msg):
            keystream += self.vals
            self.turn()
        return bytes([msg[i] ^ keystream[i] for i in range(len(msg))])

enc = bytes.fromhex('6beb1545ebee14c4770d0eba1794747506ee1490c4700ceb4643c4740aeebb109127065bf5')

format_flag = b'LKS{'    
partial_key = xor(enc[:len(format_flag)], format_flag)

for i in range(256):
    guess = bytes([i])
    key = partial_key + guess
    decryptor = ABC(key)
    decrypt = decryptor.decrypt(enc)
    # print(f'{decrypt = }')
    if decrypt.startswith(b'LKS{') and decrypt.endswith(b'}'):
        flag = decrypt.decode()
        print(flag)
        break
    
# LKS{cf3d130204238f30d62cadd24f371a8e}