import os
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305


def encrypt_message(key: bytes, plaintext: str, msg_id: int):
    nonce = os.urandom(12)

    payload = f"{msg_id}:{plaintext}"

    cipher = ChaCha20Poly1305(key)
    ciphertext = cipher.encrypt(
        nonce,
        payload.encode(),
        None
    )

    return nonce, ciphertext

def decrypt_message(key, nonce, ciphertext, used_ids: set):
    cipher = ChaCha20Poly1305(key)

    plaintext = cipher.decrypt(
        nonce,
        ciphertext,
        None
    ).decode()

    msg_id, message = plaintext.split(":", 1)

    msg_id = int(msg_id)

    if msg_id in used_ids:
        raise Exception("Replay attack detected")

    used_ids.add(msg_id)

    return message