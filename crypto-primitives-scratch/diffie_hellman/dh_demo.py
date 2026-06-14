from diffie_hellman.dh import (
    generate_public_key,
    compute_shared_secret,
    get_demo_parameters,
)


def main():
    print("\n===== DIFFIE-HELLMAN DEMO =====\n")

    p, g, alice_private, bob_private = get_demo_parameters()

    print(f"Prime p      = {p}")
    print(f"Generator g  = {g}")

    print(f"\nAlice Private Key = {alice_private}")
    print(f"Bob Private Key   = {bob_private}")

    alice_public = generate_public_key(g, alice_private, p)
    bob_public = generate_public_key(g, bob_private, p)

    print(f"\nAlice Public Key = {alice_public}")
    print(f"Bob Public Key   = {bob_public}")

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

    print(f"\nAlice Shared Secret = {alice_shared}")
    print(f"Bob Shared Secret   = {bob_shared}")

    print(
        "\nKey Exchange Successful:",
        alice_shared == bob_shared,
    )


if __name__ == "__main__":
    main()