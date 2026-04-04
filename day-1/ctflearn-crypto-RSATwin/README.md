# 🧩 Challenge

## 📌 Basic Info
- **Name**: RSA Twins!
- **Platform**: ctflearn
- **Category**: Cryptography
- **Difficulty**: Hard
- **Points**: 90

---

## 📖 Description
https://mega.nz/#!2aBwFCKa!NWQKRIbYzSAU2iwCPNppO7SE92W6sne4FKD3sKE2A-k Aww, twins :). Theyâre so cute! They must be (almost) identical because theyâre the same except for the slightest difference. Anyway, see if you can find my flag. Hint: This is just math. You're probably not going to find any sort of specialized attack.

---

## 🔗 Resources
- Link: https://ctflearn.com/challenge/484  
- File: https://mega.nz/file/2aBwFCKa#NWQKRIbYzSAU2iwCPNppO7SE92W6sne4FKD3sKE2A-k

---

## 🎯 Objective
- Retrieve the flag from the given ciphertext and public key.

---

# 🧠 Solution

## 🔍 Analysis
From the challenge description, we can assume that the RSA modulus has two prime factors that are very close to each other, which is why the challenge is called "RSA Twins". 

To solve 2 almost identical primes, we can use fermat's factorization method, which is based on the difference of squares.

OR, for a challenge where we only got the public key and the ciphertext, we can also try to find the private key by calculating the totient of n, use the `totient` function from the `sympy` library to retrieve the value of phi, and then calculate the private exponent d.

---

## 🛠️ Approach
1. Use Fermat's factorization method to factor the RSA modulus (n) into its two prime factors (p and q). Source: https://github.com/d4rkvaibhav/Fermat-Factorization/blob/master/fermat.py
2. Calculate the private exponent (d).
3. Decrypt the ciphertext (c) using the private exponent (d) and the RSA decryption formula.

OR

1. Calculate the totient of n using the `totient` function from the `sympy` library.
2. Calculate the private exponent (d) using the modular inverse function.
3. Decrypt the ciphertext (c) using the private exponent (d) and the RSA decryption formula.

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
flag{i_l0v3_tw1N_pr1m3s}

---

## 📚 Lessons Learned
- Fermat's factorization method can be effective for factoring RSA moduli that are products of two close primes.
- The security of RSA can be compromised if the prime factors of the modulus are too close to each other, as it allows for efficient factorization using Fermat's method.

---

## 🧷 Notes
- Always ensure that the prime factors of the RSA modulus are not too close to each other, as this can lead to vulnerabilities that can be exploited using Fermat's factorization method.