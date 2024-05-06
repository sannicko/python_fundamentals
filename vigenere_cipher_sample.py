def vigenere_encrypt(plain_text, key):
    cipher_text = ""
    key_index = 0
    for char in plain_text:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            key_shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                shift = (ord(char) - ord('A') + key_shift) % 26
                cipher_text += chr(ord('A') + shift)
            else:
                shift = (ord(char) - ord('a') + key_shift) % 26
                cipher_text += chr(ord('a') + shift)
            key_index += 1
        else:
            cipher_text += char
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    plain_text = ""
    key_index = 0
    for char in cipher_text:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            key_shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                shift = (ord(char) - ord('A') - key_shift) % 26
                plain_text += chr(ord('A') + shift)
            else:
                shift = (ord(char) - ord('a') - key_shift) % 26
                plain_text += chr(ord('a') + shift)
            key_index += 1
        else:
            plain_text += char
    return plain_text

# Example usage:
plain_text = "Imagination is more important than knowledge"
key = "ORCHESTRA"
encrypted_text = vigenere_encrypt(plain_text, key)
print("Encrypted:", encrypted_text)
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
