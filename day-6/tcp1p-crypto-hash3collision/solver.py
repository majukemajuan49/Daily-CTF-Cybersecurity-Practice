from pwn import *

conn = remote("gzcli.1pc.tf", 51315)

target_hash_value = int(bytes.fromhex("31333433").decode()) # 1343

chr90_count = target_hash_value // 90

password = (chr(90) * chr90_count) + chr(target_hash_value % 90)

conn.recvuntil(b">> ")
conn.sendline(b"1")

conn.recvuntil(b"Username: ")
conn.sendline(b"user2")
conn.recvuntil(b"Password: ")
conn.sendline(password.encode())

conn.recvuntil(b">> ")
conn.sendline(b"1")

conn.recvuntil(b"Here is your flag: ")
flag = conn.recvline().decode().strip()
print(flag)

# TCP1P{pl34s3_c0ns1d3r_c0ll1s10ns_wh3n_cr34t1ng_h4sh_funct10ns}