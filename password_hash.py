#!/usr/bin/env python3
import os
import sys
import getpass
import argparse
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher(
    time_cost=3,
    memory_cost=65536,
    parallelism=4,
    hash_len=32,
    salt_len=16,
)

def get_password(prompt="Password: ") -> str:
    """Read password input and apply optional pepper from environment."""
    pepper = os.environ.get("HASH_PEPPER", "")
    return getpass.getpass(prompt) + pepper

def hash_password() -> None:
    """Hash a password and print the result."""
    print(ph.hash(get_password()))

def verify_password(stored_hash: str) -> int:
    """Verify password against a stored hash."""
    try:
        if ph.verify(stored_hash, get_password()):
            print("Password is valid.")
            return 0
    except VerifyMismatchError:
        print("Invalid password.")
    return 1

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Password Hashing CLI using Argon2id."
    )
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("hash", help="Generate a new hash")
    verify_parser = subparsers.add_parser("verify", help="Verify password against a hash")
    verify_parser.add_argument("hash", help="Stored Argon2 hash")

    args = parser.parse_args()

    if args.command == "hash":
        hash_password()
    elif args.command == "verify":
        sys.exit(verify_password(args.hash))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
