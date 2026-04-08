flags = open("flags.txt", "r").read().splitlines()
target_hash = "32333934"

def my_hash(string):
	sum = 0
	for char in string:
		sum += ord(char)
	sum = sum % 2**24
	return str(sum).encode().hex()

for flag in flags:
    hash_val = my_hash(flag)
    if hash_val == target_hash:
        print(flag)
        break
    
# TCP1P{th3r3_1s_n0_w4y_b4ck}