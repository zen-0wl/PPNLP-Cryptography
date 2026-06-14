from math import gcd
from sympy import mod_inverse


def generate_keys():
    """
    Educational RSA implementation using small primes.
    DO NOT use in real systems.
    """

    p = 61
    q = 53

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 17

    if gcd(e, phi) != 1:
        raise ValueError("e and phi(n) must be coprime")

    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


def encrypt(message: int, public_key):
    e, n = public_key
    return pow(message, e, n)


def decrypt(ciphertext: int, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)


def get_rsa_parameters():
    """
    Used later for attack demonstration.
    """
    p = 61
    q = 53

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 17
    d = mod_inverse(e, phi)

    return {
        "p": p,
        "q": q,
        "n": n,
        "phi": phi,
        "e": e,
        "d": d,
    }