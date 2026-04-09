# 🧩 Challenge

## 📌 Basic Info
- **Name**: Hash 2: One-Way Function
- **Platform**: TCP1P
- **Category**: Cryptography
- **Difficulty**: -
- **Points**: 221 (when solved)

---

## 📖 Description
Untuk challenge ini aku telah membuat banyak flag tapi bingung mau pilih yang mana. Yasudahlah, aku pilih random saja~. Dari value hash yang diberikan, bisakah kamu mengetahui flag mana yang kupilih??

---

## 🔗 Resources
- Link: https://tcp.1pc.tf/games/11/challenges#294-Hash-2%3A-One-Way-Function
- File: https://tcp.1pc.tf/assets/9088089693efbe6a999eaecb00dff9bae57023a139df5f4a70f19e60840fd3ef/s/CfDJ8FxOmXurdyBOsTXykQypL8WHWym1fY7QNMW5KIU4hxtxxcSxl-GNKQuHRbXGS6ZhPHLhLRHjGEFAFp9AMNDeGGa8MPkMMq2LY2LHWZq-i6NIFLUupcoLWS9Jp--6kSpDQjj53aIEKFL5tadDAB3-hikfkdKh-KS1lwbZxmwstG6SbGfszkMaqfFZgr1Z2i4kxiDKgJdQaqst88wtuIsytClG74ZJxCgPPHTUQlFZg0NPLYDYfRkJBLv4H7aO8SjIha4YuJX2bTOzeRIXKt0eZJo/hash2one-wayfunction_hash2one-wayfunction-dist.zip ( [chall.py](chall.py), [flags.txt](flags.txt) )

---

## 🎯 Objective
- Find the flag that corresponds to the given hash value.

---

# 🧠 Solution

## 🔍 Analysis
Since hash is a one-way function, it is computationally infeasible to reverse the hash value to find the original input (flag). Therefore, the most straightforward approach is to compute the hash values for all the flags in `flags.txt` and compare them with the given hash value to find a match.

---

## 🛠️ Approach
1. Try to hash each flag from `flags.txt` using the same hashing algorithm that was used to generate the given hash value.
2. Compare the computed hash values with the given hash value.
3. If a match is found, the corresponding flag is the correct one.

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
TCP1P{th3r3_1s_n0_w4y_b4ck}

---

## 📚 Lessons Learned
- Understanding the concept of one-way functions and their properties in cryptography.
- Familiarity with hashing algorithms and their applications in security.

---

## 🧷 Notes
- The challenge emphasizes the importance of one-way functions in cryptography, which are designed to be easy to compute in one direction but difficult to reverse. This is a fundamental concept in ensuring data integrity and security.