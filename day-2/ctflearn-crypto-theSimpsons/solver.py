from pwn import xor

# Ahh! Realistically the Simpsons would use octal instead of decimal!
# encoded = 152 162 152 145 162 167 150 172 153 162 145 170 141 162
# key = chr(SolutionToDis(110 157 167 040 155 165 143 150 040 144 151 144 040 115 141 147 147 151 145 040 157 162 151 147 151 156 141 154 154 171 040 143 157 163 164 077 040 050 104 151 166 151 144 145 144 040 142 171 040 070 054 040 164 157 040 164 150 145 040 156 145 141 162 145 163 164 040 151 156 164 145 147 145 162 054 040 141 156 144 040 164 150 145 156 040 160 154 165 163 040 146 157 165 162 051))
# key = key + key + chr(ord(key)-4)
# print(DecodeDat(key=key,text=encoded))

def fromOctal(octal_str):
    return chr(int(octal_str, 8))

encoded_str = "152 162 152 145 162 167 150 172 153 162 145 170 141 162"
encoded = encoded_str.split(" ")
key_str = "110 157 167 040 155 165 143 150 040 144 151 144 040 115 141 147 147 151 145 040 157 162 151 147 151 156 141 154 154 171 040 143 157 163 164 077 040 050 104 151 166 151 144 145 144 040 142 171 040 070 054 040 164 157 040 164 150 145 040 156 145 141 162 145 163 164 040 151 156 164 145 147 145 162 054 040 141 156 144 040 164 150 145 156 040 160 154 165 163 040 146 157 165 162 051"
key = key_str.split(" ")

dec_encoded = "".join([fromOctal(o) for o in encoded])
print(dec_encoded)
# jrjerwhzkrexar

dec_key = "".join([fromOctal(o) for o in key])
print(dec_key)
# How much did Maggie originally cost? (Divided by 8, to the nearest integer, and then plus four)
# 847.63 => 847.63 / 8 = 105.95375 => 106 + 4 = 110

key = chr(110)
key = key + key + chr(ord(key) - 4)
print(key)

# a little guessy, but it turns out to be vignere cipher to decrypt the dec_encoded using the key
def vignere_decrypt(ciphertext, key):
    decrypted = []
    key_length = len(key)
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():  # Only decrypt alphabetic characters
            shift = ord(key[i % key_length]) - ord('a')
            decrypted_char = chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)  # Non-alphabetic characters are not changed
    
    return ''.join(decrypted)

decrypted_message = f"CTFlearn{{{vignere_decrypt(dec_encoded, key)}}}"
print(decrypted_message)

# CTFlearn{wearenumberone}