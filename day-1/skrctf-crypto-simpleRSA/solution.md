# 🧠 Solution

## 🔍 Analysis
The challenge provides us with the values of p, q, e, and m. We are asked to calculate the cipher text (c) using these values.

---

## 🛠️ Approach
1. Calculate n = p * q.
2. Calculate the cipher text (c) using the formula: c = m^e mod n.

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
SKR{77}


---

## 📚 Lessons Learned
- Understanding the RSA encryption process and how to calculate the cipher text using the public key components.

---

## 🧷 Notes
- The private key d can be calculated using the Extended Euclidean Algorithm, but since the challenge only asks for the cipher text, we focused on that part.