# 🔐 Password Security Lab

A simulation project that investigates modern password hashing and password-cracking techniques under realistic attack scenarios.

This project demonstrates why secure password storage mechanisms such as **bcrypt** and **Argon2** are significantly more resistant to password cracking than traditional cryptographic hashes such as **SHA256**.

---

## Project Objectives

The lab investigates:

- SHA256
- bcrypt
- Argon2

under realistic password-cracking scenarios.

The project demonstrates:

- Password hash generation
- Simulated database breaches
- Dictionary attacks
- Smart mutation (rule-based) attacks
- Brute-force attacks
- GPU-style password cracking estimates
- Salted vs unsalted hashing

---

# Project Architecture

```text
User Database
      │
      ▼
Breach Simulator
      │
      ▼
Breached Database
      │
      ▼
Dictionary Attack
      │
      ▼
Mutation Attack
      │
      ▼
Brute Force Simulation
      │
      ▼
GPU Crack-Time Estimator
```

---

# Scenario 1: Data Breach Simulation

A simulated organization stores user passwords using:

- SHA256
- bcrypt
- Argon2

The breach simulator generates a leaked database containing:

```csv
username,algorithm,hash
alice,sha256,...
bob,bcrypt,...
charlie,argon2,...
```

This represents what an attacker would obtain after a real-world breach.

---

# Scenario 2: Dictionary Attack

The attacker attempts to recover passwords using a common password dictionary.

### Process

```text
Dictionary Word
       ↓
Generate Hash
       ↓
Compare Against Stolen Hash
       ↓
Password Recovered
```

### Example Result

```text
Targets: 17
Cracked: 17
Success Rate: 100%
```

### Key Finding

Weak passwords contained in common wordlists can be recovered almost instantly.

---

# Scenario 3: Smart Mutation Attack

The mutation attack simulates rule-based cracking used by professional tools such as:

- Hashcat
- John the Ripper

### Example Transformations

```text
password
password1
password12
password123
password2024
Password123
PASSWORD123
password!
```

### Example Result

```text
Targets: 17
Cracked: 11
Success Rate: 64.7%
```

### Key Finding

Rule-based attacks significantly outperform simple dictionary attacks when passwords contain predictable modifications.

---

# Scenario 4: Brute Force Simulation

The brute-force module systematically tests every possible password combination.

### Example

```text
Target Password: cat12

Attempts: 5,112,461
Time: 6.75 seconds
```

### Key Finding

Brute-force attacks scale exponentially with password length and quickly become impractical.

---

# GPU-Style Speed Simulation

The project estimates how long a modern attacker might require to crack passwords under different hashing algorithms.

### Example: football123

| Algorithm | Estimated Crack Time |
|------------|---------------------|
| SHA256 | 417 Years |
| bcrypt | 41 Million Years |
| Argon2 | 139 Million Years |

### Key Finding

Modern password hashing algorithms intentionally increase attacker workload by several orders of magnitude.

---

# Salt Demonstration

The project demonstrates why salts are critical for secure password storage.

## Without Salt

```text
password123
↓
ef92b778...
ef92b778...
ef92b778...
```

Identical passwords produce identical hashes.

---

## With Salt

```text
password123 + salt1
↓
6303cb...

password123 + salt2
↓
14fd0a...

password123 + salt3
↓
7ef1f8...
```

Identical passwords produce completely different hashes.

### Key Finding

Salting prevents:

- Rainbow table attacks
- Hash reuse detection
- Mass password recovery attacks

---

# Hashing Benchmark

Benchmark results obtained during testing:

| Algorithm | Average Hash Time |
|------------|------------------|
| SHA256 | 0.000001 s |
| Argon2 | 0.039284 s |
| bcrypt | 0.198009 s |

### Key Finding

SHA256 is extremely fast and therefore unsuitable for password storage.

bcrypt and Argon2 deliberately slow attackers by increasing computational cost.

---

# Streamlit Dashboard

The project includes an interactive Streamlit interface featuring:

- Executive Summary
- Hash Generator
- Breached Database Viewer
- Benchmark Results
- Attack Results
- GPU Simulation
- Salt Demonstration

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/password-crack-lab.git

cd password-crack-lab
```

---

## Install Dependencies

Using Poetry:

```bash
poetry install
```

---

## Run Streamlit Dashboard

```bash
poetry run python -m streamlit run app.py
```

---

# Disclaimer

This project is intended solely for:

- Security awareness
- Password security research
- Demonstrating secure password storage practices

Do not use these techniques against systems or accounts without explicit authorisation.

---

Cybersecurity • Cryptography • Quantum-Safe Security
