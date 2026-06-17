import csv
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.hashing.sha256_hash import hash_password as sha256_hash
from src.hashing.bcrypt_hash import hash_password as bcrypt_hash
from src.hashing.argon2_hash import hash_password as argon2_hash


INPUT_FILE = PROJECT_ROOT / "data" / "leaked_users.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "breached_database.csv"


def generate_hash(password: str, algorithm: str) -> str:

    algorithm = algorithm.lower()

    if algorithm == "sha256":
        return sha256_hash(password)

    elif algorithm == "bcrypt":
        return bcrypt_hash(password)

    elif algorithm == "argon2":
        return argon2_hash(password)

    raise ValueError(f"Unsupported algorithm: {algorithm}")


def simulate_breach():

    breached_records = []

    with open(INPUT_FILE, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            username = row["username"]
            password = row["password"]
            algorithm = row["algorithm"]

            hashed_password = generate_hash(
                password,
                algorithm
            )

            breached_records.append(
                {
                    "username": username,
                    "algorithm": algorithm,
                    "hash": hashed_password
                }
            )

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        fieldnames = [
            "username",
            "algorithm",
            "hash"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(
            breached_records
        )

    print(
        f"\nBreach simulation complete."
    )

    print(
        f"Generated: {OUTPUT_FILE}"
    )

    print(
        f"Records: {len(breached_records)}"
    )


if __name__ == "__main__":
    simulate_breach()