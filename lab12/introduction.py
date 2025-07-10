'''
Tema : Introducción a los grafos
Fecha : 09/07/2025
Version : v1
Autor : Jaime Gomez
'''

# Matriz Adyacente
grafo_MA = [[0,  1,	1,	0],
            [0,	0,	1,	0],
            [0,	0,	0,	1],
            [1,	0,	0,	0]]

# Listas Adyacente
grafo_LA = {"A":	["C","B"],
            "B":	["C"],
            "C":	["D"],
            "D":	["A"]}

print(grafo_LA["A"])
