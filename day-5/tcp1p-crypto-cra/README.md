# 🧩 Challenge

## 📌 Basic Info
- **Name**: CRA
- **Platform**: TCP1P
- **Category**: Cryptography
- **Difficulty**: -
- **Points**: 166 (when solved)

---

## 📖 Description
Sayuri telah terpesona oleh geometri sejak usia muda, dan obsesinya yang terbesar adalah dengan kubus. Sementara anak-anak lain bermain dengan mainan atau berlarian di ladang, Sayuri sering ditemukan menggambar desain kubus yang rumit di buku catatannya atau membuat struktur berbentuk kubus dari berbagai bahan yang ia temukan.

Suatu hari Sayuri ingin mengirimkan pesan kepada temannya dengan penggunakan metode RSA, tetapi Sayuri yang masih belajar RSA tidak mengetahui bahwa algoritma yang dia gunakan dapat mudah diserang.

---

## 🔗 Resources
- Link: https://tcp.1pc.tf/games/11/challenges#290-CRA
- File: https://tcp.1pc.tf/assets/2ad94f52c2dfe5f091d497e66312d0dbb502ce763d77f3e6cc886a144a29b049/s/CfDJ8FxOmXurdyBOsTXykQypL8UukVvTTFZRBdwZahvb_ZQdvgE_E5MdkEBo38wY0wwJSuzch8lov8DxBbUWsIVRkQRQzTD303uwfRakZmTnV0oldBYNADj4DpAFFSlgZzTsiXi8TTIdoOtqbtS4NtU_ZQIcmy0_TlqHd3hY4kGxGtzDBeBNentIqJUu7SQaAeshfBkqIYlZNgvP1x-yeYccQYyEsVvec-qJzQiMusZccGySp3O0An-J4X8tAzzragOFXHJn8VskpBrIpbi-iqS2_xQ/cra_cra-dist.zip ( [chall.py](chall.py), [output.txt](output.txt) )

---

## 🎯 Objective
- Decrypt the given ciphertext to retrieve the flag from a nerfed RSA scheme.

---

# 🧠 Solution

## 🔍 Analysis
The public exponent is 3, which is too small that makes the m^e is smaller than n. For example
```
2**3 % 11 
= 8 % 11
= 8
```
We can see that the ciphertext is just the plaintext raised to the power of 3, without any modular reduction. Thus we can easily retrieve the plaintext by calculating the integer cube root of the ciphertext.

---

## 🛠️ Approach
1. Calculate the integer cube root of the given ciphertext to retrieve the plaintext.

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
TCP1P{YoU_c4n_us3_th1S_MetH0d_1F_the_3xponeNt_Is_3}

---

## 📚 Lessons Learned
- Understanding the risks of using small public exponents in RSA encryption.

---

## 🧷 Notes
- This challenge highlights the importance of choosing appropriate parameters in cryptographic schemes to ensure security.