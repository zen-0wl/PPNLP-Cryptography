from hash_function.toy_hash import toy_hash, hash_hex


def main():
    print("\n===== HASH FUNCTION DEMO =====\n")

    message = "HELLO"

    hash_value = toy_hash(message)

    print(f"Message: {message}")

    print(f"Hash (decimal): {hash_value}")
    print(f"Hash (hex): {hash_hex(message)}")

    print("\nDeterministic Test:")

    second_hash = toy_hash(message)

    print(f"First Hash : {hash_value}")
    print(f"Second Hash: {second_hash}")

    print(
        "\nSame input produces same output:",
        hash_value == second_hash,
    )

    print("\nAvalanche Demonstration:")

    modified = "HELLo"

    print(f"Original : {message}")
    print(f"Modified : {modified}")

    print(f"Original Hash : {toy_hash(message)}")
    print(f"Modified Hash : {toy_hash(modified)}")


if __name__ == "__main__":
    main()