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
# 2-1-0-3-4
# 2-3-5-2-3

tree2 = nx.Graph()
tree2.add_nodes_from([(i, {"weight": 1}) for i in range(15)])
tree2.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6),
                      (3, 7), (3, 8), (4, 9), (4, 10),
                      (5, 11), (5, 12), (6, 13), (6, 14)])

tree3 = nx.Graph()
tree3.add_nodes_from([(str(i), {"mass": float(i)}) for i in range(7)])
tree3.add_edges_from([("0", "1"), ("0", "2"),
                      ("1", "3"), ("1", "4"),
                      ("2", "5"), ("2", "6")])
