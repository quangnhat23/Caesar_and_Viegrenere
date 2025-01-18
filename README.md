This project is a Python implementation of two famous classical encryption techniques, namely Caesar Cipher and Vigenère Cipher. These ciphers provide ways of encrypting and decrypting texts based on substitution techniques.

Features
Caesar Cipher
Encrypt the plaintext using a fixed shift.
Decrypt the ciphertext using the same shift.
Vigenère Cipher
Encrypt the plaintext using a keyword-based repeating shift.
Decrypt the ciphertext using the same keyword.
How It Works
Caesar Cipher
The Caesar Cipher shifts every letter of the plaintext by a fixed number of positions in the alphabet. Example:

Plaintext: HELLO
Shift: 3
Ciphertext: KHOOR
Vigenère Cipher
The Vigenère Cipher uses a keyword to determine the shift for each letter. Each letter in the keyword corresponds to a shift value. Example:

Plaintext: HELLO
Keyword: KEY
Ciphertext: RIJVS
