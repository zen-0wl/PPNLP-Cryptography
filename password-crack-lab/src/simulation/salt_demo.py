import hashlib
import secrets


PASSWORD = "password123"


def sha256_hash(text):

    return hashlib.sha256(
        text.encode()
    ).hexdigest()


print("\n=== Salt Demonstration ===\n")

print("PASSWORD:")
print(PASSWORD)

print("\nWITHOUT SALT")

for i in range(3):

    hash_value = sha256_hash(
        PASSWORD
    )

    print(
        f"{i+1}: {hash_value}"
    )

print("\nWITH RANDOM SALT")

for i in range(3):

    salt = secrets.token_hex(8)

    hash_value = sha256_hash(
        PASSWORD + salt
    )

    print(
        f"{i+1}: "
        f"{hash_value}"
    )

    print(
        f"   Salt: {salt}"
    )