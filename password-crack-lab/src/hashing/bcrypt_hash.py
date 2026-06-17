import bcrypt


def hash_password(password: str) -> str:
    """
    Generate bcrypt hash.
    """
    salt = bcrypt.gensalt(rounds=12)

    hashed = bcrypt.hashpw(
        password.encode("utf-8"),
        salt
    )

    return hashed.decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify bcrypt hash.
    """
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


if __name__ == "__main__":
    password = "football2024"

    hashed = hash_password(password)

    print("Password:", password)
    print("bcrypt:", hashed)
    print("Verified:", verify_password(password, hashed))