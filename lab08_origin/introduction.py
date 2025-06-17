
'''
a = ("Jaime", "Edgar", "Juan")
b = ("Carmen", "Maribel", "Silvia")
x = tuple(zip(a, b))
print(x)

'''

import numpy as np

vector_A = np.array([1, 2, 3])
vector_B = np.array([4, 5, 6])

# Sum of vectors
sum_vectors = vector_A + vector_B
print("Sum:", sum_vectors)

# Element-wise addition using np.add
add_vectors = np.add(vector_A, vector_B)
print("Add:", add_vectors)

# Subtraction of vectors
sub_vectors = vector_A - vector_B
print("Sub:", sub_vectors)

# Scalar multiplication
scalar = 2
mult_escalar_A = scalar * vector_A
print("Mult escalar A:", mult_escalar_A)

mult_escalar_B = scalar * vector_B
print("Mult escalar B:", mult_escalar_B)

# Element-wise multiplication
mult_vectors = vector_A * vector_B
print("Mult:", mult_vectors)

# Element-wise division
div_vectors = vector_A / vector_B
print("Div:", div_vectors)

# Euclidiana
vector_B = np.array([8, -3, 6, 1])

B_2 = np.sqrt(np.sum(np.pow(vector_B,2)))
print(B_2)
magnitud_P1 = np.linalg.norm(vector_B)
print(magnitud_P1)
