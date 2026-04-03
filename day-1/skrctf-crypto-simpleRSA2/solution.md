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