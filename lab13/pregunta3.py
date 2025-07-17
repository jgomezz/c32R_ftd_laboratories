
import random
'''
resultado = random.randint(1, 6)

print(resultado)

lanzamientos = [random.randint(1, 6) for _ in range(200)]

print(lanzamientos)
'''

lanzamientos = [random.randint(1, 6) for _ in range(1000)]

prob_3 = lanzamientos.count(3) / 1000

print("[Tema 3] Probabilidad de obtener 3:", prob_3)

# Histograma de lanzamientos
import matplotlib.pyplot as plt


plt.hist(lanzamientos, bins=6, edgecolor='black', density=True)
plt.title("[Tema 4] Frecuencia del Dado")
plt.xlabel("Cara")
plt.ylabel("Frecuencia relativa")
plt.show()
