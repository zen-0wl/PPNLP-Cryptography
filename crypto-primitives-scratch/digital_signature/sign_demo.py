from digital_signature.signature import (
    generate_signature_keys,
    sign_message,
    verify_signature,
)


def main():
    print("\n===== DIGITAL SIGNATURE DEMO =====\n")

    public_key, private_key = generate_signature_keys()

    message = "Transfer RM100"

    print(f"Message: {message}")

    signature = sign_message(
        message,
        private_key,
    )

    print(f"\nSignature: {signature}")

    valid = verify_signature(
        message,
        signature,
        public_key,
    )

    print(f"\nVerification Result: {valid}")

    if valid:
        print("Signature is VALID")
    else:
        print("Signature is INVALID")


if __name__ == "__main__":
    main()