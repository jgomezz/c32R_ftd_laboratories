import numpy as np
from scipy import stats

tiempos_entrega = [25, 30, 28, 35, 22, 32, 29, 27, 31, 26]

# Calcular la media y la desviación estándar de la muestra
media_muestra = np.mean(tiempos_entrega)
std_muestra = np.std(tiempos_entrega, ddof=1) # ddof=1 para desviación estándar muestral (n-1)
n = len(tiempos_entrega)


# Calcular el error estándar
error_estandar = std_muestra / np.sqrt(n)


# Calcular el valor t crítico para un IC del 95% y n-1 grados de libertad
# Grados de libertad = n - 1
grados_libertad = n - 1
valor_t = stats.t.ppf(0.975, grados_libertad) # 0.975 para 95% de confianza (alpha=0.05, alpha/2=0.025, 1-0.025=0.975)



# Calcular el margen de error
margen_error = valor_t * error_estandar


# Calcular el intervalo de confianza
limite_inferior = media_muestra - margen_error
limite_superior = media_muestra + margen_error


print(f"Tiempos de entrega: {tiempos_entrega}")
print(f"Media muestral: {media_muestra:.2f}")
print(f"Desviación estándar muestral: {std_muestra:.2f}")
print(f"Error estándar: {error_estandar:.2f}")
print(f"Valor t crítico (95% CI): {valor_t:.2f}")
print(f"Margen de error: {margen_error:.2f}")
print(f"Intervalo de confianza del 95% para la media: ({limite_inferior:.2f},  {limite_superior:.2f})")
