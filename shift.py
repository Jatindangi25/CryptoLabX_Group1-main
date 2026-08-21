def shift_encrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            result += ch

    return result


def shift_decrypt(text, key):
    return shift_encrypt(text, -key)


text = input("Enter plaintext: ")
key = int(input("Enter key: "))

cipher = shift_encrypt(text, key)
print("Encrypted text:", cipher)

plain = shift_decrypt(cipher, key)
print("Decrypted text:", plain)
