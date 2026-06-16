import numpy as np


class LWE:

    def __init__(self, n=4, q=97):
        self.n = n
        self.q = q

    def keygen(self):
        A = np.random.randint(0, self.q, (self.n, self.n))

        s = np.random.randint(0, self.q, self.n)

        e = np.random.randint(-1, 2, self.n)

        b = (A @ s + e) % self.q

        return {
            "A": A.tolist(),
            "b": b.tolist(),
            "s": s.tolist(),
            "e": e.tolist()
        }

    def encrypt(self, message: int):

        ciphertext = (message + 42) % self.q

        return {
            "message": message,
            "ciphertext": ciphertext
        }

    def decrypt(self, ciphertext: int):

        message = (ciphertext - 42) % self.q

        return {
            "ciphertext": ciphertext,
            "message": message
        }