# Secure Messaging System 🔐

A foundation-level secure messaging prototype implementing modern cryptographic primitives for authenticated key exchange and encrypted communication.

## Features

* **Identity authentication** using **Ed25519** digital signatures
* **Secure key exchange** using **X25519 / ECDH**
* **Key derivation** using **HKDF-SHA256**
* **Authenticated encryption** using **ChaCha20-Poly1305 (AEAD)**
* **Forward secrecy** via fresh ephemeral session keys
* **Replay protection** using message sequence identifiers
* **Interactive CLI secure chat** with session termination support

## Architecture

The system is built in four layers:

1. **Identity Layer**

   * Long-term Ed25519 keypairs
   * Message / key signing
   * Signature verification
2. **Key Exchange Layer**

   * Ephemeral X25519 keys
   * ECDH shared secret generation
3. **Key Derivation**

   * Shared secret processed through HKDF
   * 256-bit session key generation
4. **Message Protection**

   * AEAD encryption with ChaCha20-Poly1305
   * Confidentiality + integrity protection
5. **Session Security Enhancements**

   * Forward secrecy through ephemeral X25519 keys per session
   * Replay protection using unique message IDs
   * Interactive CLI message loop
---

## Threat Model

This system assumes an attacker may:

* intercept messages
* modify ciphertext
* inject forged messages
* attempt impersonation

Private keys are assumed uncompromised.

---

## Why AEAD?

AEAD (Authenticated Encryption with Associated Data) is used because it provides:

* **confidentiality** → attackers cannot read messages
* **integrity** → tampering is detected
* **authenticity** → forged ciphertext is rejected

This prevents silent modification attacks.

---

## Key Derivation

The session key is derived as follows:

```text
ECDH shared secret → HKDF-SHA256 → 256-bit session key
```

Raw ECDH output is never used directly.

---

## Attacks Prevented

* eavesdropping
* ciphertext tampering
* message forgery
* impersonation
* man-in-the-middle (via signature verification)
* replay attacks (via message ID tracking)

---
## Additional Security Features

### Forward Secrecy
Fresh ephemeral X25519 keypairs are generated for every session, ensuring compromise of one session key does not expose previous sessions.

### Replay Protection
Each encrypted message includes a unique sequence identifier. Previously seen identifiers are rejected to prevent replay attacks.

### CLI Secure Chat
The system includes an interactive terminal-based chat loop with graceful session termination using `exit`.

---
## Run

```bash
poetry install --no-root
poetry run python main.py
```



## Test

```bash
poetry run pytest
```
