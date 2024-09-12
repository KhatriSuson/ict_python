def caeser_cipher(text, shift, mode ='encrypt'):
    result = ""

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)

        elif char.islower():
           result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result
encrypted_text = caeser_cipher("hello", 3, mode='encrypt')
decrypted_text = caeser_cipher(encrypted_text, 3, mode='decrypt')

print(f"Encrypted_text : {encrypted_text}")
print(f"Decrypted_text: {decrypted_text}")