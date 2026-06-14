def toy_hash(message: str) -> int:
    """
    Educational hash function.

    Properties:
    - Deterministic
    - Fast
    - Small output space

    NOT cryptographically secure.
    """

    h = 0

    for character in message:
        h = (h * 31 + ord(character)) % 100000

    return h


def hash_hex(message: str) -> str:
    """
    Pretty hexadecimal representation.
    """

    return hex(toy_hash(message))