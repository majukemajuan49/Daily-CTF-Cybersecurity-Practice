# 🧩 Challenge

## 📌 Basic Info
- **Name**: Geprek
- **Platform**: TCP1P
- **Category**: Cryptography
- **Difficulty**: -
- **Points**: 221 (when solved)

---

## 📖 Description
Implementasi lanjutan tentang gerbang logika xor.

Coba baca-baca cara xor bekerja dan implementasikan untuk dapat flag di sistem ini.

Jangan lupa connect dengan netcat.

Connection: nc gzcli.1pc.tf (no value)

Start challenge from: https://gzcli.1pc.tf/tcp1p-special-ramadhan-2024-archive-crypto-geprek

---

## 🔗 Resources
- Link: https://tcp.1pc.tf/games/11/challenges#291-Geprek
- File: https://tcp.1pc.tf/assets/d1874d299c15c3b625d17683b4695a926f5e96987802cdc0ecdb91309d999367/s/CfDJ8FxOmXurdyBOsTXykQypL8WdMVVOo93hcoGkN7hU8S458qDLJTA9hozmVCeQNpm1h8jw7eijYo2JLVIYYilGHBpIBDClcbVQKdGt29on-GZrnNBdc2UsBb36OqhvPDWke7Hr-oJ1PqQ5HUyRjGKF-OZoG2_jdLNVUWuehGkN55XlD_dohYq_dMvVn1eKy4aflHYf32N2VaeXU5hZWtcUIhuuhlb5MnTvnEKJY5yqG8BGEmAIMkvhfkX4kUEt0Vf3BigKN-QEQsxbX0wv_iH5Afk/geprek_ayam_geprek.py ( [geprek_ayam_geprek.py](geprek_ayam_geprek.py) )

---

## 🎯 Objective
- Retrieve the key to xor the encrypted flag and get the flag.

---

# 🧠 Solution

## 🔍 Analysis
We can use the function `encrypt` as an oracle to retrieve the key by sending a plaintext of 16 null bytes (0x00). The output will be the key itself since XORing with 0x00 does not change the value. After obtaining the key, we can XOR it with the encrypted flag to retrieve the original flag.

---

## 🛠️ Approach
1. Input 16 null bytes to the `encrypt` function to get the key.
2. Get the encrypted flag from the server.
3. XOR the encrypted flag with the retrieved key to get the original flag.

---

## 💻 Exploit / Code
[debug_server.py](debug_server.py)
[solver.py](solver.py)

---

## 🚩 Flag
TCP1P{dil4rang_m4kan_4yaM_g3prEk_di_s1ang_hAri_s3lamA_ramadhann}

---

## 📚 Lessons Learned
- Understanding how XOR works and how to use it as an oracle to retrieve keys in cryptographic challenges.
- The importance of analyzing the provided code and functions to find vulnerabilities or ways to retrieve necessary information for solving the challenge.

---

## 🧷 Notes
- Always analyze the provided code and functions carefully to find potential vulnerabilities or ways to retrieve necessary information.
- In cryptographic challenges, understanding the underlying principles of the algorithms used can be crucial in finding a solution.