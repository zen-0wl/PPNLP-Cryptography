# Quantum Threat Simulator

An interactive educational platform demonstrating how quantum computers threaten classical public-key cryptography and how Learning With Errors (LWE) provides the foundation for post-quantum cryptographic systems.

---

## Overview

Modern cryptographic systems such as RSA and Elliptic Curve Cryptography (ECC) derive their security from mathematical problems that are computationally difficult for classical computers.

Quantum computers introduce new algorithms, most notably Shor's Algorithm, that can efficiently solve these problems and potentially compromise widely deployed cryptographic systems.

This project explores:

* Why RSA and ECC become vulnerable in a quantum era
* How quantum attacks affect public-key cryptography
* How Learning With Errors (LWE) works as a post-quantum alternative
* Security, performance, and size tradeoffs between classical and post-quantum systems

---

## Features

### Quantum Attack Simulation

Visual explanation of how Shor's Algorithm can break RSA by factoring large integers.

### Classical Cryptography Demo

* RSA key generation
* RSA encryption and decryption
* Simplified ECC key exchange

### LWE Encryption Demo

Interactive demonstration of:

* Key generation
* Encryption
* Decryption
* Public and private key relationships

### Noise Visualisation

Illustrates the role of noise in LWE security and its impact on successful decryption.

### Benchmark Dashboard

Comparison of:

* RSA
* ECC
* LWE

Across:

* Key size
* Encryption performance
* Decryption performance
* Quantum resistance

---

## Architecture

Frontend:

* React
* TypeScript
* Tailwind CSS
* Recharts

Backend:

* FastAPI
* Python
* Poetry

---

## Running Locally

### Backend

```bash
cd backend

poetry install

poetry run uvicorn app.main:app --reload
```

Backend available at:

```text
http://127.0.0.1:8000
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend available at:

```text
http://localhost:5173
```

---

## Project Objectives

This project was developed to investigate the impact of quantum computing on modern cryptographic systems and to explore post-quantum alternatives through interactive visualisations and demonstrations.

---

## Educational Disclaimer

The cryptographic implementations used are intentionally simplified for educational purposes and should not be used in production environments.

---
