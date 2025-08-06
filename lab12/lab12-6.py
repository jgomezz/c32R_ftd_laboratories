import networkx as nx
import matplotlib.pyplot as plt

# Create a friendship network
friends = nx.Graph()
friends.add_edges_from([
    ('Alice', 'Bob'), ('Alice', 'Charlie'), ('Bob', 'David'),
    ('Charlie', 'David'), ('David', 'Eve'), ('Eve', 'Frank'),
    ('Charlie', 'Frank'), ('Bob', 'Grace')
])

# Calculate centrality measures
degree_centrality = nx.degree_centrality(friends)
betweenness_centrality = nx.betweenness_centrality(friends)
closeness_centrality = nx.closeness_centrality(friends)

# Visualize with node sizes based on centrality
plt.figure(figsize=(15, 5))

plt.subplot(131)
node_sizes = [degree_centrality[node] * 1000 for node in friends.nodes()]
nx.draw(friends, with_labels=True, node_size=node_sizes, node_color='lightblue')
plt.title('Degree Centrality')

plt.subplot(132)
node_sizes = [betweenness_centrality[node] * 1000 for node in friends.nodes()]
nx.draw(friends, with_labels=True, node_size=node_sizes, node_color='lightgreen')
plt.title('Betweenness Centrality')

plt.subplot(133)
node_sizes = [closeness_centrality[node] * 1000 for node in friends.nodes()]
nx.draw(friends, with_labels=True, node_size=node_sizes, node_color='lightcoral')
plt.title('Closeness Centrality')

plt.tight_layout()
plt.show()