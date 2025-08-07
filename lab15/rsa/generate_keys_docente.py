from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generar par de claves
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
)

# Guardar clave privada
with open("private_key_docente.pem", "wb") as f:
    f.write(private_pem)


public_key = private_key.public_key()

public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

# Guardar clave pública
with open("public_key_docente.pem", "wb") as f:
    f.write(public_pem)


print("🔐 Claves del docente generadas y guardadas.")
