# A) JPG sin perder calidad (metadatos EXIF)


from PIL import Image
import piexif, os

entrada = "demo.jpeg"     # pon tu imagen base
salida  = "mi_mascota_modificada.jpeg"

mensaje = "XYZEEFF -->   Curso: FTD | Carrera: C32R | Ciclo: 1er ciclo"

img = Image.open(entrada)

exif_data = img.info.get("Exif")

if exif_data:
    exif_dict = piexif.load(img.info.get("Exif", b""))
else :
    exif_dict = {}
    exif_dict["Exif"] = {piexif.ExifIFD.UserComment: b""}  # Initialize UserComment if not present


# Agregar mensaje a los metadatos EXIF
exif_dict["Exif"][piexif.ExifIFD.UserComment] = mensaje.encode("utf-8")

exif_bytes = piexif.dump(exif_dict)

img.save(salida, "jpeg", exif=exif_bytes, quality=95)

print("Tamaño original:", os.path.getsize(entrada))
print("Tamaño estego  :", os.path.getsize(salida))
print("OK ->", salida)


