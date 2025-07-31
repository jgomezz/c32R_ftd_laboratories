import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# 1. Generar la población
np.random.seed(42) # para reproducibilidad
poblacion = np.random.normal(loc=170, scale=8, size=50)


Q1 = np.percentile(poblacion, 25)
Q2 = np.percentile(poblacion, 50)
Q3 = np.percentile(poblacion, 75)

print(Q1,Q2,Q3)

plt.figure(figsize=(8, 6))
sns.boxplot(y=poblacion)
plt.grid(True)
plt.show()









