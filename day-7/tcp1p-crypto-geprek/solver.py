from pwn import *

conn = remote("gzcli.1pc.tf", 36110)

retrieve_key_payload = (b'\x00'*16).hex()

conn.recvuntil(b"Input: ")
conn.sendline(b"2")
conn.recvuntil(b"input pesan kamu dalam bentuk hex: ")
conn.sendline(retrieve_key_payload.encode())
conn.recvuntil(b"Hasil= ")
key = bytes.fromhex(conn.recvline().strip().decode())

conn.recvuntil(b"Input: ")
conn.sendline(b"1")
enc_flag = bytes.fromhex(conn.recvline().strip().decode())

flag = xor(enc_flag, key).decode()
print(flag)

# TCP1P{dil4rang_m4kan_4yaM_g3prEk_di_s1ang_hAri_s3lamA_ramadhann}