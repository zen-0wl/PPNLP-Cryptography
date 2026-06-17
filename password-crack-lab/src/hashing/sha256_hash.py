import hashlib


def hash_password(password: str) -> str:
    """
    Generate SHA256 hash.
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify SHA256 hash.
    """
    return hash_password(password) == hashed_password


if __name__ == "__main__":
    password = "football2024"

    hashed = hash_password(password)

    print("Password:", password)
    print("SHA256:", hashed)
    print("Verified:", verify_password(password, hashed))