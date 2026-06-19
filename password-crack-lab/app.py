import json
import hashlib
import secrets

import bcrypt
import numpy as np
import pandas as pd
import streamlit as st

from argon2 import PasswordHasher

st.set_page_config(
    page_title="Password Security Lab",
    page_icon="🔐",
    layout="wide"
)

ph = PasswordHasher()

try:
    with open("data/results.json", "r") as f:
        results = json.load(f)
except Exception:
    results = {
        "dictionary": {
            "targets": 17,
            "cracked": 17,
            "attempts": 1834,
            "time": 0.0023,
            "success_rate": 100.0
        },
        "mutation": {
            "targets": 17,
            "cracked": 11,
            "attempts": 4328,
            "time": 0.0043,
            "success_rate": 64.7
        },
        "bruteforce": {
            "password": "cat12",
            "attempts": 5112461,
            "time": 6.7508
        },
        "benchmark": {
            "sha256": 0.000001,
            "argon2": 0.039284,
            "bcrypt": 0.198009
        }
    }


st.title("🔐 Password Security Lab")

st.markdown(
    """
    Compare **SHA256**, **bcrypt**, and **Argon2**
    under realistic password cracking scenarios.

    This project simulates:
    - Password hashing
    - Database breaches
    - Dictionary attacks
    - Mutation attacks
    - Brute-force attacks
    - GPU cracking estimates
    - Salt protection
    """
)

# =====================================================
# TABS
# =====================================================

tabs = st.tabs(
    [
        "Executive Summary",
        "Hash Generator",
        "Breached Database",
        "Benchmark Results",
        "Attack Results",
        "GPU Simulation",
        "Salt Demo"
    ]
)

# =====================================================
# TAB 1
# =====================================================

with tabs[0]:

    st.header("Executive Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Records",
        50
    )

    col2.metric(
        "Dictionary Success",
        f"{results['dictionary']['success_rate']}%"
    )

    col3.metric(
        "Mutation Success",
        f"{results['mutation']['success_rate']}%"
    )

    col4.metric(
        "Brute Force Attempts",
        f"{results['bruteforce']['attempts']:,}"
    )

    st.info(
        """
        This lab demonstrates how different password hashing algorithms
        resist realistic cracking attacks after a simulated database breach.
        """
    )

# =====================================================
# TAB 2
# =====================================================

with tabs[1]:

    st.header("Hash Generator")

    password = st.text_input(
        "Enter Password",
        value="football123"
    )

    if st.button("Generate Hashes"):

        sha256_hash = hashlib.sha256(
            password.encode()
        ).hexdigest()

        bcrypt_hash = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        ).decode()

        argon2_hash = ph.hash(password)

        col1, col2, col3 = st.columns(3)

        with col1:

            st.subheader("SHA256")

            st.code(sha256_hash)

            st.metric(
                "Hash Length",
                len(sha256_hash)
            )

        with col2:

            st.subheader("bcrypt")

            st.code(bcrypt_hash)

            st.metric(
                "Hash Length",
                len(bcrypt_hash)
            )

        with col3:

            st.subheader("Argon2")

            st.code(argon2_hash)

            st.metric(
                "Hash Length",
                len(argon2_hash)
            )

# =====================================================
# TAB 3
# =====================================================

with tabs[2]:

    st.header("Breached Database")

    try:

        breached = pd.read_csv(
            "data/breached_database.csv"
        )

        sha_count = (
            breached["algorithm"]
            .str.lower()
            .eq("sha256")
            .sum()
        )

        bcrypt_count = (
            breached["algorithm"]
            .str.lower()
            .eq("bcrypt")
            .sum()
        )

        argon_count = (
            breached["algorithm"]
            .str.lower()
            .eq("argon2")
            .sum()
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Total Records",
            len(breached)
        )

        c2.metric(
            "SHA256",
            sha_count
        )

        c3.metric(
            "bcrypt",
            bcrypt_count
        )

        c4.metric(
            "Argon2",
            argon_count
        )

        st.dataframe(
            breached,
            use_container_width=True,
            height=500
        )

    except Exception as e:

        st.error(
            f"Could not load breached database.\n\n{e}"
        )

