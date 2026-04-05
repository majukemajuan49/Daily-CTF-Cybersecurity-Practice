# 🧩 Challenge

## 📌 Basic Info
- **Name**: mbptl-3
- **Platform**: TCP1P
- **Category**: Web
- **Difficulty**: -
- **Points**: 100

---

## 📖 Description
MBPTL Flag 3 - Directory Enumeration

The administrator panel is under maintenance. Check the directory listing.

Start challenge from: https://gzcli.1pc.tf/mbptl-ctf-pentest-mbptl-1

---

## 🔗 Resources
- Link: https://tcp.1pc.tf/games/14/challenges#417-mbptl-3
- File: -

---

## 🎯 Objective
- Find the flag hidden in the directory listing of the administrator panel (initially)
- Turns out the administrator panel is on a different port, it's provided so just access it anyway

---

# 🧠 Solution

## 🔍 Analysis
Just access the administrator panel on the provided port.

---

## 🛠️ Approach
1. Access the administrator panel on the provided port
2. Fetch the flag right away

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
MBPTL-3{561fcbc74844bcc32731cfb3508c86d1}

---

## 📚 Lessons Learned
- Sometimes, the flag can be hidden in a different location than expected, so it's important to explore all provided resources and hints in CTF challenges.

---

## 🧷 Notes
- This challenge is straightforward and serves as a reminder to always explore all provided resources and hints in CTF challenges, as the flag may not always be located where you initially expect it to be.