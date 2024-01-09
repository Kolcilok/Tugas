import random


def generate_adfgvx_key():
    alphabet = "ADFGVX"
    key = [c1 + c2 for c1 in alphabet for c2 in alphabet]
    random.shuffle(key)
    return key


def encrypt(message, key):
    adfgvx = "ADFGVX"
    encrypted_message = ""

    for char in message:
        if char.isalpha():
            char = char.upper()
            index = key.index(char)
            row = adfgvx[index // 6]
            col = adfgvx[index % 6]
            encrypted_message += row + col

    return encrypted_message


def decrypt(encrypted_message, key):
    adfgvx = "ADFGVX"
    decrypted_message = ""

    for i in range(0, len(encrypted_message), 2):
        row, col = encrypted_message[i], encrypted_message[i + 1]
        index = adfgvx.index(row) * 6 + adfgvx.index(col)
        decrypted_message += key[index]

    return decrypted_message


# Contoh penggunaan
message = "HELLO"
key = generate_adfgvx_key()

encrypted_message = encrypt(message, key)
print("Enkripsi:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Dekripsi:", decrypted_message)
