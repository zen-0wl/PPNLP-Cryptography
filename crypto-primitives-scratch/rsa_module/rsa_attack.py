from sympy import mod_inverse
from rsa_module.rsa import generate_keys


def factor_n(n):
    """
    Brute force factorization attack.
    Demonstrates why small RSA keys are insecure.
    """

    for i in range(2, n):
        if n % i == 0:
            return i, n // i

    return None, None


def main():
    print("\n===== RSA FACTORIZATION ATTACK =====\n")

    public_key, _ = generate_keys()

    e, n = public_key

    print(f"Public Key (e, n): {public_key}")

    print("\nAttacker only knows:")
    print(f"e = {e}")
    print(f"n = {n}")

    print("\nFactoring n...")

    p, q = factor_n(n)

    print(f"Recovered p = {p}")
    print(f"Recovered q = {q}")

    phi = (p - 1) * (q - 1)

    print(f"\nRecovered phi(n) = {phi}")

    d = mod_inverse(e, phi)

    print(f"Recovered private exponent d = {d}")

    print("\nAttacker has reconstructed the private key!")
    print(f"Private Key = ({d}, {n})")

    message = 65

    ciphertext = pow(message, e, n)

    recovered_message = pow(ciphertext, d, n)

    print(f"\nCiphertext = {ciphertext}")
    print(f"Recovered Message = {recovered_message}")

    print("\nATTACK SUCCESSFUL")


if __name__ == "__main__":
    main()