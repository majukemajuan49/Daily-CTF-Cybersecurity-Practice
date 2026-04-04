# 🧩 Challenge

## 📌 Basic Info
- **Name**: RSA Noob
- **Platform**: ctflearn
- **Category**: Cryptography
- **Difficulty**: Medium
- **Points**: 60

---

## 📖 Description
These numbers were scratched out on a prison wall. Can you help me decode them? https://mega.nz/#!al8iDSYB!s5olEDK5zZmYdx1LZU8s4CmYqnynvU_aOUvdQojJPJQ

e: 1

c: 9327565722767258308650643213344542404592011161659991421

n: 245841236512478852752909734912575581815967630033049838269083

---

## 🔗 Resources
- Link: https://ctflearn.com/challenge/120  
- File: https://mega.nz/#!al8iDSYB!s5olEDK5zZmYdx1LZU8s4CmYqnynvU_aOUvdQojJPJQ

---

## 🎯 Objective
- Retrieve the flag from the given ciphertext and public key.

---

# 🧠 Solution

## 🔍 Analysis
The challenge provides us with the values of p, q, e, and m. We are asked to calculate the cipher text (c) using these values. Since e is 1, the encryption process simplifies significantly. The cipher text can be calculated as c = m^e mod n, which in this case becomes c = m mod n.

Because m is less than n, the result of m mod n is simply m itself. Therefore, the cipher text (c) is equal to the plaintext message (m).

---

## 🛠️ Approach
1. Decode the given ciphertext (c) rigth away since e is 1.

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
abctf{b3tter_up_y0ur_e}

---

## 📚 Lessons Learned
- Understanding the RSA encryption process and how the choice of e can affect the security of the encryption. In this case, using e = 1 is a critical mistake that leads to an easily recoverable plaintext.

---

## 🧷 Notes
- Always ensure that the public exponent e is chosen appropriately (commonly 65537) to avoid vulnerabilities in RSA encryption.