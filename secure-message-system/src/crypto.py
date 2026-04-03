import os
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305


def encrypt_message(key: bytes, plaintext: str):
    nonce = os.urandom(12)
    cipher = ChaCha20Poly1305(key)
    ciphertext = cipher.encrypt(nonce, plaintext.encode(), None)
    return nonce, ciphertext


def decrypt_message(key: bytes, nonce: bytes, ciphertext: bytes):
    cipher = ChaCha20Poly1305(key)
    plaintext = cipher.decrypt(nonce, ciphertext, None)
    return plaintext.decode()