# RSA-Algorithm
Rivest-Shamir-Adleman (RSA) encryption algorithm from scratch.

Cybersecurity, at its core, is not just about code, firewalls, or algorithms — it’s about **protecting people**.
Every password protected, every encrypted message, every secure transaction — these all preserve **trust, privacy, and human dignity** in our digital world.

That’s why cryptography, especially **RSA encryption**, is not just mathematics — it’s **humanity safeguarded through numbers**.

---

## 🔐 **Rivest–Shamir–Adleman (RSA) Encryption**

RSA is one of the **most famous public-key cryptography algorithms**, used for securing data transmission, digital signatures, and authentication.

---

### 🧠 **1. The Core Idea**

RSA is based on one simple mathematical fact:

> It’s **easy** to multiply two large prime numbers together,
> but **extremely hard** to find those primes again from their product.

That one-way difficulty forms the backbone of RSA’s security.

---

### ⚙️ **2. The Building Blocks**

RSA uses **two keys**:

* **Public Key** – used to *encrypt* data (shared with everyone)
* **Private Key** – used to *decrypt* data (kept secret)

These keys are generated together in a way that they are mathematically linked.

---

### 🧩 **3. Key Generation Steps (Step-by-Step)**

#### **Step 1: Choose Two Prime Numbers**

Let’s pick small ones for simplicity:
p = 7, q = 11

#### **Step 2: Compute n (the modulus)**

n = p × q = 7 × 11 = **77**

> n will be part of both the public and private keys.

#### **Step 3: Compute ϕ(n) (Euler’s Totient Function)**

ϕ(n) = (p − 1) × (q − 1) = 6 × 10 = **60**

#### **Step 4: Choose an Encryption Key (e)**

Choose an integer **e** that is:

* 1 < e < ϕ(n)
* e and ϕ(n) are *coprime* (no common factors except 1)

Let’s pick **e = 13**

#### **Step 5: Compute Decryption Key (d)**

Find **d** such that:
(d × e) mod ϕ(n) = 1

So, (d × 13) mod 60 = 1 → **d = 37** (because 13×37 = 481 → 481 mod 60 = 1)

---

### 🔑 **4. Your Keys Are:**

* **Public Key (e, n)** = (13, 77)
* **Private Key (d, n)** = (37, 77)

---

### 📥 **5. Encryption Process**

Let’s encrypt the message **M = 9** (just a number for illustration).
Formula:

> C = M^e mod n

C = 9¹³ mod 77 = **62**

So, ciphertext **C = 62**

---

### 📤 **6. Decryption Process**

Formula:

> M = C^d mod n

M = 62³⁷ mod 77 = **9**

The original message is recovered!

---

### 🧩 **7. Real-World Use**

RSA uses **very large primes** (hundreds or thousands of bits long) — not small ones like 7 and 11.
But the principle is identical.

RSA is used in:

* 🔒 HTTPS (SSL/TLS encryption)
* 💳 Secure transactions (digital payments)
* 📧 Email encryption
* 🔏 Digital signatures & certificates


* Your personal chats remain private.
* Online banking transactions stay secure.
* Journalists and whistleblowers can communicate safely.
* Sensitive data, from hospitals to humanitarian organizations, stays confidential.
