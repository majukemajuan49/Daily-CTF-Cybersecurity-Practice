#!/usr/bin/env python3
import secrets

FLAG = b'LKS{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}'

class ABC:
    def __init__(self, key):
        self.vals = [i for i in key]
        
    def turn(self):
        self.vals = [self.vals[-1]] + self.vals[:-1]
        
    def encrypt(self, msg):
        keystream = []
        while len(keystream) < len(msg):
            keystream += self.vals
            self.turn()
        return bytes([msg[i] ^ keystream[i] for i in range(len(msg))]).hex()

print(ABC(secrets.token_bytes(5)).encrypt(FLAG))

'''
6beb1545ebee14c4770d0eba1794747506ee1490c4700ceb4643c4740aeebb109127065bf5
'''