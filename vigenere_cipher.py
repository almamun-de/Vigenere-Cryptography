# vigenere_cipher.py

def generate_key(message, key):
    """Extend the key to match the length of the message."""
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(plaintext, keyword):
    """Encrypt the plaintext using the Vigenère cipher."""
    key = generate_key(plaintext, keyword)
    ciphertext = []
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = (ord(plaintext[i].upper()) + ord(key[i].upper())) % 26
            cipher_char = chr(shift + ord('A'))
            if plaintext[i].islower():
                cipher_char = cipher_char.lower()
            ciphertext.append(cipher_char)
        else:
            ciphertext.append(plaintext[i])
    return "".join(ciphertext)

def decrypt_vigenere(ciphertext, keyword):
    """Decrypt the ciphertext using the Vigenère cipher."""
    key = generate_key(ciphertext, keyword)
    plaintext = []
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = (ord(ciphertext[i].upper()) - ord(key[i].upper()) + 26) % 26
            plain_char = chr(shift + ord('A'))
            if ciphertext[i].islower():
                plain_char = plain_char.lower()
            plaintext.append(plain_char)
        else:
            plaintext.append(ciphertext[i])
    return "".join(plaintext)

if __name__ == "__main__":
    # Example usage
    message = input("Enter the message: ")
    key = input("Enter the keyword: ")
    
    encrypted_message = encrypt_vigenere(message, key)
    print(f"Encrypted Message: {encrypted_message}")
    
    decrypted_message = decrypt_vigenere(encrypted_message, key)
    print(f"Decrypted Message: {decrypted_message}")
