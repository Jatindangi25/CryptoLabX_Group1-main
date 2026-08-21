from collections import Counter

# Expected English letter frequencies
english_freq = [
    8.167, 1.492, 2.782, 4.253, 12.702,
    2.228, 2.015, 6.094, 6.966, 0.153,
    0.772, 4.025, 2.406, 6.749, 7.507,
    1.929, 0.095, 5.987, 6.327, 9.056,
    2.758, 0.978, 2.360, 0.150, 1.974,
    0.074
]


def decrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base - key) % 26 + base)
        else:
            result += ch

    return result


def chi_square(text):
    letters = [ch.upper() for ch in text if ch.isalpha()]
    total = len(letters)

    if total == 0:
        return float('inf')

    count = Counter(letters)

    chi = 0

    for i in range(26):
        letter = chr(ord('A') + i)

        observed = count.get(letter, 0)
        expected = english_freq[i] * total / 100

        chi += (observed - expected) ** 2 / expected

    return chi


cipher = input("Enter ciphertext: ")

best_key = 0
best_score = float('inf')
best_text = ""

# Try all 26 possible keys
for key in range(26):

    plaintext = decrypt(cipher, key)

    score = chi_square(plaintext)

    print("Key:", key, "Chi-square:", round(score, 2))

    if score < best_score:
        best_score = score
        best_key = key
        best_text = plaintext


print("\nBest key:", best_key)
print("Decrypted text:", best_text)
print("Chi-square value:", round(best_score, 2))
