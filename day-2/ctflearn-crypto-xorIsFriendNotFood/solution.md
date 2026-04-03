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