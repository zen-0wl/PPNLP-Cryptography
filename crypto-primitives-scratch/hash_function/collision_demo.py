import random
import string

from hash_function.toy_hash import toy_hash


def random_string(length=5):
    return "".join(
        random.choice(string.ascii_uppercase)
        for _ in range(length)
    )


def main():
    print("\n===== COLLISION SEARCH =====\n")

    seen_hashes = {}

    attempts = 0

    while True:
        candidate = random_string()

        h = toy_hash(candidate)

        if h in seen_hashes:
            previous = seen_hashes[h]

            if previous != candidate:
                print("Collision Found!\n")

                print(
                    f"String A: {previous}"
                )

                print(
                    f"String B: {candidate}"
                )

                print(
                    f"Hash Value: {h}"
                )

                print(
                    f"\nAttempts Required: {attempts}"
                )

                break

        seen_hashes[h] = candidate

        attempts += 1


if __name__ == "__main__":
    main()