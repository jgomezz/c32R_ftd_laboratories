import networkx as nx
import matplotlib.pyplot as plt

# Create a weighted graph
G = nx.Graph()
edges = [('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 1), ('B', 'D', 5), 
         ('C', 'D', 8), ('C', 'E', 10), ('D', 'E', 2), ('D', 'F', 6), ('E', 'F', 3)]
G.add_weighted_edges_from(edges)

# Find shortest path
shortest_path = nx.shortest_path(G, 'A', 'F', weight='weight')
path_edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]

# Visualize
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})

# Highlight shortest path
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
plt.title(f'Shortest Path from A to F: {" -> ".join(shortest_path)}')
plt.show()