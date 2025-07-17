
# Se desea estudiar un experimento aleatorio que consiste en realizar 200 intentos 
# de una actividad en la
# que solo pueden ocurrir dos resultados posibles: "Éxito" o "Fallo". 
# La probabilidad de obtener un "Éxito"
# en cada intento es de 0.3, mientras que la de obtener un "Fallo" es de 0.7.
# Se pide calcular la probabilidad de fallos
# Este tipo de experimento se modela como una variable aleatoria de tipo 
# Bernoulli, ya que solo hay dos posibles resultados mutuamente excluyentes.
import random

'''
intentos = random.choices(['Cara', 'Sello'], weights=[0.3, 0.7], k=100)
caras = intentos.count('Cara')
sellos = intentos.count('Sello')

print("[Preg 2] Caras:", caras)
print("[Preg 2] Sellos:", sellos)

'''
intentos = random.choices(['Éxito', 'Fallo'], weights=[0.3, 0.7], k=200)
exitos = intentos.count('Éxito')
fallos = intentos.count('Fallo')


print("[Tema 2] Éxitos:", exitos)
print("[Tema 2] Fallos:", fallos)
print("[Tema 2] Probabilidad de fallo:", fallos / 200)

# Barras de intentos
import matplotlib.pyplot as plt

plt.bar(['Éxito', 'Fallo'], [exitos, fallos], color=['green', 'red'])
plt.title("[Tema 4] Resultados de Accesos")
plt.ylabel("Cantidad")
plt.show()