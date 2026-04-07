# 🧩 Challenge

## 📌 Basic Info
- **Name**: xor
- **Platform**: TCP1P
- **Category**: Cryptography
- **Difficulty**: -
- **Points**: 154 (when solved)

---

## 📖 Description
XOR adalah operator bitwise yang mengembalikan 0 jika bitnya sama, dan 1 jika bitnya sama.

Hints
Jangan terpatok sama randomnya
Coba bruteforce buat nemuin prefix flagnya

---

## 🔗 Resources
- Link: https://tcp.1pc.tf/games/11/challenges#293-xor
- File: https://tcp.1pc.tf/assets/e50196516a71df12673694c2201a83ef64dc37b29aa4ad0c7cdbf5d9f9b9d8b3/s/CfDJ8FxOmXurdyBOsTXykQypL8XfZWDvQNJZ0sU_xlIYi5p7Ew0uqj-Yk2_ZAXHrk0-itdZVGtZMx2qVBhwg5gh3Ncp9ZTNKtnFEz0ecAggPx5fIRhgPz03sr5fxEjR4WA9TIlsIc903E-XlxYIZoqG6EWZ5_3bVRdagzcMPuFcQCd9-dPOw-WfX7Ur5tHTP2OWtjVqFE0o-s8cxKEQRXBbp_ftosowClkE6LR79x5f-zm4k9EacOdGcyeqZBBG6IrCbvwYAjAOCCbdbU8rtU_8UXkI/xor_chall.py ( [xor_chall.py](xor_chall.py) )

---

## 🎯 Objective
- Decrypt the given ciphertext to retrieve the flag.

---

# 🧠 Solution

## 🔍 Analysis
Simple xor, the key for xor can be retrieved by xoring the other 2 keys.

---

## 🛠️ Approach
1. Get the key by xoring `key_1` and `key_xor`.
2. Decrypt the cipher by xoring it with the retrieved key.

---

## 💻 Exploit / Code
[debug.py](debug.py)
[solver.py](solver.py)

---

## 🚩 Flag
TCP1P{To_s0lv3_1t_juSt_us3_l0g1C_agalN}

---

## 📚 Lessons Learned
- XOR is a simple but effective encryption method when used with a secure key.

---

## 🧷 Notes
- XOR operations are their own inverse, making them useful for both encryption and decryption.