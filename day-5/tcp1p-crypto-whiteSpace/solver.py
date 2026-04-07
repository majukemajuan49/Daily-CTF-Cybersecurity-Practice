enc = open("output.txt", "r").read()
blocks = enc.split("\n")

# flag format
# TCP1P{}

# even index to retrieve key_1
char1 = ord('T') # 84
key_1 = len(blocks[0]) // char1

# odd index to retrieve key_2
char2 = ord('C') # 67
key_2 = len(blocks[1]) // char2

flag = ''
for i, block in enumerate(blocks):
    if i % 2 == 0:
        flag += chr(len(block) // key_1)
    else:
        flag += chr(len(block) // key_2)
        
print(flag)

# TCP1P{I_h4Ve_TrIed_noT_t0_Be_se3n}