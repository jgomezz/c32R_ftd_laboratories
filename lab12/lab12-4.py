import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph and add nodes/edges manually
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

# Visualize with different layouts
plt.figure(figsize=(12, 4))

plt.subplot(131)
nx.draw(G, with_labels=True, node_color='lightblue')
plt.title('Default Layout')

plt.subplot(132)
nx.draw_circular(G, with_labels=True, node_color='lightgreen')
plt.title('Circular Layout')

plt.subplot(133)
nx.draw_spring(G, with_labels=True, node_color='lightcoral')
plt.title('Spring Layout')

plt.tight_layout()
plt.show()