
This project implements a Shift Cipher and demonstrates basic cryptanalysis techniques using Frequency Analysis and the Chi-Square Test.

Features
Encrypt text using a Shift/Caesar Cipher.
Decrypt ciphertext using a given shift key.
Calculate the frequency of letters in ciphertext.
Apply the Chi-Square Test to compare observed frequencies with expected English frequencies.
Identify the most probable shift based on the lowest Chi-Square value.
Working

The Shift Cipher shifts each alphabetic character by a fixed number of positions.

Encryption: C = (P + K) mod 26
Decryption: P = (C - K) mod 26

Frequency analysis counts the occurrence of each letter, while the Chi-Square Test determines which possible shift produces a frequency distribution closest to standard English.

Technologies
Python
Git & GitHub
Conclusion

The project demonstrates how a simple Shift Cipher can be broken using statistical techniques. It shows the importance of frequency analysis and Chi-Square testing in classical cryptanalysis.
