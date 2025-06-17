import string

"""
def convertir_a_vector(password):
	longitud = len(password)
	mayusculas = sum(1 for c in password if c.isupper())/longitud
	numeros = sum(1 for c in password if c.isdigit())/longitud
	especiales = sum(1 for c in password if c in string.punctuation) / longitud
	return [longitud, mayusculas, numeros, especiales]

password = "Password123!"
vector = convertir_a_vector(password)
print("Vector de caracteristicas:", vector)
"""

#''' 


def clasificar_contrasena(vector, referencias):

	similitudes = {}
	
	for categoria, referencia in referencias.items():
		similitudes[categoria] = sum(v*r for v, r in zip(vector, referencia))
	
	return max(similitudes, key=similitudes.get)

referencias = {"debil": [5, 0, 0.1, 0],
			   "moderada": [8, 0.2, 0.2, 0.1],
			   "fuerte": [12, 0.4, 0.3, 0.2]}

vector = [10, 0.3, 0.2, 0.1]

categoria = clasificar_contrasena(vector, referencias)

print("La contraseña es:", categoria)
#''' 

''' 
import matplotlib.pyplot as plt

def graficar_contrasenas(vectores, etiquetas):
	
	for vector, etiqueta in zip(vectores, etiquetas):
		plt.scatter(vector[0], vector[1], label=etiqueta)

	plt.xlabel("Longitud")
	plt.ylabel("Proporcion de letras mayusculas")
	plt.legend()
	plt.title("Contraseñas en el espacio vectorial")
	plt.show()


vectores = [[10, 0.3], [5, 0], [12, 0.4]]
etiquetas = ["Password123!", "1234", "StrongPass!"]

graficar_contrasenas(vectores, etiquetas)


#''' 





