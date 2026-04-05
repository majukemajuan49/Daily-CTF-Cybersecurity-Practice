# 🧩 Challenge

## 📌 Basic Info
- **Name**: mbptl-2
- **Platform**: TCP1P
- **Category**: Web
- **Difficulty**: -
- **Points**: 100

---

## 📖 Description
MBPTL Flag 2 - HTTP Header

Look at HTTP response headers to find the flag.

Start challenge from: https://gzcli.1pc.tf/mbptl-ctf-pentest-mbptl-1

---

## 🔗 Resources
- Link: https://tcp.1pc.tf/games/14/challenges#412-mbptl-2
- File: -

---

## 🎯 Objective
- Find the flag hidden in the HTTP response headers.

---

# 🧠 Solution

## 🔍 Analysis
The flag is hidden in the HTTP response headers, so we need to inspect the headers of the response from the bookstore homepage.

---

## 🛠️ Approach
1. Use a programming language like Python with the `requests` library to send a GET request to the bookstore homepage.
2. Print the response headers to find the flag.
3. Later on we find out that the flag is in a custom header called `X-MBPTL`.
4. Extract the flag from the `X-MBPTL` header.

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
MBPTL-2{2538dc5426d2e3ca16957a091bf8c0f3}

---

## 📚 Lessons Learned
- HTTP headers can sometimes contain sensitive information or flags in CTF challenges, so always check the response headers when looking for hidden clues.

---

## 🧷 Notes
- This challenge is straightforward and serves as a reminder to always check the HTTP response headers for hidden information in web-based CTF challenges.