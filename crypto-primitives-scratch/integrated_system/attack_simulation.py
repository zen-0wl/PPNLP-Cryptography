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
    print("\n===== ATTACK SIMULATION =====\n")

    # ---------------------------
    # Key Exchange
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

    shared_key = compute_shared_secret(
        bob_public,
        alice_private,
        p,
    )

    print("Shared Secret Established")
    print(f"Shared Key: {shared_key}")

    # ---------------------------
    # Alice Creates Message
    # ---------------------------

    public_key, private_key = generate_signature_keys()

    original_message = "Transfer RM100"

    signature = sign_message(
        original_message,
        private_key,
    )

    print("\n=== ORIGINAL TRANSMISSION ===")
    print(f"Message: {original_message}")
    print(f"Signature: {signature}")

    # ---------------------------
    # Mallory Attacks
    # ---------------------------

    forged_message = "Transfer RM1000"

    print("\n=== ATTACKER MODIFIES MESSAGE ===")
    print(f"Modified Message: {forged_message}")

    # ---------------------------
    # Bob Verifies
    # ---------------------------

    print("\n=== RECEIVER VERIFICATION ===")

    valid = verify_signature(
        forged_message,
        signature,
        public_key,
    )

    if valid:
        print("Forgery Successful")
        print("Security Failure")
    else:
        print("Signature Verification Failed")
        print("Tampering Detected")
        print("Message Rejected")


if __name__ == "__main__":
    main()