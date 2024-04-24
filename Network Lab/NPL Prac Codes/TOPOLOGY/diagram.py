import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_nodes_from([1, 2, 3, 4, 5])
edge_list = [(1,2), (1,3), (1,4), (1,5),                  # Mesh Topology
             (2,1), (2,3), (2,4), (2,5),
             (3,1), (3,2), (3,4), (3,5),
             (4,1), (4,2), (4,3), (4,5),
             (5,1), (5,2), (5,3), (5,4)]
g.add_edges_from(edge_list)
nx.draw(g, with_labels = True, node_color = 'lightblue', node_size = 1000, font_size = 12, font_weight = "bold")
plt.show()