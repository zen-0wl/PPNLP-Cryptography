from digital_signature.signature import (
    generate_signature_keys,
    sign_message,
    verify_signature,
)


def main():
    print("\n===== MESSAGE TAMPERING ATTACK =====\n")

    public_key, private_key = generate_signature_keys()

    original_message = "Transfer RM100"

    signature = sign_message(
        original_message,
        private_key,
    )

    print(f"Original Message: {original_message}")
    print(f"Signature: {signature}")

    print("\n--- Attacker Modifies Message ---\n")

    forged_message = "Transfer RM1000"

    print(f"Modified Message: {forged_message}")

    result = verify_signature(
        forged_message,
        signature,
        public_key,
    )

    print(f"\nVerification Result: {result}")

    if not result:
        print(
            "Tampering Detected!"
        )
    else:
        print(
            "Forgery Successful (unexpected)"
        )


if __name__ == "__main__":
    main()