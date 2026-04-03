from src.identity import (
    generate_identity_keys,
    sign_data,
    verify_signature,
)


def test_signature_verification():
    private_key, public_key = generate_identity_keys()

    message = b"Hello secure world"
    signature = sign_data(private_key, message)

    assert verify_signature(public_key, message, signature) is True