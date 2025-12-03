# Program: Network Graph Visualization using NetworkX

import networkx as nx
import matplotlib.pyplot as plt

# Create a graph object
G = nx.Graph()

# Add nodes
G.add_nodes_from(["A", "B", "C", "D", "E"])

# Add edges (connections)
G.add_edges_from([("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("D", "E")])

# Draw the graph
plt.figure(figsize=(6, 4))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_weight='bold')
plt.title("Network Graph using NetworkX", fontsize=14)
plt.show()
