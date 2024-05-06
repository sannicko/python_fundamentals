def affine_encrypt_message(message: str, keyset: tuple) -> str:
    # Define the alphabet with indices
    alphabet = "abcdefghijklmnopqrstuvwxyz ,."
    
    # Unpack the keyset
    a, b = keyset
    
    # Initialize an empty string to store the encrypted message
    encrypted_message = ""
    
    # Iterate over each character in the message
    for char in message:
        # Check if the character is in the alphabet
        if char in alphabet:
            # Find the index of the character in the alphabet
            char_index = alphabet.index(char)
            
            # Apply the encryption formula: (a * char_index + b) mod 29
            encrypted_index = (a * char_index + b) % 29
            
            # Append the encrypted character to the encrypted message
            encrypted_message += alphabet[encrypted_index]
        else:
            # If the character is not in the alphabet, append it unchanged
            encrypted_message += char
    
    # Return the encrypted message
    return encrypted_message

# Encrypt the message "hello world." using the keyset (a=2, b=3)
encrypted_message = affine_encrypt_message("hello world.", (2, 3))
print("Encrypted Message:", encrypted_message)

