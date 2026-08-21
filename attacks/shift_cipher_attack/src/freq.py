from collections import Counter


def shift_decrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base - key) % 26 + base)
        else:
            result += ch

    return result


cipher = input("Enter ciphertext: ")

# Count frequency of letters
letters = [ch.upper() for ch in cipher if ch.isalpha()]
frequency = Counter(letters)

print("Letter frequencies:")
print(frequency)

# Most frequent letter
most_common = frequency.most_common(1)[0][0]

print("Most frequent letter:", most_common)

# Assume most frequent letter is E
key = (ord(most_common) - ord('E')) % 26

print("Guessed key:", key)

# Decrypt
plaintext = shift_decrypt(cipher, key)

print("Decrypted text:", plaintext)
