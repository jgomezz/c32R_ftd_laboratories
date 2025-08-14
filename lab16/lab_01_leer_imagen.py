from PIL import Image
import piexif

archivo = "mi_mascota_modificada.jpeg"
img = Image.open(archivo)
exif = piexif.load(img.info.get("exif", b""))
oculto = exif["Exif"].get(piexif.ExifIFD.UserComment, b"").decode("utf-8", "ignore")
print("Texto extraído:", oculto)
