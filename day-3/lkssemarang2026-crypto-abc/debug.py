#!/usr/bin/env python3
import secrets
from pwn import xor

FLAG = b'LKS{testing_flag}'

class ABC:
    def __init__(self, key):
        self.vals = [i for i in key]
        
    def turn(self):
        self.vals = [self.vals[-1]] + self.vals[:-1]
        
    def encrypt(self, msg):
        keystream = []
        while len(keystream) < len(msg):
            print(f'{self.vals = }')
            keystream += self.vals
            self.turn()
        print(f'{keystream = }')
        return bytes([msg[i] ^ keystream[i] for i in range(len(msg))]).hex()

key = secrets.token_bytes(5)
print(f'{key = }')
ct = ABC(key).encrypt(FLAG)
print(f'{ct = }')

print(xor(b'LKS{', bytes.fromhex(ct)[:len(b'LKS{')]) == key[:len(b'LKS{')])