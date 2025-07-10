import networkx as nx
import matplotlib.pyplot as plt

# /opt/homebrew/bin/python3.11 -m pip install scipy

G = nx.Graph()
G.add_edges_from([("A","B"), ("A","C"), ("B","D"), ("C","D"), ("D","E")])

# Matriz de adyacencia
adj_matrix = nx.adjacency_matrix(G).todense()
print("Matriz de Adyacencia:")
print(adj_matrix)

# Dibujar el grafo
nx.draw(G, with_labels=True, node_color='skyblue', node_size=800)
plt.title("Grafo Ejercicio 1")
plt.show()



