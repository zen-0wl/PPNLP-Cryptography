# Crypto Primitives from Scratch

## Project Overview

This project implements four fundamental cryptographic primitives from scratch using Python:

1. RSA Encryption
2. Diffie-Hellman Key Exchange
3. Hash Functions
4. Digital Signatures

The objective is not to build production-ready cryptography, but to understand how these primitives work internally and why modern systems use more advanced and secure variants.

In addition to implementing each primitive, this project demonstrates common attacks and weaknesses associated with simplified cryptographic systems.

---

## Objectives

This project aims to:

* Understand the mathematical foundations of cryptography.
* Implement cryptographic primitives without relying on cryptographic libraries.
* Demonstrate common vulnerabilities in naïve implementations.
* Compare educational implementations against real-world cryptographic systems.
* Simulate secure communication using multiple cryptographic primitives.

---

# 1. RSA Encryption

## Theory

RSA is an asymmetric cryptographic algorithm based on the difficulty of factoring large integers.

### Key Generation

Choose two prime numbers:

```text
p = 61
q = 53
```

Compute:

```text
n = p × q = 3233
```

Euler's Totient:

```text
φ(n) = (p − 1)(q − 1)
```

Choose:

```text
e = 17
```

Compute:

```text
d = e⁻¹ mod φ(n)
```

Public Key:

```text
(e, n)
```

Private Key:

```text
(d, n)
```

---

## Encryption

```text
C = M^e mod n
```

---

## Decryption

```text
M = C^d mod n
```

---

## Demonstration

```bash
poetry run python -m rsa_module.rsa_demo
```

Example Output:

```text
Original Message: 65
Encrypted Message: 2790
Decrypted Message: 65
```

---

## Attack Demonstration

```bash
poetry run python -m rsa_module.rsa_attack
```

The attack factors:

```text
3233 = 53 × 61
```

and reconstructs the private key.

---

## Why This RSA Is Insecure

The implementation uses extremely small primes.

An attacker can easily factor:

```text
n = 3233
```

and recover:

```text
p
q
φ(n)
d
```

This completely breaks the system.

---

## Real-World RSA

Modern systems use:

* RSA-2048
* RSA-3072
* OAEP Padding
* PKCS#1 Standards

Applications:

* TLS
* Certificates
* Secure Key Exchange

---

# 2. Diffie-Hellman Key Exchange

## Theory

Diffie-Hellman allows two parties to establish a shared secret over an insecure channel.

Shared parameters:

```text
p = 23
g = 5
```

Alice chooses:

```text
a
```

Bob chooses:

```text
b
```

Public values:

```text
A = g^a mod p
B = g^b mod p
```

Shared secret:

```text
S = B^a mod p
S = A^b mod p
```

---

## Demonstration

```bash
poetry run python -m diffie_hellman.dh_demo
```

Example Output:

```text
Alice Shared Secret = 2
Bob Shared Secret = 2
```

---

## Man-in-the-Middle Attack

```bash
poetry run python -m diffie_hellman.mitm_attack
```

Mallory intercepts public keys and establishes independent keys with Alice and Bob.

Result:

```text
Alice ↔ Mallory
Mallory ↔ Bob
```

Instead of:

```text
Alice ↔ Bob
```

---

## Why This Is Insecure

Basic Diffie-Hellman does not authenticate participants.

An attacker can:

* Intercept public keys
* Replace public keys
* Establish separate secrets

This is the classic Man-in-the-Middle (MITM) attack.

---

## Real-World Systems

Modern protocols use:

* ECDH
* ECDHE
* Digital Certificates
* TLS Authentication

Applications:

* HTTPS
* Signal
* WhatsApp

---

# 3. Hash Function

## Theory

A hash function maps arbitrary-length input into a fixed-size output.

Implemented Toy Hash:

```python
h = (h * 31 + ord(character)) % 100000
```

---

## Demonstration

```bash
poetry run python -m hash_function.hash_demo
```

Example:

```text
HELLO → 24562
```

Properties:

* Deterministic
* Fixed-length output
* Fast computation

---

## Collision Demonstration

```bash
poetry run python -m hash_function.collision_demo
```

Example:

