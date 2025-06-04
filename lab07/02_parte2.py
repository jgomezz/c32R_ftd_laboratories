def cifrar_cesar(texto, desplazamiento):
    """Cifra un texto utilizando el cifrado César"""
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nueva_letra = chr((ord(caracter) - base + desplazamiento) % 26 + base)
            resultado += nueva_letra
        else:
            resultado += caracter  # Mantener espacios y signos
    return resultado

def descifrar_cesar(texto_cifrado, desplazamiento):
    """Descifra un texto cifrado con el cifrado César"""
    return cifrar_cesar(texto_cifrado, -desplazamiento)

# Ejemplo de uso
mensaje_original = "Saludos de Spam MMXI"
desplazamiento = 3

mensaje_cifrado = cifrar_cesar(mensaje_original, desplazamiento)
print("Mensaje cifrado:", mensaje_cifrado)

mensaje_descifrado = descifrar_cesar(mensaje_cifrado, desplazamiento)
print("Mensaje descifrado:", mensaje_descifrado)