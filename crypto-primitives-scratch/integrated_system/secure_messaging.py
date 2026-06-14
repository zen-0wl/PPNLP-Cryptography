from diffie_hellman.dh import (
    generate_public_key,
    compute_shared_secret,
)

from digital_signature.signature import (
    generate_signature_keys,
    sign_message,
    verify_signature,
)


def main():
    print("\n===== SECURE MESSAGING SIMULATION =====\n")

    # ---------------------------
    # Diffie-Hellman Key Exchange
    # ---------------------------

    p = 23
    g = 5

    alice_private = 6
    bob_private = 15

    alice_public = generate_public_key(
        g,
        alice_private,
        p,
    )

    bob_public = generate_public_key(
        g,
        bob_private,
        p,
    )

    alice_shared = compute_shared_secret(
        bob_public,
        alice_private,
        p,
    )

    bob_shared = compute_shared_secret(
        alice_public,
        bob_private,
        p,
    )

    print("=== KEY EXCHANGE ===")
    print(f"Alice Shared Secret: {alice_shared}")
    print(f"Bob Shared Secret:   {bob_shared}")

    if alice_shared == bob_shared:
        print("Shared secret established.\n")

    # ---------------------------
    # Digital Signature
    # ---------------------------

    public_key, private_key = generate_signature_keys()

    message = "Hello Bob"

    print("=== MESSAGE CREATION ===")
    print(f"Message: {message}")

    signature = sign_message(
        message,
        private_key,
    )

    print(f"Signature: {signature}")

    # ---------------------------
    # Bob receives message
    # ---------------------------

    print("\n=== RECEIVER VERIFICATION ===")

    valid = verify_signature(
        message,
        signature,
        public_key,
    )

    if valid:
        print("Signature Verified")
        print("Message Accepted")
    else:
        print("Verification Failed")
        print("Message Rejected")


if __name__ == "__main__":
    main()