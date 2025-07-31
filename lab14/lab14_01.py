

import numpy as np
import statistics as stat

ventas = [150, 200, 120, 180, 250, 100, 170]

# Media
media_ventas = stat.mean(ventas)

print(f"Media de ventas: {media_ventas:.2f}")

sd = stat.stdev(ventas)
print(f"Desviacion Estandar: {sd:.2f}")

# Rango
rango_ventas = max(ventas) - min(ventas)
print(f"Rango de ventas: {rango_ventas:.2f}")
