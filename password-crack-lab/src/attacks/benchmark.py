import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
    
import time

from src.hashing.sha256_hash import hash_password as sha256_hash
from src.hashing.bcrypt_hash import hash_password as bcrypt_hash
from src.hashing.argon2_hash import hash_password as argon2_hash

password = "football2024"

algorithms = {
    "SHA256": sha256_hash,
    "bcrypt": bcrypt_hash,
    "Argon2": argon2_hash,
}

ROUNDS = 50

print("\nHashing Benchmark\n")

for name, func in algorithms.items():

    start = time.perf_counter()

    for _ in range(ROUNDS):
        func(password)

    elapsed = time.perf_counter() - start

    avg = elapsed / ROUNDS

    print(
        f"{name:<10} "
        f"Average = {avg:.6f}s "
        f"Total = {elapsed:.3f}s"
    )