```text
DTHHJ → 73370
YTNQX → 73370
```

Two different inputs produce identical outputs.

---

## Why This Is Insecure

The hash space contains only:

```text
100,000 outputs
```

Collisions occur quickly.

Missing properties:

* Collision Resistance
* Preimage Resistance
* Second-Preimage Resistance
* Strong Avalanche Effect

---

## Real-World Hash Functions

Modern systems use:

* SHA-256
* SHA-3
* BLAKE3

Applications:

* Password Storage
* Blockchain
* Data Integrity
* Digital Signatures

---

# 4. Digital Signatures

## Theory

Digital signatures provide:

* Authentication
* Integrity
* Non-repudiation

Workflow:

```text
Message
↓
Hash
↓
Private Key
↓
Signature
```

Verification:

```text
Signature
↓
Public Key
↓
Recovered Hash
↓
Compare Hashes
```

---

## Demonstration

```bash
poetry run python -m digital_signature.sign_demo
```

Example:

```text
Message: Transfer RM100
Signature: 1797
Verification Result: True
```

---

## Message Tampering Attack

```bash
poetry run python -m digital_signature.forgery_demo
```

Original:

```text
Transfer RM100
```

Modified:

```text
Transfer RM1000
```

Result:

```text
Verification Failed
Tampering Detected
```

---

## Why This Is Insecure

This implementation uses:

* Small RSA keys
* Toy hash function
* Raw RSA signatures

It is suitable only for educational purposes.

---

## Real-World Digital Signatures

Modern systems use:

* RSA-PSS
* ECDSA
* Ed25519

Applications:

* Software Updates
* TLS Certificates
* Code Signing
* Cryptocurrency Wallets

---

# Integrated Secure Messaging System

This project combines all implemented primitives into a simplified secure communication system.

Workflow:

```text
Alice
│
├─ Diffie-Hellman
│
├─ Shared Secret
│
├─ Hash Message
│
├─ Sign Message
│
└─ Send
      Message
      Signature
      Shared Secret

Bob
│
└─ Verify Signature
```

---

## Normal Communication

```bash
poetry run python -m integrated_system.secure_messaging
```

Result:

```text
Shared secret established
Signature verified
Message accepted
```

---

## Attack Simulation

```bash
poetry run python -m integrated_system.attack_simulation
```

Result:

```text
Message modified
Verification failed
Message rejected
```

This demonstrates how digital signatures protect against message tampering.

---

# Security Analysis Summary

| Primitive         | Educational Version | Vulnerability | Real-World Alternative |
| ----------------- | ------------------- | ------------- | ---------------------- |
| RSA               | Small RSA           | Factorization | RSA-2048 / RSA-3072    |
| Diffie-Hellman    | Unauthenticated DH  | MITM Attack   | ECDHE + Certificates   |
| Hash Function     | Toy Hash            | Collisions    | SHA-256 / SHA-3        |
| Digital Signature | Raw RSA Signature   | Weak Security | RSA-PSS / Ed25519      |

---

# Installation

Clone repository:

```bash
git clone
cd crypto-primitives-scratch
```

Install dependencies:

```bash
poetry install
```

Activate environment:

```bash
poetry shell
```

---

# Running All Demonstrations

RSA:

```bash
poetry run python -m rsa_module.rsa_demo
poetry run python -m rsa_module.rsa_attack
```

Diffie-Hellman:

```bash
poetry run python -m diffie_hellman.dh_demo
poetry run python -m diffie_hellman.mitm_attack
```

Hash Function:

```bash
poetry run python -m hash_function.hash_demo
poetry run python -m hash_function.collision_demo
```

Digital Signatures:

```bash
poetry run python -m digital_signature.sign_demo
poetry run python -m digital_signature.forgery_demo
```

Integrated System:

```bash
poetry run python -m integrated_system.secure_messaging
poetry run python -m integrated_system.attack_simulation
```

---

# Disclaimer

This project is intended solely for educational purposes.

The implementations are deliberately simplified and should never be used in production systems. Real-world cryptographic systems require secure parameter selection, standardized algorithms, proper randomness, authenticated key exchange, and resistance against modern cryptographic attacks.
