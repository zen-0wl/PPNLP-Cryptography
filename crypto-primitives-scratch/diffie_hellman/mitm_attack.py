from diffie_hellman.dh import (
    generate_public_key,
    compute_shared_secret,
)


def main():
    print("\n===== MAN-IN-THE-MIDDLE ATTACK =====\n")

    p = 23
    g = 5

    alice_private = 6
    bob_private = 15

    mallory_private_a = 7
    mallory_private_b = 11

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

    mallory_public_a = generate_public_key(
        g,
        mallory_private_a,
        p,
    )

    mallory_public_b = generate_public_key(
        g,
        mallory_private_b,
        p,
    )

    print("Alice sends public key to Bob...")
    print("Mallory intercepts it.")

    print("\nBob sends public key to Alice...")
    print("Mallory intercepts it.")

    alice_shared = compute_shared_secret(
        mallory_public_b,
        alice_private,
        p,
    )

    bob_shared = compute_shared_secret(
        mallory_public_a,
        bob_private,
        p,
    )

    mallory_with_alice = compute_shared_secret(
        alice_public,
        mallory_private_b,
        p,
    )

    mallory_with_bob = compute_shared_secret(
        bob_public,
        mallory_private_a,
        p,
    )

    print("\n===== RESULTS =====\n")

    print("\nAlice ↔ Mallory Shared Key")
    print(alice_shared)

    print("\nMallory ↔ Bob Shared Key")
    print(bob_shared)

    print("\nSecurity Observation:")
    print(
        "Alice and Bob do NOT share the same key."
    )
    print(
        "Mallory established independent keys with both parties."
    )


if __name__ == "__main__":
    main()