from src.identity import (
    generate_identity_keys,
    sign_data,
    verify_signature
)

from src.key_exchange import (
    generate_ephemeral_keys,
    compute_shared_secret,
    derive_session_key
)

from src.crypto import (
    encrypt_message,
    decrypt_message
)


def establish_secure_session():
    # Identity keys
    alice_sign_priv, alice_sign_pub = generate_identity_keys()
    bob_sign_priv, bob_sign_pub = generate_identity_keys()

    # Ephemeral ECDH keys
    alice_ecdh_priv, alice_ecdh_pub = generate_ephemeral_keys()
    bob_ecdh_priv, bob_ecdh_pub = generate_ephemeral_keys()

    alice_pub_bytes = alice_ecdh_pub.public_bytes_raw()
    signature = sign_data(
        alice_sign_priv,
        alice_pub_bytes
    )

    verified = verify_signature(
        alice_sign_pub,
        alice_pub_bytes,
        signature
    )

    if not verified:
        raise Exception("Signature verification failed")

    alice_secret = compute_shared_secret(
        alice_ecdh_priv,
        bob_ecdh_pub
    )

    bob_secret = compute_shared_secret(
        bob_ecdh_priv,
        alice_ecdh_pub
    )

    return (
        derive_session_key(alice_secret),
        derive_session_key(bob_secret)
    )

def demo_chat():
    alice_key, bob_key = establish_secure_session()

    message = "Hello Bob, secure channel established"

    nonce, ciphertext = encrypt_message(
        alice_key,
        message
    )

    decrypted = decrypt_message(
        bob_key,
        nonce,
        ciphertext
    )

    return decrypted


def secure_chat_session():
    alice_key, bob_key = establish_secure_session()

    used_ids = set()
    msg_id = 1
    
    print("Secure chat started. Type 'exit' to quit.\n")

    while True:
        message = input("Alice: ")

        if message.lower() == "exit":
            print("Session ended securely.")
            break

        nonce, ciphertext = encrypt_message(
            alice_key,
            message,
            msg_id
        )

        try:
            decrypted = decrypt_message(
                bob_key,
                nonce,
                ciphertext,
                used_ids
            )

            print("Bob:", decrypted)

        except Exception as e:
            print("Security alert:", e)

        msg_id += 1