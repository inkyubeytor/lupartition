import networkx as nx

from .utils import cartesian_sum, copy, flatten


def naive_partition(tree, key, parts, lower, upper):
    """
    Implements `partition` with the naive O(p^4 u^2 n) algorithm.
    """
    dp_tree = copy(tree, key, parts, dict)
    # We adopt the convention that the (k-1)th element of the dp table for a
    # node v is our current S(T_v, k).

    # Initialize T0 for k = 1
    for node, node_data in dp_tree.nodes.items():
        node_data["table"][0][node_data["weight"]] = (2, 0)

    # Traverse the graph bottom up, defining children as
    # already-processed neighbors
    processed = set()
    root = None
    for v in nx.dfs_postorder_nodes(dp_tree):
        children = set(dp_tree.neighbors(v)) & processed
        for child in children:
            new_table = []
            for k in range(1, parts + 1):
                s1 = {}
                for k_prime in range(1, k + 1):
                    left = dp_tree.nodes[v]["table"][k_prime - 1]
                    right = dp_tree.nodes[child]["table"][k - k_prime]
                    for a in left.keys():
                        for b in right.keys():
                            s1[a + b] = (1, a, k_prime)
                s2 = {}
                for k_prime in range(1, k):
                    left = dp_tree.nodes[v]["table"][k_prime - 1]
                    right = dp_tree.nodes[child]["table"][k - k_prime]
                    for b in right.keys():
                        if lower <= b <= upper:
                            for a in left.keys():
                                s2[a] = (2, k_prime)
                s1.update(s2)
                new_table.append(s1)
            dp_tree.nodes[v]["table"] = new_table
        processed.add(v)
        root = v
    return any(map(lambda x: lower <= x <= upper,
                   dp_tree.nodes[root]["table"][parts - 1]))


def naive_decision(tree, key, parts, lower, upper):
    """
    Implements the decision problem variant of the naive O(p^4 u^2 n) algorithm.
    """
    dp_tree = copy(tree, key, parts, set)
    # We adopt the convention that the (k-1)th element of the dp table for a
    # node v is our current S(T_v, k).

    # Initialize T0 for k = 1
    for node, node_data in dp_tree.nodes.items():
        node_data["table"][0].add(node_data["weight"])

    # Traverse the graph bottom up, defining children as
    # already-processed neighbors
    processed = set()
    root = None
    for v in nx.dfs_postorder_nodes(dp_tree):
        children = set(dp_tree.neighbors(v)) & processed
        for child in children:
            new_table = []
            for k in range(1, parts + 1):
                s1 = flatten(cartesian_sum(
                    dp_tree.nodes[v]["table"][k_prime - 1],
                    dp_tree.nodes[child]["table"][k - k_prime]
                )
                    for k_prime in range(1, k + 1))
                s2 = flatten(
                    dp_tree.nodes[v]["table"][k_prime - 1]
                    for k_prime in range(1, k)
                    if any(map(lambda x: lower <= x <= upper,
                               dp_tree.nodes[child]["table"][k - k_prime - 1]))
                )
                new_table.append(s1 | s2)
            dp_tree.nodes[v]["table"] = new_table
        processed.add(v)
        root = v
    return any(map(lambda x: lower <= x <= upper,
                   dp_tree.nodes[root]["table"][parts - 1]))
