import mpmath as mp
mp.mp.prec = 2000

FLAG = b"XMAS{yes_yesyes_yesyes_yes}"
print(f'{len(FLAG) = }')
multiply = -len(FLAG) % 12
print(f'{multiply = }')
FLAG += b"X" * (multiply)
print(f'{FLAG = }')

# panjang flag kelipatan 12, dengan padding X

secrets = [int.from_bytes(FLAG[i:i+12]) for i in range(0, len(FLAG), 12)]
print(f'{secrets = }')
def transform(x):
    a = mp.mpf(x)
    print(f"{a = }")
    a = a.sqrt()
    print(f"{a = }")
    return str(a).split('.')[-1]

print(f'{transform(secrets[0]) = }')
print(f'{len(transform(secrets[0])) = }')


ct = list(map(lambda x : str(mp.mpf(x).sqrt()).split('.')[-1], secrets))
print(f'{ct = }')
print(f'{len(ct) = }')


    

# print(list(map(lambda x : str(mp.mpf(x).sqrt()).split('.')[-1], secrets)))
