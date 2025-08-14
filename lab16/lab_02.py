from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("portada.pdf", pagesize=A4)
c.setFont("Helvetica-Bold", 28)
c.drawString(72, 780, "Tu Nombre")
c.setFont("Helvetica", 14)
c.drawString(72, 750, "Portada Esteganografía PDF")
c.showPage()
c.save()
print("portada.pdf listo")


from cryptography.fernet import Fernet
import base64


# Generar clave
key = Fernet.generate_key()
fernet = Fernet(key)
# Mensaje personalizado
mensaje = "Soy xxxx xxxxx, estudiante de xxxxxx, Refran secreto: xxxx"
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



from PyPDF2 import PdfReader
from cryptography.fernet import Fernet


reader = PdfReader("portada_oculta.pdf")
metadata = reader.metadata
mensaje_cifrado = metadata.get("/Secret")

'''
# Leer clave
with open("clave.key", "rb") as f:
    key = f.read()
'''

fernet = Fernet(key)
mensaje_descifrado = fernet.decrypt(mensaje_cifrado.encode()).decode()


print("Mensaje recuperado:", mensaje_descifrado)

