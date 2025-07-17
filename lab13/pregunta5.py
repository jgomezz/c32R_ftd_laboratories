usuarios = ["user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8", "user9", "user10"]
registro = [
   ("user1", "Fallo"), ("user1", "Fallo"), ("user1", "Fallo"),
   ("user2", "Éxito"), ("user2", "Fallo"), ("user3", "Fallo"),
   ("user3", "Fallo"), ("user4", "Éxito"), ("user5", "Fallo"),
   ("user5", "Fallo"), ("user5", "Fallo"), ("user5", "Fallo"),
   ("user6", "Éxito"), ("user7", "Fallo"), ("user8", "Fallo"),
   ("user8", "Fallo"), ("user9", "Éxito"), ("user10", "Fallo"),
   ("user10", "Fallo"), ("user10", "Fallo"), ("user10", "Fallo"),
   ("user10", "Fallo"), ("user10", "Fallo"), ("user10", "Fallo"),
]
# Contar fallos por usuario
conteo_fallos = {}
for usuario, resultado in registro:
   if resultado == "Fallo":
       conteo_fallos[usuario] = conteo_fallos.get(usuario, 0) + 1


usuarios_sospechosos = [u    for u, c in conteo_fallos.items() if c > 5]

print("[Tema 5] Usuarios con más de 3 fallos:", usuarios_sospechosos)
print("[Tema 5] Total de usuarios sospechosos:", len(usuarios_sospechosos))