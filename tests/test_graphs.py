"""
Create graphs for use in test cases here.
"""
import networkx as nx

tree1 = nx.Graph()
tree1.add_nodes_from([
    (0, {"weight": 5}),
    (1, {"weight": 3}),
    (2, {"weight": 2}),
    (3, {"weight": 2}),
    (4, {"weight": 3})
])
tree1.add_edges_from([(0, 1), (1, 2), (0, 3), (3, 4)])
