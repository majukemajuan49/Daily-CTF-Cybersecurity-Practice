# 🧩 Challenge

## 📌 Basic Info
- **Name**: mbptl-4
- **Platform**: TCP1P
- **Category**: Web
- **Difficulty**: -
- **Points**: 100

---

## 📖 Description
MBPTL Flag 4 - Login Page Source

Check the login page source code for hidden flags.

Start challenge from: https://gzcli.1pc.tf/mbptl-ctf-pentest-mbptl-1

---

## 🔗 Resources
- Link: https://tcp.1pc.tf/games/14/challenges#410-mbptl-4
- File: -

---

## 🎯 Objective
- Access the login page and check its source code for flag (hidden / in plain sight).

---

# 🧠 Solution

## 🔍 Analysis
Since we don't know the specific endpoint for the login page, we can use directory enumeration to find it. Once we find the login page, we can check its source code for the flag.

---

## 🛠️ Approach
1. Perform directory enumeration to find the login page.
2. In this case, I used `dirsearch` with a common wordlist to find the login page.
3. Found `[12:30:19] 200 -  755B  - /administrator/index.php`
4. Access the login page and check its source code for the flag.
5. Found the flag in the source code of the login page or use regex to extract it.

---

## 💻 Exploit / Code
[solver.py](solver.py)
[reports/http_gzcli.1pc.tf_40796/ (dirsearch results)](reports/http_gzcli.1pc.tf_40796/)

---

## 🚩 Flag
MBPTL-4{fe45bec5ee4d5bf8628e79e8267a19f1}

---

## 📚 Lessons Learned
- Directory enumeration is a crucial technique in a penetration web-based CTF challenges to discover hidden endpoints, such as login pages, which may contain flags in their source code.

---

## 🧷 Notes
- This challenge emphasizes the importance of exploring all aspects of a web application, including hidden directories and source code, to find flags in CTF challenges.