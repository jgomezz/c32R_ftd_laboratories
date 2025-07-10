import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_edges_from([("A","B"), ("A","C"), ("B","D"), ("C","D"), ("D","E")])

# Lista de adyacencia
print("Lista de Adyacencia:")
for node, neighbors in G.adjacency(): 
  print(f"{node}:{list(neighbors)} ")

# Dibujar el grafo
nx.draw(G, with_labels=True, node_color='skyblue', node_size=800)
plt.title("Grafo Ejercicio 1")
plt.show()
