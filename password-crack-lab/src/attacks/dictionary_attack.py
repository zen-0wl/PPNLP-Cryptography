import csv
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hashing.sha256_hash import (
    hash_password as sha256_hash
)


BREACHED_DB = (
    PROJECT_ROOT
    / "data"
    / "breached_database.csv"
)

WORDLIST = (
    PROJECT_ROOT
    / "data"
    / "passwords.txt"
)


def load_wordlist():

    with open(
        WORDLIST,
        "r",
        encoding="utf-8"
    ) as file:

        return [
            line.strip()
            for line in file
            if line.strip()
        ]


def load_sha256_targets():

    targets = []

    with open(
        BREACHED_DB,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["algorithm"] == "sha256":

                targets.append(
                    {
                        "username": row["username"],
                        "hash": row["hash"]
                    }
                )

    return targets


def dictionary_attack():

    print("\n=== Dictionary Attack ===\n")

    wordlist = load_wordlist()

    targets = load_sha256_targets()

    attempts = 0
    cracked = []

    start = time.perf_counter()

    for target in targets:

        username = target["username"]
        target_hash = target["hash"]

        found = False

        for candidate in wordlist:

            attempts += 1

            if sha256_hash(candidate) == target_hash:

                cracked.append(
                    {
                        "username": username,
                        "password": candidate
                    }
                )

                print(
                    f"[CRACKED] "
                    f"{username:<12} "
                    f"-> {candidate}"
                )

                found = True
                break

        if not found:

            print(
                f"[FAILED] "
                f"{username}"
            )

    elapsed = (
        time.perf_counter()
        - start
    )
    
    success_rate = (len(cracked) / len(targets)) * 100

    print("\n=== Summary ===")

    print(
        f"Targets: {len(targets)}"
    )

    print(
        f"Cracked: {len(cracked)}"
    )

    print(
        f"Attempts: {attempts}"
    )

    print(
        f"Time: {elapsed:.4f}s"
    )
    
    print(
        f"Success Rate: {success_rate:.1f}%"
    )

if __name__ == "__main__":
    dictionary_attack()