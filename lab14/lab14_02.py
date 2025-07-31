import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1. Generar la población
np.random.seed(42) # para reproducibilidad
poblacion = np.random.normal(loc=50, scale=10, size=100000)

# 2. Tomar 50 muestras de tamaño 30 y calcular sus medias
medias_muestrales = []
num_muestras = 1000
tamano_muestra = 50

for _ in range(num_muestras):
    muestra = np.random.choice(poblacion, size=tamano_muestra, replace=False)
    medias_muestrales.append(np.mean(muestra))

# print(medias_muestrales)
# 4. Calcular la media de las medias muestrales
media_de_medias_muestrales = np.mean(medias_muestrales)
print(f"Media de las medias muestrales: {media_de_medias_muestrales:.2f}")
print(f"Media de la población: {np.mean(poblacion):.2f}")


# 3. Graficar el histograma de las medias muestrales
plt.figure(figsize=(8, 6))
plt.hist(medias_muestrales, bins=40, edgecolor='black', alpha=0.7)
plt.title('Histograma de las Medias Muestrales')
plt.xlabel('Media Muestral')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.75)
plt.show()

