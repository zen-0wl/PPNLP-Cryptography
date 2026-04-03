from src.key_exchange import *

def test_shared_secret():
    priv1, pub1 = generate_ephemeral_keys()
    priv2, pub2 = generate_ephemeral_keys()

    s1 = compute_shared_secret(priv1, pub2)
    s2 = compute_shared_secret(priv2, pub1)

    assert s1 == s2