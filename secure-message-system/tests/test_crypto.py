from src.crypto import encrypt_message, decrypt_message
import os


def test_encrypt_decrypt():
    key = os.urandom(32)

    message = "Hello Bob"

    nonce, ciphertext = encrypt_message(key, message)

    decrypted = decrypt_message(key, nonce, ciphertext)

    assert decrypted == message