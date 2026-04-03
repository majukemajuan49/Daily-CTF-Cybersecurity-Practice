# 🧠 Solution

## 🔍 Analysis
Stacked base64 encoded strings. Assume that the flag has a "{" character, just decode it recursively until we get a plaintext containing "{".

---

## 🛠️ Approach
1. Decode the given string from base64 recursively until we get a plaintext containing "{".

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
ABCTF{pr3tty_b4s1c_r1ght?}

---

## 📚 Lessons Learned
- Base64 encoding can be stacked multiple times, and it is important to check for common patterns (like "{" in flags) to know when to stop decoding.

---

## 🧷 Notes
- Stacked encodings can be a common technique in CTF challenges to obfuscate the flag. Always look for hints in the challenge description and use them to guide your decoding process.