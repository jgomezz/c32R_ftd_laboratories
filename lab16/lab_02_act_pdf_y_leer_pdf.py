

from cryptography.fernet import Fernet
import base64


# Generar clave
key = Fernet.generate_key()
fernet = Fernet(key)
# Mensaje personalizado
mensaje = "Mensaje deseado"
mensaje_bytes = mensaje.encode()
# Cifrar
mensaje_cifrado = fernet.encrypt(mensaje_bytes)


from PyPDF2 import PdfReader, PdfWriter


reader = PdfReader("portada.pdf")
writer = PdfWriter()


for page in reader.pages:
    writer.add_page(page)


writer.add_metadata({
    "/Title": "Documento Esteganografiado",
    "/Secret": mensaje_cifrado.decode()
})


with open("portada_oculta.pdf", "wb") as f:
    writer.write(f)

