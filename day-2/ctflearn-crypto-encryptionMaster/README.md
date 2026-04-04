# 🧩 Challenge

## 📌 Basic Info
- **Name**: Encryption Master
- **Platform**: ctflearn
- **Category**: Cryptography
- **Difficulty**: Hard
- **Points**: 90

---

## 📖 Description
Alright. Serious talk. You need to work pretty hard for this one (unless you are an encryption god.) Well, good luck. https://mega.nz/#!iPgzXIiD!Pkza_S8YUxIXrZ7gdwMcIoufMzi_FjSio3Vx9GuL0ok

---

## 🔗 Resources
- Link: https://ctflearn.com/challenge/243
- File: https://mega.nz/#!iPgzXIiD!Pkza_S8YUxIXrZ7gdwMcIoufMzi_FjSio3Vx9GuL0ok

---

## 🎯 Objective
- Decrypt the given encoded strings to find the flag.

---

# 🧠 Solution

## 🔍 Analysis
This chall involves multiple encodings methods to obfuscate the flag. 

---

## 🛠️ Approach
1. Decoding per layer will lead us to the next layer of encoding and what type of encoding it is.
2. Later it is revealed that the sequence of method to decode is: base64 -> hex -> binary -> base64. 

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
CTF{I_AM_PROUD_OF_YOU}

---

## 📚 Lessons Learned
- When dealing with multiple layers of encoding, it is important to analyze the output of each decoding step to determine the next encoding method used. Common patterns in the output can provide hints on how to proceed with the next decoding step.

---

## 🧷 Notes
- In CTF challenges, it is common to encounter multiple layers of encoding. Always pay attention to the output of each decoding step, as it can provide clues on the next encoding method used.