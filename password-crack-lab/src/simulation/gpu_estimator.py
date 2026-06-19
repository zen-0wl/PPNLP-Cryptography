from math import pow


PASSWORDS = [
    ("cat12", 5),
    ("football123", 11),
    ("Password2025!", 13),
]

# Simulated attacker speeds
HASH_RATES = {
    "SHA256": 10_000_000,  # 10 million/sec
    "bcrypt": 100,         # 100/sec
    "Argon2": 30           # 30/sec
}

CHARSET_SIZE = 36


def format_time(seconds):

    if seconds < 60:
        return f"{seconds:.2f} sec"

    if seconds < 3600:
        return f"{seconds/60:.2f} min"

    if seconds < 86400:
        return f"{seconds/3600:.2f} hrs"

    if seconds < 31536000:
        return f"{seconds/86400:.2f} days"

    return f"{seconds/31536000:.2f} years"


print("\n=== GPU Speed Simulation ===\n")

for password, length in PASSWORDS:

    search_space = pow(
        CHARSET_SIZE,
        length
    )

    print(f"\nPassword: {password}")
    print(
        f"Search Space: "
        f"{search_space:,.0f}"
    )

    for algorithm, rate in HASH_RATES.items():

        seconds = (
            search_space / rate
        )

        print(
            f"{algorithm:<8} "
            f"{format_time(seconds)}"
        )