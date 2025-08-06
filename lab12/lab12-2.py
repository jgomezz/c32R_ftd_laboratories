import networkx as nx
import matplotlib.pyplot as plt


n = 6  # número de vértices
p = 0.4  # probabilidad de conexión entre nodos
G = nx.erdos_renyi_graph(n, p)


nx.draw(G, with_labels=True, node_color='orange', node_size=800)
plt.title("Grafo Aleatorio")
plt.show()
