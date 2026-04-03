p = 11
q = 17
e = 3
n = p * q
c = 103

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

m = pow(c, d, n)
print(m)

# 137