from rsa_module.rsa import generate_keys
from hash_function.toy_hash import toy_hash


def sign_message(message: str, private_key):
    d, n = private_key

    # RSA works modulo n
    message_hash = toy_hash(message) % n

    signature = pow(message_hash, d, n)

    return signature


def verify_signature(
    message: str,
    signature: int,
    public_key,
):
    e, n = public_key

    expected_hash = toy_hash(message) % n

    recovered_hash = pow(signature, e, n)

    return expected_hash == recovered_hash


def generate_signature_keys():
    return generate_keys()