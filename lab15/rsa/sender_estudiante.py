from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

# 1. Cargar la clave pública de B desde archivo
with open("public_key_docente.pem", "rb") as f:
    public_key_docente = serialization.load_pem_public_key(f.read())

# 2. Mensaje a cifrar
original_message = b"Entrega del laboratorio 15"
print(f"\n🔐 A (emisor) - Mensaje original: {original_message.decode()}")

# 3. Cifrar el mensaje con la clave pública de docente
encrypted_message = public_key_docente.encrypt(
    original_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# 4. Guardar mensaje cifrado como base64
with open("encrypted_message.txt", "wb") as f:
    f.write(base64.b64encode(encrypted_message))

print("\n📤 A ha cifrado y guardado el mensaje en encrypted_message.txt")
