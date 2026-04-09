# 🧩 Challenge

## 📌 Basic Info
- **Name**: Hash 2: One-Way Function
- **Platform**: TCP1P
- **Category**: Cryptography
- **Difficulty**: -
- **Points**: 248 (when solved)

---

## 📖 Description
Aku baru saja membuat sebuah aplikasi yang akan memberikan flag pada user selama user itu telah terdaftar dalam sistem. Di sini aku berikan saja database username dan password mereka hehe. Selama sudah di-hash, password mereka akan aman... kan?

Connection: nc gzcli.1pc.tf (no value)

Start challenge from: https://gzcli.1pc.tf/tcp1p-special-ramadhan-2024-archive-crypto-hash-3-collision

---

## 🔗 Resources
- Link: https://tcp.1pc.tf/games/11/challenges#316-Hash-3%3A-Collision
- File: https://tcp.1pc.tf/assets/b97d66950bdacc6c03ad10defb6bbcb36570a0dac21b95099862c8c34e05fb08/s/CfDJ8FxOmXurdyBOsTXykQypL8XqwQ9vipHQKpGOn-Fma4GOyUKEKMD0L6qOs2Wf-v77jH3mllAdJdG8bo70K6EwmiObA8ypiNZqTKyZT23Bk62DrcR9cMSZ5uh5O9Tmavu9HdIBT3sRWRBBsQszhj67fKKjERf7C19XgUk3LKfyGCoQii1v_CG1twZwCn_3f7jEFR_7nf4dA46z63LK1IFjjvLS2PwVjSyadxuG3B40wtyaLuExAAW20yhYIiAP3miEf8oZLbt6HZaTR5axPUk7bhQ/hash3collision_server.py ( [hash3collision_server.py](hash3collision_server.py) )

---

## 🎯 Objective
- Construct a password that produces the same hash value as the target hash value, demonstrating a collision in the hashing algorithm used by the application.

---

# 🧠 Solution

## 🔍 Analysis
Since the hashing algorithm is too simple, which it just sums the ASCII values of the characters in the password, we can easily create a collision by finding different combinations of characters that yield the same sum. The target hash value is given, and we can use this information to construct a password that produces the same hash value. For example, I targeted the `user2` account, which has a hash value of 1343. To create a collision, I can use 14 'Z' characters (which have an ASCII value of 90) and one additional character to make the total sum equal to 1343.

---

## 🛠️ Approach
1. Calculate the target hash value for the `user2` account, which is 1343.
2. Determine how many 'Z' characters (ASCII value 90) can be used without exceeding the target hash value. In this case, 14 'Z' characters will contribute 1260 to the hash value.
3. Calculate the remaining value needed to reach the target hash value (1343 - 1260 = 83).
4. Find a character with an ASCII value of 83, which is 'S'.
5. Construct the password using 14 'Z' characters followed by 'S', resulting in a password that produces the same hash value of 1343.

---

## 💻 Exploit / Code
[debug_server.py](debug_server.py)
[solver.py](solver.py)

---

## 🚩 Flag
TCP1P{pl34s3_c0ns1d3r_c0ll1s10ns_wh3n_cr34t1ng_h4sh_funct10ns}

---

## 📚 Lessons Learned
- Understanding the concept of hash collisions and their implications in cryptography.
- Recognizing the importance of using strong hashing algorithms that are resistant to collisions to ensure data integrity and security.

---

## 🧷 Notes
- Always consider the possibility of hash collisions when designing hashing algorithms, as they can lead to security vulnerabilities if not properly addressed.