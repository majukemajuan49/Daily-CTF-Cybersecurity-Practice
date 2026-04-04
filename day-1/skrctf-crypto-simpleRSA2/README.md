# 🧩 Challenge

## 📌 Basic Info
- **Name**: Simple RSA 2
- **Platform**: skrctf
- **Category**: Cryptography
- **Difficulty**: Easy
- **Points**: 20

---

## 📖 Description
Using the same e and n from the previous challenge calculate the message m which cipher text c = 103

Flag format: Decimal number

---

## 🔗 Resources
- Link: https://skrctf.me/challenges#Simple%20RSA%202
- File: -

---

## 🎯 Objective
- Decrypt the message (m) using the given cipher text (c) and the RSA parameters.

---

# 🧠 Solution

## 🔍 Analysis
The challenge provides us with the values of p, q, e, and c. We are asked to calculate the message (m) using these values.

---

## 🛠️ Approach
1. Calculate n = p * q.
2. Calculate the private key (d) using the Extended Euclidean Algorithm.
3. Calculate the message (m) using the formula: m = c^d mod n.

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
137

---

## 📚 Lessons Learned
- Understanding the RSA encryption process and how to calculate the cipher text using the public key components.
- The importance of the private key in decrypting messages encrypted with RSA.

---

## 🧷 Notes
- The private key d can be calculated using the Extended Euclidean Algorithm, which is essential for decrypting messages in RSA.