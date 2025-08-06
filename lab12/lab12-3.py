import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_edges_from([(1,2), (1,3), (2,4), (3,4), (4,5)])


# Dibujar el grafo
nx.draw(G, with_labels=True, node_color='skyblue', node_size=800)
plt.title("Grafo Ejercicio 1")
plt.show()


# Matriz de adyacencia
adj_matrix = nx.adjacency_matrix(G).todense()
print("Matriz de Adyacencia:")
print(adj_matrix)
