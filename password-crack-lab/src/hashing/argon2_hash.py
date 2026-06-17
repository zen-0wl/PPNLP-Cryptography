from argon2 import PasswordHasher


ph = PasswordHasher()


def hash_password(password: str) -> str:
    """
    Generate Argon2 hash.
    """
    return ph.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify Argon2 hash.
    """
    try:
        return ph.verify(
            hashed_password,
            password
        )

    except Exception:
        return False


if __name__ == "__main__":
    password = "football2024"

    hashed = hash_password(password)

    print("Password:", password)
    print("Argon2:", hashed)
    print("Verified:", verify_password(password, hashed))