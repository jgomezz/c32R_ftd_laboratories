# AES GCM Encryption Example
# This example demonstrates symmetric encryption using AES in GCM mode with the cryptography library.
from cryptography.fernet import Fernet 

# --- EJEMPLO RESUELTO ---
print("\n--- Experimento 2: Criptografía Simétrica (AES) ---")

# 1. Generar una clave AES (debe ser compartida de forma segura)
# Fernet es una implementación de AES que maneja IVs y padding automáticamente
key = Fernet.generate_key()
f = Fernet(key)
print(f"Clave AES generada (Fernet): {key.decode()}") # Decode para mostrar como string

# 2. Mensaje a encriptar
# Nota: Fernet opera sobre bytes, por eso el 'b' antes del string
original_message = b"Este es mi mensaje secreto y confidencial para el curso de ciberseguridad."
print(f"Mensaje Original: {original_message.decode()}")

# 3. Encriptar el mensaje
encrypted_message = f.encrypt(original_message)
print(f"Mensaje Encriptado: {encrypted_message.decode()}")

# 4. Desencriptar el mensaje
# El mismo objeto Fernet (con la misma clave) se usa para desencriptar
decrypted_message = f.decrypt(encrypted_message)
print(f"Mensaje Desencriptado: {decrypted_message.decode()}")

# 5. Verificar
assert original_message == decrypted_message
print("¡Encriptación/Desencriptación AES GCM exitosa y verificada!")

# Intentar desencriptar con una clave incorrecta (demostración de seguridad)
print("\n--- Demostración: Clave Incorrecta ---")
try:
    wrong_key = Fernet.generate_key() # Una clave diferente
    f_wrong = Fernet(wrong_key)
    f_wrong.decrypt(encrypted_message)
except Exception as e:
    print(f"ERROR: No se pudo desencriptar con la clave incorrecta. Mensaje: {e}")
