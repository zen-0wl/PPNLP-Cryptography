import random
from math import gcd


class RSADemo:

    def __init__(self):
        self.p = 61
        self.q = 53

        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

        self.e = 17

        self.d = pow(self.e, -1, self.phi)

    def keygen(self):
        return {
            "public_key": [self.e, self.n],
            "private_key": [self.d, self.n]
        }

    def encrypt(self, message: int):
        ciphertext = pow(message, self.e, self.n)

        return {
            "message": message,
            "ciphertext": ciphertext
        }

    def decrypt(self, ciphertext: int):
        message = pow(ciphertext, self.d, self.n)

        return {
            "ciphertext": ciphertext,
            "message": message
        }