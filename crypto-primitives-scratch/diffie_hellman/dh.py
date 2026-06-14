def generate_public_key(g, private_key, p):
    """
    Computes public key:
    A = g^a mod p
    """
    return pow(g, private_key, p)


def compute_shared_secret(other_public_key, private_key, p):
    """
    Computes shared secret:
    S = B^a mod p
    """
    return pow(other_public_key, private_key, p)


def get_demo_parameters():
    """
    Small values for educational demonstration.
    DO NOT USE IN REAL SYSTEMS.
    """

    p = 23
    g = 5

    alice_private = 6
    bob_private = 15

    return p, g, alice_private, bob_private