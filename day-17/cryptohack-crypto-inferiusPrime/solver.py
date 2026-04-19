from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

n = 984994081290620368062168960884976209711107645166770780785733
e = 65537
ct = 948553474947320504624302879933619818331484350431616834086273

# factordb
p = 848445505077945374527983649411
q = 1160939713152385063689030212503

assert p*q == n

phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(ct, d, n)
flag = long_to_bytes(m).decode()

print(flag)
# crypto{N33d_b1g_pR1m35}