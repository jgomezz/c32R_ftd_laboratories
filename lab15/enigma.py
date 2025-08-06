import string

# Abecedario y un rotor de sustitución ficticio (solo un ejemplo)
alphabet = string.ascii_uppercase
rotor = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"  # Rotor I de Enigma real

def enigma_encrypt(message, rotor_offset=0):
    encrypted = ""
    for char in message.upper():
        if char in alphabet:
            # Ajustar por la posición del rotor
            index = (alphabet.index(char) + rotor_offset) % 26
            substituted = rotor[index]
            encrypted += substituted
            # Simular rotación del rotor: se incrementa en cada letra
            rotor_offset = (rotor_offset + 1) % 26
        else:
            encrypted += char  # Mantener espacios y signos
    return encrypted

def enigma_decrypt(encrypted, rotor_offset=0):
    decrypted = ""
    for char in encrypted.upper():
        if char in rotor:
            index = (rotor.index(char) - rotor_offset) % 26
            original = alphabet[index]
            decrypted += original
            rotor_offset = (rotor_offset + 1) % 26
        else:
            decrypted += char
    return decrypted

# Mensaje a cifrar
mensaje = "HOLA MUNDO"
cifrado = enigma_encrypt(mensaje)
descifrado = enigma_decrypt(cifrado)

print(f"Mensaje original:  {mensaje}")
print(f"Mensaje cifrado:   {cifrado}")
print(f"Mensaje descifrado: {descifrado}")
