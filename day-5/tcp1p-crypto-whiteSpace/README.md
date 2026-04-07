# 🧩 Challenge

## 📌 Basic Info
- **Name**: White Space
- **Platform**: TCP1P
- **Category**: Cryptography
- **Difficulty**: -
- **Points**: 221 (when solved)

---

## 📖 Description
KOSONG ?!?!?!?! Astaghfirullahaladzim !!!

https://youtu.be/WvEbvShTss4?si=zl075Vh6DpFEX7Rp

Hints
Jangan terpatok sama randomnya
Coba bruteforce buat nemuin prefix flagnya

---

## 🔗 Resources
- Link: https://tcp.1pc.tf/games/11/challenges#322-White-Space
- File: https://tcp.1pc.tf/assets/e56b3ff052831b03577424b947815332826ee81caae011f6628f69496c0c9ba7/s/CfDJ8FxOmXurdyBOsTXykQypL8UHQ92vIl0NRITcguhp7Q-URkC3ml3fSq_i7fpjZpxxYrEwv4rg2SYeG6xK9rAE3NzJYXot7-BkY4vHPjuW27WFAV0DAebke6Nh-sUtwbnZnSQm-niZ2qN5acVVNyQehGJweDg2vBzH6weMF1dsfzLwiARrmJzr2CmW4kdWL23p4HsP3cxQhmp0zQRpYYHeE02k3VQSz9apDhm1P7nbTy_CCO8u8PXoRl6Ew63Ez8KDwfi5FmogR3MLG57gmyjnmMA/whitespace_whitespace-dist.zip ( [chall.py](chall.py), [output.txt](output.txt) )

---

## 🎯 Objective
- Retrieve the hidden flag by analyzing the whitespace patterns in the provided output.

---

# 🧠 Solution

## 🔍 Analysis
Every encoded character are seperated with `\n`. key_1 is used for even indexed characters and key_2 is used for odd indexed characters. By knowing the prefix of the flag TCP1P{} we can use 'T' to calculate key_1 and 'C' to calculate key_2.

---

## 🛠️ Approach
1. Split the output by `\n` to get the encoded characters.
2. Use the known prefix of the flag to calculate key_1 and key_2.
```
key1 = length of encoded 'T' // ascii value of 'T'
key2 = length of encoded 'C' // ascii value of 'C'
```
3. Use the calculated keys to decode the rest of the characters.
```
decoded_char = length of encoded char // key (key_1 for even index, key_2 for odd index)
```
4. Combine the decoded characters to retrieve the flag.

---

## 💻 Exploit / Code
[debug.py](debug.py)
[solver.py](solver.py)

---

## 🚩 Flag
TCP1P{I_h4Ve_TrIed_noT_t0_Be_se3n}

---

## 📚 Lessons Learned
- Understanding how whitespace can be used to encode information.
- The importance of analyzing patterns in seemingly random data.

---

## 🧷 Notes
- Always look for known patterns or prefixes when dealing with encoded data, as they can provide crucial hints for decoding.