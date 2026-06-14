from rsa_module.rsa import generate_keys, encrypt, decrypt


def main():
    print("\n===== RSA DEMONSTRATION =====\n")

    public_key, private_key = generate_keys()

    print(f"Public Key : {public_key}")
    print(f"Private Key: {private_key}")

    message = 65

    print(f"\nOriginal Message: {message}")

    ciphertext = encrypt(message, public_key)

    print(f"Encrypted Message: {ciphertext}")

    decrypted = decrypt(ciphertext, private_key)

    print(f"Decrypted Message: {decrypted}")

    print("\nEncryption Successful:", decrypted == message)


if __name__ == "__main__":
    main()