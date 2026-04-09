# 🧩 Challenge

## 📌 Basic Info
- **Name**: euclid's apprentice
- **Platform**: TCP1P
- **Category**: Cryptography
- **Difficulty**: -
- **Points**: 248 (when solved)

---

## 📖 Description
Pengetahuan yang baik dalam modular arithmetic akan sangat membantumu dalam crypto, terutama dalam memahami beberapa algoritma seperti RSA dan Diffie-Hellman. Kalau begitu, mari mulai dari basic-nya. Zaman dahulu kala, Euclid menemukan sebuah cara untuk menghitung faktor persekutuan terbesar/greatest common divisor (GCD) dari dua bilangan bulat a dan b dengan cepat (Euclidean algortihm).

Memperluas algoritmanya (Extended euclidean algorithm), kita juga bisa menemukan bilangan bulat x dan y yang memenuhi ax + by = gcd(a,b).

Hints:

angka 23 dan getPrime(216) itu konstanta random, tidak perlu dipikirkan
ingat baik-baik apa output yang diberikan gcd() dan egcd()

---

## 🔗 Resources
- Link: https://tcp.1pc.tf/games/11/challenges#303-euclid's-apprentice
- File: https://tcp.1pc.tf/assets/ce78850d8315b995014595d4c8645f8b71e8c06c2b84bdc2c8f0eb609a7c838b/s/CfDJ8FxOmXurdyBOsTXykQypL8V9UcZ9E-zsUlil-OHwVGsveGn8P1yM1b4h6T7hXlmZs9L_z0l2A9di8G2YheEhDimDCTCnw9vesMvG95XfKTqxWHVfJTlOPoipJKK7shY1v0MwOYT3FmLlHhqzITZS_1gCpANkTNrSkomRQOXeQ67jK5f4Ol72OTyqOHR09Xza165-selFXkUXocxab3lwgz182ftKztyfS4d9BzAnmeOg4RnS8I_Tnr2ynAFqypxpvYqtrdtZun-EPdVHTOq33uw/euclidsapprentice_euclidsapprentice-dist.zip ( [chall.py](chall.py), [output.txt](output.txt) )

---

## 🎯 Objective
- Decrypt the separated flag from the information given in the output.txt and chall.py

---

# 🧠 Solution

## 🔍 Analysis
Using the equations known in the chall.py and reusing the same `egcd` function, we can find the value of the first flag part and retrieve x and y used to retrieve the second flag part.

---

## 🛠️ Approach
1. Calculate `m1` by square rooting the `c1 - 23` which is the first flag part
2. Mimic the calculation of x and y using the `egcd` function with c1 and c2 as inputs
3. Calculate the second flag part `m2` using the retrieved x and y values by `m2 = c3 // (x * y)`
4. Combine the two flag parts to get the full flag

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
TCP1P{eucl1de4n_alg0r1thmmmm_4ndd_b3z0utsss_1d3ntityyyy}

---

## 📚 Lessons Learned
- Understanding the Extended Euclidean Algorithm and its applications in cryptography
- How to manipulate modular arithmetic to retrieve hidden information

---

## 🧷 Notes
- The constants used in the equations (like 23 and getPrime(216)) are not relevant to the solution, so they can be ignored.
- The key to solving the challenge is to understand how the equations relate to each other and how to use the Extended Euclidean Algorithm to find the necessary values for decryption.