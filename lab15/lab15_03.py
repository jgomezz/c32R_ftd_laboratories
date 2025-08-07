

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization


# --- EJEMPLO RESUELTO ---
print("\n--- Experimento 3: Criptografía Asimétrica (RSA) ---")


# 1. Generar un par de claves RSA (Privada y Pública)
private_key = rsa.generate_private_key(
    public_exponent=65537, # Valor común para el exponente público
    key_size=2048          # Tamaño de la clave, 2048 bits es un estándar
)
public_key = private_key.public_key()

print("Par de claves RSA generado.")

# Opcional: Guardar las claves para verlas (NO HACER EN PRODUCCIÓN ASÍ CON CLAVES PRIVADAS REALES)

# Formato PEM para la clave privada
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption() # Sin encriptar la clave privada
)
# Formato PEM para la clave pública
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print("\nClave Privada (PEM):\n", private_pem.decode())
print("\nClave Pública (PEM):\n", public_pem.decode())

# 2. Mensaje a encriptar (debe ser pequeño para RSA directamente)
# RSA se usa comúnmente para encriptar claves simétricas, no mensajes largos.
# El padding es crucial para la seguridad de RSA.
original_message = b"La proxima semana finalizan las clases de FTD"
print(f"\nMensaje Original: {original_message.decode()}")

# 3. Encriptar el mensaje con la CLAVE PÚBLICA
encrypted_message = public_key.encrypt(
    original_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(f"Mensaje Encriptado (RSA): {encrypted_message.hex()}") # Mostrar en hexadecimal


# 4. Desencriptar el mensaje con la CLAVE PRIVADA
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(f"Mensaje Desencriptado: {decrypted_message.decode()}")


# 5. Verificar
assert original_message == decrypted_message
print("¡Encriptación/Desencriptación RSA exitosa y verificada!")
