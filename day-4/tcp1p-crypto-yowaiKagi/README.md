# 🧩 Challenge

## 📌 Basic Info
- **Name**: Yowai Kagi
- **Platform**: TCP1P
- **Category**: Cryptography
- **Difficulty**: -
- **Points**: 181 (when solved)

---

## 📖 Description
Terinspirasi dari Compfest 15 Hackerclass ;)

---

## 🔗 Resources
- Link: https://tcp.1pc.tf/games/11/challenges#305-Yowai-Kagi
- File: https://tcp.1pc.tf/assets/2ed3677c9ff863e96db306085eec849e91ad622e061645e33894de01261200e3/s/CfDJ8FxOmXurdyBOsTXykQypL8V_dTLJpaer4CGuU6pjQI7oD9fnLmjAPzDVaMAtq4Gjb7N1kaKAOtBpVNv30sk-FYlC_XCjjIatcgDjU7jF-_lEY67TM_y_dZ0xoR_AMBNi_rgszTuXgIyAMy5xaXDQ_bMGlXIjH9pYgCFBD_g5SEuHBKkSDuQFaEP5HX8yM9x3-sJQPx5lNccwYyJtPw0e_gjkcgBpOCXw6Wbv_pkWeGgk9RNMs_0gDAaL2BlQmBnjIMXX9twr-eOiifZuVs__trs/yowaikagi_yowaikagi-dist.zip ( [chall.py](chall.py), [chall.py](chall.py) )

---

## 🎯 Objective
- Decrypt the given ciphertext to retrieve the flag from a broken RSA scheme.

---

# 🧠 Solution

## 🔍 Analysis
Analyzing the provided code, we notice that the encryption only use one prime for the modulus `n`, this means we can easily calculate `phi(n)` and then calculate the private key `d` to decrypt the ciphertext.

---

## 🛠️ Approach
1. Extract the ciphertext and modulus from the provided data.
2. Calculate `phi(n)` using the fact that `n` is a product of a single prime.
3. Calculate the private key `d` using the modular inverse of `e` and `phi(n)`.
4. Decrypt the ciphertext using the private key `d` to retrieve the original message (flag).

---

## 💻 Exploit / Code
[debug.py](debug.py)
[solver.py](solver.py)

---

## 🚩 Flag
TCP1P{th4tS_k3y_1s_t00_We4K}

---

## 📚 Lessons Learned
- Understanding the importance of using two distinct primes in RSA to ensure security.

---

## 🧷 Notes
- Always check the structure of the RSA modulus to identify potential weaknesses.