#############################
#############################
####### Ejercicio 01 ########
#############################
#############################
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

# Definir la funcion: f(x) = x-1 = y
def funcion_1(x):
	return x-1

y = funcion_1(x)

# Graficar
plt.figure(figsize=(8,5))
plt.plot(x, y, label="$f(x) = x - 1$", color="blue")
plt.title("Grafica de f(x) = x - 1", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("f(x)", fontsize=14)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.grid(alpha=0.4)
plt.legend(fontsize=12)
plt.show()
"""
#############################
#############################
####### Ejercicio 02 ########
#############################
#############################
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 500)

# Definir la funcion: f(x) = sqrt(x) + 2
def funcion_2(x):
	return np.sqrt(x) + 2

y = funcion_2(x)

# Graficar
plt.figure(figsize=(8,5))
plt.plot(x, y, label="$f(x) = \sqrt{x} + 2$", color="green")
plt.title("Grafica de f(x) = \sqrt{x} + 2", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("f(x)", fontsize=14)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axhline(4, color="red", linewidth=0.9, linestyle="-")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.grid(alpha=0.4)
plt.legend(fontsize=12)
plt.show()
"""

#############################
#############################
####### Ejercicio 03 ########
#############################
#############################
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 500)

# Definir la funcion: f(x) = x**2 - x + 2
def funcion_3(x):
	return x**2 - x + 2

y = funcion_3(x)

# Graficar
plt.figure(figsize=(8,5))
plt.plot(x, y, label="$f(x) = x^2 - x + 2$", color="orange")
plt.title("Grafica de $f(x) = x^2 - x + 2$", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("f(x)", fontsize=14)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axhline(65.7, color="red", linewidth=0.9, linestyle="-")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.grid(alpha=0.4)
plt.legend(fontsize=12)
plt.show()
"""
#############################
#############################
####### Ejercicio 04 ########
#############################
#############################
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 500)

# Definir la funcion: f(x) = x**4 + x
def funcion_4(x):
	return x**4 + x

y = funcion_4(x)

# Graficar
plt.figure(figsize=(8,5))
plt.plot(x, y, label="$f(x) = x^4 + x$", color="orange")
plt.title("Grafica de $f(x) = x^4 + x$", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("f(x)", fontsize=14)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axhline(5100, color="red", linewidth=0.9, linestyle="-")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.grid(alpha=0.4)
plt.legend(fontsize=12)
plt.show()
"""

#############################
#############################
####### Ejercicio 05 ########
#############################
#############################

# ABCDEFGHIJKLMNOPQRSTUVWXYZ   
# H -> K
# O -> R
# L -> O
# A -> D

def cifrar(mensaje, desplazamiento):
	# Texto cifrado
	resultado = ""
	for caracter in mensaje:
		if caracter.isalpha():
			# Convertir el caracter a una representacion alfabetica
			base = ord('A') if caracter.isupper() else ord('a')
			# Aplicamos desplazamiento  y asegurarnos que siempre este dentro del alfabeto
			nuevo_caracter = chr((ord(caracter) - base + desplazamiento) % 26 + base)
			resultado += nuevo_caracter
		
		else:
			resultado += caracter
	return resultado

def descifrar(mensaje_cifrado, desplazamiento):
	return cifrar(mensaje_cifrado, -desplazamiento)
	
		
mensaje_original = "puso babe en vez de base en nuevo_caracter"
desplazamiento = 3

mensaje_cifrado = cifrar(mensaje_original, desplazamiento)
mensaje_descifrado = descifrar(mensaje_cifrado, desplazamiento)

print("Mensaje Original:", mensaje_original)
print("Mensaje Cifrado:", mensaje_cifrado)
print("Mensaje Descifrado:", mensaje_descifrado)








