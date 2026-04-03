# 🧠 Solution

## 🔍 Analysis
RSA with big public exponent e is vulnerable to Wiener's attack if the private exponent d is small. The attack exploits the fact that if d is small, then the fraction k/d (where k is an integer) can be approximated by a convergent of the continued fraction expansion of e/n. By computing the continued fraction expansion of e/n and checking the convergents, we can find potential candidates for d.

Usually if we found RSA with big e, we can try to apply Wiener's attack to find d. In this case, we can use the `attack` function from the `owiener` module in Python to compute d.

---

## 🛠️ Approach
1. Wiener attack from github: https://github.com/orisano/owiener
2. Use the `attack` function to compute d from e and n.

---

## 💻 Exploit / Code
[solver.py](solver.py)

---

## 🚩 Flag
SKR{350786625978064581215135530033089387015206639800834956950379423314875105929452468001147105402517815123935962549902126256855950505671860607588880149111769}


---

## 📚 Lessons Learned
- RSA with big e can be vulnerable to Wiener's attack if d is small.
- Whenever we encounter RSA with big e, we should consider applying Wiener's attack to find d.

---

## 🧷 Notes
- Always check for common vulnerabilities in RSA, such as big public exponent.