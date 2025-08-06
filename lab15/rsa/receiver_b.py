from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

# 1. Cargar la clave privada de B desde archivo
with open("private_key_b.pem", "rb") as f:
    private_key_b = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

# 2. Leer el mensaje cifrado
with open("encrypted_message.txt", "rb") as f:
    encrypted_message = base64.b64decode(f.read())

# 3. Descifrar el mensaje
decrypted_message = private_key_b.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(f"\n✅ B (receptor) - Mensaje descifrado: {decrypted_message.decode()}")
