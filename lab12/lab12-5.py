import networkx as nx
import matplotlib.pyplot as plt


# Generate different types of random graphs
erdos_renyi = nx.erdos_renyi_graph(10, 0.3)
barabasi_albert = nx.barabasi_albert_graph(10, 2)
watts_strogatz = nx.watts_strogatz_graph(10, 4, 0.3)

# Compare their properties
graphs = [erdos_renyi, barabasi_albert, watts_strogatz]
names = ['Erdős-Rényi', 'Barabási-Albert', 'Watts-Strogatz']

for i, (graph, name) in enumerate(zip(graphs, names)):
    plt.subplot(1, 3, i+1)
    nx.draw(graph, with_labels=True, node_size=300)
    plt.title(f'{name}\nNodes: {graph.number_of_nodes()}, Edges: {graph.number_of_edges()}')
    plt.show()