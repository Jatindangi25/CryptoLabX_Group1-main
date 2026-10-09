# Padding Oracle Attack on AES-CBC

## Aim
To understand and demonstrate how a Padding Oracle Attack can recover plaintext from AES-CBC ciphertext without knowing the AES key.

## 1. Introduction
AES-CBC is a block cipher mode that encrypts data in blocks of 16 bytes. If the plaintext is not a multiple of 16 bytes, PKCS#7 padding is added.

A Padding Oracle is a function that tells whether decrypted ciphertext has valid padding. An attacker can exploit this information to recover plaintext without directly accessing the AES key.

## 2. Requirements
- Python 3
- PyCryptodome library

Install the library:

```bash
pip install pycryptodome
