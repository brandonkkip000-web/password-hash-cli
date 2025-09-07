# 🔐 Password Hash CLI

[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/brandonkkip000-web/password-hash-cli)](https://github.com/brandonkkip000-web/password-hash-cli/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/brandonkkip000-web/password-hash-cli)](https://github.com/brandonkkip000-web/password-hash-cli)

A **minimal, professional CLI tool** for secure password hashing and verification with **Argon2id**.  

This project is for developers and sysadmins who need a simple way to hash and verify passwords without diving into cryptography internals.

---

## ✨ Features
- **Argon2id** hashing with strong defaults.
- **Two operations**: `hash` and `verify`.
- **Pepper support** via environment variable (`HASH_PEPPER`).
- **Exit codes** (`0` success, `1` failure) for automation/CI/CD.
- Lightweight & cross-platform (Windows, Linux, macOS).

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/brandonkkip000-web/password-hash-cli.git
cd password-hash-cli
pip install -r requirements.txt
🛠 Usage
1. Hash a password
bash
Copy code
python password_hash.py hash
Prompts for password input (hidden), then outputs an Argon2id hash string.

2. Verify a password
bash
Copy code
python password_hash.py verify "<stored-hash>"
Prompts for password input.

Prints Password is valid. if it matches, or Invalid password. otherwise.

Returns exit code 0 on success, 1 on failure.

3. Pepper support
For extra security, set a pepper (secret string) in an environment variable:

Linux/macOS:

bash
Copy code
export HASH_PEPPER="mysecretpepper"
Windows (PowerShell):

powershell
Copy code
setx HASH_PEPPER "mysecretpepper"
📂 Project Structure
python
Copy code
password-hash-cli/
├── password_hash.py      # Main script
├── requirements.txt      # Dependencies
├── .gitignore            # Ignore cache/venv files
├── README.md             # Documentation
└── LICENSE               # License file
🔒 Security Notes
Argon2id is OWASP-recommended for modern password storage.

Default params: time_cost=3, memory_cost=65536, parallelism=4.

Keep your pepper secret and never commit it.

Store password hashes in a secure database.

🤝 Contributing
Contributions are welcome!
Open an issue or submit a pull request to improve functionality or security.

