# 🧩 Challenge

## 📌 Basic Info
- **Name**: mbptl-1
- **Platform**: TCP1P
- **Category**: Web
- **Difficulty**: -
- **Points**: 100

---

## 📖 Description
MBPTL Flag 1 - HTML Source Comment

Find the flag hidden in the HTML source code comments of the bookstore homepage.

Start challenge from: https://gzcli.1pc.tf/mbptl-ctf-pentest-mbptl-1

---

## 🔗 Resources
- Link: https://tcp.1pc.tf/games/14/challenges#408-mbptl-1
- File: -

---

## 🎯 Objective
- Find the flag hidden in the HTML source code comments of the bookstore homepage.

---

# 🧠 Solution

## 🔍 Analysis
Simply view the page source of the bookstore homepage to find the flag hidden in the HTML comments or use a tool like `curl` to fetch the page source and search for the flag.

---

## 🛠️ Approach
1. Open the bookstore homepage in a web browser.
2. Right-click on the page and select "View Page Source" or use `Ctrl+U` to view the HTML source code.
3. Search for HTML comments (<!-- ... -->) in the source code.
4. Look for the flag format (MBPTL-1{...}) within the comments.
5. Alternatively, use a python script with `requests` to fetch the page source and search for the flag with regular expressions.

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
MBPTL-1{c54fece87eff31e3e3eba57f82e33616}

---

## 📚 Lessons Learned
- HTML comments can sometimes contain sensitive information or flags in CTF challenges, so always check the page source when looking for hidden clues.

---

## 🧷 Notes
- This challenge is straightforward and serves as a reminder to always check the source code for hidden information in web-based CTF challenges.