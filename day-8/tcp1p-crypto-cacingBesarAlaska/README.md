# 🧩 Challenge

## 📌 Basic Info
- **Name**: Cacing Besar Alaska
- **Platform**: TCP1P
- **Category**: Cryptography
- **Difficulty**: -
- **Points**: 124 (when solved)

---

## 📖 Description
Dalam tabel Ascii berisi banyak kumpulan kode untuk mewakili setiap karater, salah satunya adalah Desimal

https://youtu.be/mk_to8HT5Qo?si=lTa3WHDmBcy-bQZJ

chall : [84, 67, 80, 49, 80, 123, 99, 52, 99, 105, 78, 54, 95, 66, 51, 115, 97, 82, 95, 97, 108, 97, 83, 107, 52, 95, 109, 101, 82, 117, 115, 52, 75, 66, 105, 107, 49, 110, 95, 98, 48, 116, 116, 111, 77, 125]

Hints
Tabel Ascii
Bentuk Decimal

---

## 🔗 Resources
- Link: https://tcp.1pc.tf/games/11/challenges#295-Cacing-Besar-Alaska
- File: -

---

## 🎯 Objective
- Decode the given decimal values using the ASCII table to retrieve the flag.

---

# 🧠 Solution

## 🔍 Analysis
The given challenge provides a list of decimal values that represent ASCII codes. To solve the challenge, we need to convert each decimal value into its corresponding ASCII character and concatenate them to form the flag.

---

## 🛠️ Approach
1. Take the list of decimal values.
2. Convert each decimal value to its corresponding ASCII character using the ASCII table.

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
TCP1P{c4ciN6_B3saR_alaSk4_meRus4KBik1n_b0ttoM}

---

## 📚 Lessons Learned
- Understanding how to convert decimal values to ASCII characters is crucial in solving certain types of cryptography challenges. This challenge reinforces the importance of being familiar with the ASCII table and how to use it effectively in CTF competitions.

---

## 🧷 Notes
- This challenge is a straightforward application of ASCII conversion, which is a fundamental skill in cryptography and CTF challenges. It serves as a good practice for beginners to get comfortable with basic encoding and decoding techniques.