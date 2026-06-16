import random


class ECCDemo:

    def exchange(self):

        alice_private = random.randint(1, 100)

        bob_private = random.randint(1, 100)

        generator = 5

        prime = 97

        alice_public = pow(
            generator,
            alice_private,
            prime
        )

        bob_public = pow(
            generator,
            bob_private,
            prime
        )

        alice_secret = pow(
            bob_public,
            alice_private,
            prime
        )

        bob_secret = pow(
            alice_public,
            bob_private,
            prime
        )

        return {
            "alice_public": alice_public,
            "bob_public": bob_public,
            "shared_secret": alice_secret
        }