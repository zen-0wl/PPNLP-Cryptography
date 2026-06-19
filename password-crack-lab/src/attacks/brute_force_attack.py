import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import itertools
import string
import time

from src.hashing.sha256_hash import hash_password


CHARSET = string.ascii_lowercase + string.digits


def brute_force(target_hash, max_length=5):

    attempts = 0

    start = time.perf_counter()

    for length in range(1, max_length + 1):

        print(f"\n[*] Trying length {length}")

        for candidate_tuple in itertools.product(
            CHARSET,
            repeat=length
        ):

            candidate = "".join(candidate_tuple)

            attempts += 1

            if hash_password(candidate) == target_hash:

                elapsed = (
                    time.perf_counter()
                    - start
                )

                return {
                    "password": candidate,
                    "attempts": attempts,
                    "time": elapsed
                }

    return None


def demo():

    password = "cat12"

    print("\n=== Brute Force Demo ===")

    print(
        f"Target Password: {password}"
    )

    target_hash = hash_password(password)

    result = brute_force(
        target_hash,
        max_length=5
    )

    if result:

        print("\n[CRACKED]")

        print(
            f"Password : {result['password']}"
        )

        print(
            f"Attempts : {result['attempts']}"
        )

        print(
            f"Time     : {result['time']:.4f}s"
        )

    else:

        print(
            "\nPassword not found."
        )


if __name__ == "__main__":
    demo()