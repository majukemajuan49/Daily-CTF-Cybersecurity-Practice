# 🧩 Challenge

## 📌 Basic Info
- **Name**: Symbolic Decimals
- **Platform**: ctflearn
- **Category**: Cryptography
- **Difficulty**: Hard
- **Points**: 80

---

## 📖 Description
Did you know that you can hide messages with symbols? For example, !@#$%^&*( is 123456789!<br /> Now Try: ^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@% However, this isn't as easy as you might think.

---

## 🔗 Resources
- Link: https://ctflearn.com/challenge/231
- File: -

---

## 🎯 Objective
- Decode the given string to find the flag.

---

# 🧠 Solution

## 🔍 Analysis
The given string is a sequence of symbols that represent decimal digits. It is taken from "when you hold shift on the keyboard and type 123456789" rule. Each symbol corresponds to a specific digit from 0 to 9 and separated by commas which represent groups of digits. Each digit group is then converted to its corresponding character. By decoding the symbols into their respective digits, we can reconstruct the original message, which is likely the flag.

---

## 🛠️ Approach
1. Create a mapping of symbols to their corresponding digits based on the "shift + number" rule.
2. Split the given string by commas to get individual groups of symbols.
3. For each group of symbols, convert each symbol to its corresponding digit using the mapping.
4. Combine the digits to form a number, and then convert that number to its corresponding ASCII character.
5. Concatenate all the characters to get the final decoded message, which should be the flag.

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
```CTF{Star_._Wars_._For_._Life}```

---

## 📚 Lessons Learned
- Symbolic representations can be used to encode messages in a way that requires understanding the underlying mapping to decode.
- The "shift + number" rule can be a useful hint in decoding puzzles that involve symbols.

---

## 🧷 Notes
- The key to solving this challenge was recognizing the pattern of symbols and their corresponding digits, which is a common encoding method in CTF challenges.