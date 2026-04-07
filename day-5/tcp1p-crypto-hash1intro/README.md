# 🧩 Challenge

## 📌 Basic Info
- **Name**: Hash 1: intro
- **Platform**: TCP1P
- **Category**: Cryptography
- **Difficulty**: -
- **Points**: 199 (when solved)

---

## 📖 Description
Hashing adalah sebuah metode untuk mengubah data menjadi sebuah string yang panjangnya tetap. Algoritma hash merupakan fungsi satu arah, artinya apabila diberikan hasil hash dari suatu data, akan sangat sulit untuk menerka data aslinya. Oleh karena itu, biasanya password disimpan di database dalam bentuk hash.

Meskipun begitu, untuk beberapa value hash, kita bisa mengetahui data aslinya menggunakan tool yang tersedia online. Untuk soal ini, cobalah "crack" beberapa value hash MD5 pada hashes.txt.

---

## 🔗 Resources
- Link: https://tcp.1pc.tf/games/11/challenges#308-Hash-1%3A-intro
- File: https://tcp.1pc.tf/assets/e2cbc3b2a616674e41e8b9903623ca7bdc50bc438b047beb75a995ba9da88bb8/s/CfDJ8FxOmXurdyBOsTXykQypL8W0OOjeiVY7rk21mVB_DZZ_NWFNatZQFJIqr87SUKDgc9slxhlSvUNQuK7BXneZxlQK_wi065uTck34zPfjan8Zvp3QGAEEyfxbVW0T_J8jpzMBTfVnGVM9QSloJ-z7wksTRU_mZoV-tF8M__q8aMDqQhxp4op9DkVySS280NYc_UpB4YPNYY_7Jdu4uIT7eqXluUlzg-3gfu6-t_G3LwYMkqGsm4oINothib37q8pzXtZiWllPg2Mmf-vmzYz-oqI/hash1intro_hashes.txt ( [hash1intro_hashes.txt](hash1intro_hashes.txt) )

---

## 🎯 Objective
- Crack the provided MD5 hashes to find the corresponding plaintext values.

---

# 🧠 Solution

## 🔍 Analysis
Some md5 values ca be cracked using online tools, but some of them are not. We can use an online tool called https://crackstation.net/.

---

## 🛠️ Approach
1. Copy the provided MD5 hashes from `hash1intro_hashes.txt`.
2. Paste the hashes into the input field on https://crackstation.net/.

---

## 💻 Exploit / Code
[solving.txt](solving.txt)

---

## 🚩 Flag
TCP1P{d0nt_us3_sh0rt_p4ssw0rds}

---

## 📚 Lessons Learned
- For some hashes, especially those generated from short or common passwords, it is possible to find the original plaintext using online hash cracking tools. This highlights the importance of using strong, unique passwords that are not easily guessable or found in common password lists.

---

## 🧷 Notes
- Always use strong, unique passwords to protect your accounts and data. Avoid using common words or short passwords that can be easily cracked using hash cracking tools.