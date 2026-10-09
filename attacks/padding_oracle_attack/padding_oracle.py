
padding_oracle.py

100%
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

BLOCK_SIZE = 16
queries = 0


def encrypt_message(message, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(message, BLOCK_SIZE))


def padding_oracle(data, key):
    global queries
    queries += 1

    iv = data[:BLOCK_SIZE]
    ciphertext = data[BLOCK_SIZE:]

    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext)
        unpad(plaintext, BLOCK_SIZE)
        return True
    except ValueError:
        return False


def attack_block(previous, current, key):
    intermediate = bytearray(BLOCK_SIZE)
    plaintext = bytearray(BLOCK_SIZE)

    for i in range(BLOCK_SIZE - 1, -1, -1):
        padding = BLOCK_SIZE - i
        modified = bytearray(previous)

        for j in range(i + 1, BLOCK_SIZE):
            modified[j] = intermediate[j] ^ padding

        found = False

        for guess in range(256):
            modified[i] = guess ^ padding
            data = bytes(modified) + current

            if padding_oracle(data, key):
                if i > 0:
                    check = bytearray(modified)
                    check[i - 1] ^= 1

                    if not padding_oracle(bytes(check) + current, key):
                        continue

                intermediate[i] = guess
                plaintext[i] = guess ^ previous[i]
                found = True
                break

        if not found:
            raise Exception("Could not recover plaintext byte")

    return bytes(plaintext)


def padding_oracle_attack(iv, ciphertext, key):
    recovered = b""
    previous = iv

    for i in range(0, len(ciphertext), BLOCK_SIZE):
        current = ciphertext[i:i + BLOCK_SIZE]

        if len(current) != BLOCK_SIZE:
            raise ValueError("Ciphertext length must be a multiple of 16")

        recovered += attack_block(previous, current, key)
        previous = current

    return unpad(recovered, BLOCK_SIZE)


key = get_random_bytes(BLOCK_SIZE)
iv = get_random_bytes(BLOCK_SIZE)

message = b"Padding oracle attack demonstration"
ciphertext = encrypt_message(message, key, iv)

print("IV:", iv.hex())
print("Ciphertext:", ciphertext.hex())

queries = 0
recovered = padding_oracle_attack(iv, ciphertext, key)

print("Recovered plaintext:", recovered.decode())
print("Oracle queries:", queries)