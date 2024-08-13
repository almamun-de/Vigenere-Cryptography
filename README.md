# Vigenere-Cryptography or # Vigenère Cipher
A Python implementation of the Vigenère cipher, including both encryption and decryption functionalities. This project demonstrates a classical polyalphabetic substitution cipher and includes a README.md file for usage instructions.

## Overview
This project provides a simple implementation of the Vigenère cipher in Python. The Vigenère cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. This project includes functions for both encryption and decryption.

## Features
- **Encryption**: Convert plaintext into ciphertext using a keyword.
- **Decryption**: Convert ciphertext back into plaintext using the same keyword.

## Files
- `vigenere_cipher.py`: The main Python script that implements the Vigenère cipher for encryption and decryption.

## Usage
### Running the Script
To use the script, you can run it directly from the command line. The script will prompt you to enter a message and a keyword for encryption and then display the encrypted message. It will also allow you to decrypt the message using the same keyword.

#### Example Usage
1. **Encrypt a Message**:
    - Run the script and enter the plaintext message and the keyword when prompted.
    - The script will output the encrypted message (ciphertext).

2. **Decrypt a Message**:
    - Run the script and enter the ciphertext and the same keyword when prompted.
    - The script will output the decrypted message (plaintext).

```bash
# Example command to run the script
python vigenere_cipher.py


## Sample Output
Enter the message: HELLO WORLD
Enter the keyword: KEY
Encrypted Message: RIJVS UYVJN
Decrypted Message: HELLO WORLD
