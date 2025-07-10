'''
Tema : Lab 12 -> Grafos
Fecha : 09/07/2025
Version : v1
Autor : Jaime Gomez
'''

# /opt/homebrew/bin/python3.11 -m pip install networkx
# /opt/homebrew/bin/python3.11 -m pip install matplotlib


import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_edges_from(
    [("A", "B"), 
     ("B", "C"), 
     ("C", "D"), 
     ("D", "A"), 
     ("A", "C")])

# Mostrar grado de cada vértice
for node in G.nodes():
    print(f"Grado de {node}: {G.degree(node)}")

# Dibujar
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1000)
plt.title("Grafo no dirigido")
plt.show()


