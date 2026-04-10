# 🧩 Challenge

## 📌 Basic Info
- **Name**: OTP
- **Platform**: TCP1P
- **Category**: Cryptography
- **Difficulty**: -
- **Points**: 181 (when solved)

---

## 📖 Description
Ketika ngopi di cafe saya iseng untuk melakukan capture sebuah jaringan wifi. Secara tidak sengaja saya mendapatkan 3 pesan yang terenkripsi, saya coba analisa dan ternyata bisa didapatkan pesan kedua yaitu "dengan menyelesaikan tantangan keamanan dalam tim atau individu". Setiap kali pesan itu dikirim selalu saja ada sebuah keterangan panjang key 32, saya terlalu capek untuk berpikir tolonglah bantu...

note: flag format TCP1P{.*}

---

## 🔗 Resources
- Link: https://tcp.1pc.tf/games/11/challenges#310-OTP
- File: https://tcp.1pc.tf/assets/df4dbdabfa78ca1332a86502d061edee84aaaecf90c53ecda4e6fa9c0dc23107/s/CfDJ8FxOmXurdyBOsTXykQypL8VDeNZePYjBNqyQOttmU9qKa8PtQ3kUO4TGB4x8Nh2HfE_4BSF8rO4Fi1M2Koe0fwwcwRJKTPMQpYlSql0V0C7UB4MPWotN2yWQRee2bqcztfJxmf-cWnTf0nyVqH049-bPYFuIHB9QaDEdFQ_emJ5DPihjIvlNiZUe6z8VHMnyFthRTIppBjpxjtcvekc1SU6HERMr6JwCbaRCG9aKt6Vx8qEp_zJqn1b_p2v5dYpf9TpT_RwBdl1tX8G5M7UCGt4/otp_pesan.txt ( [otp_pesan.txt](otp_pesan.txt) )

---

## 🎯 Objective
- Retrieve the key and decrypt the messages to get the flag.

---

# 🧠 Solution

## 🔍 Analysis
We can retrieve the key by xoring the second message with the known plaintext "dengan menyelesaikan tantangan keamanan dalam tim atau individu" but only the first 32 characters (according to the challenge description). After obtaining the key, we can use it to decrypt the first and third messages to retrieve the original messages. The flag is likely hidden in one of these decrypted messages.

---

## 🛠️ Approach
1. XOR the second message with the known plaintext to retrieve the key.
2. Use the retrieved key to XOR with the first and third messages to get the original messages.
3. Analyze the decrypted messages to find the flag.

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
TCP1P{p3serTa_harUs_m3nemUkan_daN_m3ngeksplOitas1_ker3ntanan_s1st3m}

---

## 📚 Lessons Learned
- Understanding the properties of XOR operation is crucial in solving certain types of cryptography challenges.
- In OTP (One-Time Pad) encryption, the key must be truly random and used only once for the encryption to be secure.


---

## 🧷 Notes
- The key retrieved from the second message can only be used to decrypt the first and third messages, as OTP encryption requires the key to be the same length as the plaintext.
- The known plaintext attack is a common technique used in cryptanalysis to retrieve the key when part of the plaintext is known.