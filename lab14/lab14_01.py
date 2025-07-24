

import numpy as np
import statistics

ventas = [150, 200, 120, 180, 250, 100, 170]

# Media
media_ventas = statistics.mean(ventas)

print(f"Media de ventas: {media_ventas:.2f}")

sd = statistics.stdev(ventas)
print(f"Desviacion Estandar: {sd:.2f}")

