import os
from Crypto.Util.number import bytes_to_long, getRandomNBitInteger, isPrime, getPrime
from math import gcd

def nextPrime(n):
    print(f'initial n: {n}')
    while not isPrime(n := n + 1):
        # print('Hit!')
        continue
    print(f'nextPrime result: {n}')
    return n

def gen():
    attempts = 0
    max_attempts = 1000
    while attempts < max_attempts:
        q = getPrime(128)
        r = getRandomNBitInteger(128)
        p = q * nextPrime(r) + nextPrime(q) * r
        if p.bit_length() <= 256 and isPrime(p) and isPrime(q):
            return p, q, r
        attempts += 1
        
        # n = p * q
        # p = q * nextPrime(r) + nextPrime(q) * r
        # n = q * (q * nextPrime(r) + nextPrime(q) * r)
        # n = (q * q * nextPrime(r)) + (q * nextPrime(q) * r)

    raise ValueError("Failed to generate primes within attempts")

# r = 272617646727976431124665621907966000454
# print(f'{nextPrime(r) = }')

# n=18307564183336174372957570419285112053386287578636115613810768749885553622091399241390778725602944089106231437595887

# a = n // (nextPrime(r) * r)
# print(f'{a = }')

# q = gcd(n, a)
# p = n // q

# assert p*q == n

# print(f'{p = }')
# print(f'{q = }')

# flag = b"TCP1P{testing}"
# m = bytes_to_long(flag)
p, q, r = gen()
print(f'{p - q = }')
# n = p * q
# phi = (p - 1) * (q - 1)
# e = 0x10001
# d = pow(e, -1, phi)
# c = pow(m, e, n)
# print(f"{n=}")
# print(f"{e=}")
# print(f"{c=}")
# print(f"{r=}")
