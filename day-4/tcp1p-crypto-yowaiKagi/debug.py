from Crypto.Util.number import *

flag = b"TCP1P{testing_flag}"

def source(flag):
    e = 65537
    n = getStrongPrime(1024)
    m = bytes_to_long(flag)
    return [e, n, m]

def enc(source):
    e, n, m = source
    if(pow(m, e) > n):
        cp = pow(m, e, n)
        cp = long_to_bytes(cp)
        return [cp, n]

def write(data):
    cp, n = data
    print(f"Ciphertext: {cp.hex()}")
    print(f"Modulus: {n}")

sourceProc = source(flag)
encProc = enc(sourceProc)
write(encProc)