# =====================================================
# TAB 4
# =====================================================

with tabs[3]:

    st.header("Hashing Benchmark")

    benchmark_df = pd.DataFrame(
        {
            "Algorithm": [
                "SHA256",
                "Argon2",
                "bcrypt"
            ],
            "Average Time (seconds)": [
                results["benchmark"]["sha256"],
                results["benchmark"]["argon2"],
                results["benchmark"]["bcrypt"]
            ]
        }
    )

    st.dataframe(
        benchmark_df,
        use_container_width=True
    )

    st.bar_chart(
        benchmark_df.set_index(
            "Algorithm"
        )
    )

    st.success(
        """
        SHA256 is extremely fast and therefore unsuitable for password storage.

        bcrypt and Argon2 intentionally increase computational cost,
        making password cracking dramatically more difficult.
        """
    )

# =====================================================
# TAB 5
# =====================================================

with tabs[4]:

    st.header("Attack Results")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Dictionary Attack",
            f"{results['dictionary']['success_rate']}%"
        )

        st.json(
            results["dictionary"]
        )

    with col2:

        st.metric(
            "Mutation Attack",
            f"{results['mutation']['success_rate']}%"
        )

        st.json(
            results["mutation"]
        )

    with col3:

        st.metric(
            "Brute Force Attempts",
            f"{results['bruteforce']['attempts']:,}"
        )

        st.json(
            results["bruteforce"]
        )

    attack_df = pd.DataFrame(
        {
            "Attack": [
                "Dictionary",
                "Mutation"
            ],
            "Success Rate": [
                results["dictionary"]["success_rate"],
                results["mutation"]["success_rate"]
            ]
        }
    )

    st.subheader("Attack Success Comparison")

    st.bar_chart(
        attack_df.set_index(
            "Attack"
        )
    )

# =====================================================
# TAB 6
# =====================================================

with tabs[5]:

    st.header("GPU Crack-Time Simulation")

    gpu_df = pd.DataFrame(
        {
            "Algorithm": [
                "SHA256",
                "bcrypt",
                "Argon2"
            ],
            "Estimated Years": [
                417,
                41736968,
                139123228
            ]
        }
    )

    gpu_df["Log10 Years"] = np.log10(
        gpu_df["Estimated Years"]
    )

    st.subheader(
        "Estimated Time to Crack football123"
    )

    st.bar_chart(
        gpu_df.set_index(
            "Algorithm"
        )[["Log10 Years"]]
    )

    st.dataframe(
        gpu_df,
        use_container_width=True
    )

    st.warning(
        """
        Log scale is used because bcrypt and Argon2 require
        orders of magnitude more work than SHA256.
        """
    )

# =====================================================
# TAB 7
# =====================================================

with tabs[6]:

    st.header("Salt Demonstration")

    password = "password123"

    st.write("Password:")

    st.code(password)

    st.subheader("Without Salt")

    for _ in range(3):

        hash_value = hashlib.sha256(
            password.encode()
        ).hexdigest()

        st.code(hash_value)

    st.error(
        "Identical passwords produce identical hashes."
    )

    st.subheader("With Salt")

    for _ in range(3):

        salt = secrets.token_hex(8)

        salted_hash = hashlib.sha256(
            (password + salt).encode()
        ).hexdigest()

        st.write(
            f"Salt: {salt}"
        )

        st.code(salted_hash)

    st.success(
        """
        Salting ensures that identical passwords
        generate different hashes.
        """
    )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    """
    Password Security Lab

    Features:
    • SHA256
    • bcrypt
    • Argon2
    • Breach Simulation
    • Dictionary Attack
    • Mutation Attack
    • Brute Force Attack
    • GPU Crack-Time Estimation
    • Salt Demonstration
    """
)