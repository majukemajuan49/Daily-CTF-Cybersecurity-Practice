# 🧩 Challenge

## 📌 Basic Info
- **Name**: XOR Is Friend Not Food
- **Platform**: ctflearn
- **Category**: Cryptography
- **Difficulty**: Hard
- **Points**: 100

---

## 📖 Description
Here: \t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e

I think the flag started with: ctflearn{

---

## 🔗 Resources
- Link: https://ctflearn.com/challenge/165
- File: -

---

## 🎯 Objective
- Decrypt the given string to find the flag.

---

# 🧠 Solution

## 🔍 Analysis
We can recover the key but partially. We can only recover the first 9 bytes of the key because we know the first 9 bytes of the plaintext (ctflearn{). After that, we can only guess the rest of the key and check if it produces a valid flag format (ending with } and containing only valid characters).

---

## 🛠️ Approach
1. XOR the first 9 bytes of the ciphertext with "ctflearn{" to get the first 9 bytes of the key.
2. We got "jowlsjowl". We can guess that the key is "jowlsjowl" repeated (since XOR is a repeating key cipher).
3. So the complete key would be "jowlsjowljowlsjowljowlsjowl...".
4. Add "s" to the end of the key to make it "jowlsjowls" which is the complete key.
5. XOR the ciphertext with the complete key to get the plaintext.

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
ctflearn{xor_is_the_goop}

---

## 📚 Lessons Learned
- XOR is a fundamental operation in cryptography and can be used to both encrypt and decrypt data.
- Knowing part of the plaintext can help recover the key in a repeating key XOR cipher.

---

## 🧷 Notes
- The key is repeated in a XOR cipher, so once we recover part of the key, we can guess the rest of it.