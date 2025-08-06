

def encrypt_caesar(text, shift):
    
    """
    Cifra un texto usando el Cifrado César.
    text: str, el mensaje a cifrar.
    shift: int, el número de posiciones a desplazar.
    """
    result = ""
    for char in text:
        if char.isalpha(): # Solo ciframos letras del alfabeto
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            result += char # Mantener caracteres no alfabéticos tal cual
    return result


def decrypt_caesar(text, shift):
    """
    Descifra un texto cifrado con el Cifrado César.
    text: str, el mensaje cifrado.
    shift: int, el número de posiciones de desplazamiento original.
    """
    # Desencriptar es lo mismo que encriptar con un desplazamiento negativo
    return encrypt_caesar(text, -shift)



import sys

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Uso: python lab15_01.py <mensaje> <clave_desplazamiento>")
        sys.exit(1)


    message = sys.argv[1]
    shift_key = int(sys.argv[2])

    # --- EJEMPLO RESUELTO ---
    print("--- Experimento 1: Cifrado César ---") 

    #message = "HoLA MUNDO"
    #shift_key = 3

    # Encriptar
    encrypted_message = encrypt_caesar(message, shift_key)
    print(f"Mensaje Original: {message}")
    print(f"Clave de Desplazamiento: {shift_key}")
    print(f"Mensaje Encriptado: {encrypted_message}")

    # Desencriptar
    decrypted_message = decrypt_caesar(encrypted_message, shift_key)
    print(f"Mensaje Desencriptado: {decrypted_message}")

    # Verificar si la desencriptación fue correcta
    assert message == decrypted_message
    print("¡Desencriptación exitosa y verificada!")
