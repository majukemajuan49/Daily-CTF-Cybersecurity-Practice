# 🧩 Challenge

## 📌 Basic Info
- **Name**: mbptl-5
- **Platform**: TCP1P
- **Category**: Web
- **Difficulty**: -
- **Points**: 100

---

## 📖 Description
MBPTL Flag 5 - SQL Injection Error

Trigger an SQL error to reveal the flag.

Start challenge from: https://gzcli.1pc.tf/mbptl-ctf-pentest-mbptl-1

---

## 🔗 Resources
- Link: https://tcp.1pc.tf/games/14/challenges#420-mbptl-5
- File: -

---

## 🎯 Objective
- Trigger an SQL error on the web application to reveal the flag.

---

# 🧠 Solution

## 🔍 Analysis
First we need to identify which endpoint may perform SQL queries. After identifying the endpoint, we can try to trigger an SQL error by injecting a single quote (`'`) or other SQL syntax that may cause an error. The error message may contain the flag.

---

## 🛠️ Approach
1. Identified endpoint http://gzcli.1pc.tf:40731/detail.php?id=1
2. The `id` parameter is likely used in an SQL query. We can try to inject a single quote (`'`) to trigger an SQL error.
3. After injecting the single quote, we can analyze the error message to find the flag.
4. Error message
```
Error: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' LIMIT 1' at line 1
MBPTL-5{ecfccdccc915eec43cfbcca2d0489204}
```

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
MBPTL-5{ecfccdccc915eec43cfbcca2d0489204}

---

## 📚 Lessons Learned
- SQL Injection can be exploited to reveal sensitive information such as flags in CTF challenges.

---

## 🧷 Notes
- Always sanitize user input to prevent SQL Injection vulnerabilities in web applications.