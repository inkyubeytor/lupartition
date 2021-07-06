import networkx as nx
from collections import deque

from .utils import cartesian_sum, copy, copy_partition, flatten


def naive_partition_old(tree, key, parts, lower, upper):
    """
    Implements `partition` with the naive O(p^4 u^2 n) algorithm.
    """
    # ordered(?) dict of sets
    # key is i or v_i
    dp_tree = copy(tree, key, parts, dict)
    # We adopt the convention that the (k-1)th element of the dp table for a
    # node v is our current S(T_v, k).

    # Initialize T0 for k = 1
    for node, node_data in dp_tree.nodes.items():
        node_data["table"][0][node_data["weight"]] = (2, 0, None)

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
                            s1[a + b] = (1, a, k_prime, child)
                s2 = {}
                for k_prime in range(1, k):
                    left = dp_tree.nodes[v]["table"][k_prime - 1]
                    right = dp_tree.nodes[child]["table"][k - k_prime]
                    for b in right.keys():
                        if lower <= b <= upper:
                            for a in left.keys():
                                s2[a] = (2, k_prime, child)
                s1.update(s2)
                new_table.append(s1)
            dp_tree.nodes[v]["table"] = new_table
        processed.add(v)
        root = v
    processed.clear()
    z = None
    for x in dp_tree.nodes[root]["table"][parts - 1].keys():
        if lower <= x <= upper:
            z = x
            break
    if z is None:
        return None
    assignment = {}
    partition_num = 0
    same_partition = deque([(root, parts)])
    new_partition_roots = deque()
    while same_partition or new_partition_roots:
        if same_partition:
            v, k = same_partition.popleft()
        else:  # start new partition
            partition_num += 1
            v, k = new_partition_roots.popleft()
        assignment[v] = partition_num
        children = set(dp_tree.neighbors(v)) - processed
        for x in dp_tree.nodes[v]["table"][k - 1].keys():
            if lower <= x <= upper:
                zv = x
                break
        tup = dp_tree.nodes[v]["table"][k - 1][zv]
        if tup[0] == 1:
            _, zp, kp, child = tup
        else:  # tup[0] == 2
            _, kp, child = tup
        processed.add(v)

# Decision version
# dp_tree                          - whole tree
# dp_tree.nodes[v]                 - vertex v
# dp_tree.nodes[v]["table"][k - 1] - vertex v, partition count k S(T_v, k) - set of z values

# for vertex v
# for child i
# for val of k

# Partition version
# dp_tree                          - whole tree
# dp_tree.nodes[v]                 - vertex v
# dp_tree.nodes[v]["table"][k - 1] - vertex v, partition count k
# dp_tree.nodes[v]["table"][k - 1][index i] - vertex v, partition count k
# - Dict with "vertex": v_i, "s1": S^1 (T_v^i, k), "s2": S^2 (T_v^i, k)
# s1 is a dict from z -> (z', k')   s2 is a dict from z -> k'


def naive_partition(tree, key, parts, lower, upper):
    """
    Implements `partition` with the naive O(p^4 u^2 n) algorithm.
    """
    dp_tree = copy_partition(tree, key)

    # dp_tree                          - whole tree
    # dp_tree.nodes[v]                 - vertex v
    # dp_tree.nodes[v]["table"][index i] - vertex v, child i is a dict with values "vertex": v_i,
    #   "parts": k -> Dict { z -> Set{ (z', k') for s1 | (None, k') for s2 } } }

    # Traverse the graph bottom up, defining children as
    # already-processed neighbors
    processed = set()
    root = None
    for v in nx.dfs_postorder_nodes(dp_tree):
        children = set(dp_tree.neighbors(v)) & processed
        parts_0 = {k: {} for k in range(2, parts + 1)}
        parts_0[1] = {dp_tree.nodes[v]["weight"]: (None, 0)}
        dp_tree.nodes[v]["table"] = [{"vertex": None, "parts": parts_0}]
        for child in children:
            parts_dict = {}
            for k in range(1, parts + 1):
                z_dict = {}
                # S1 stuff
                for k_prime in range(1, k + 1):
                    left = dp_tree.nodes[v]["table"][-1]["parts"][k_prime]
                    right = dp_tree.nodes[child]["table"][-1]["parts"][k - k_prime + 1]
                    for a in left:
                        for b in right:
                            try:
                                z_dict[a + b].add((a, k_prime))
                            except KeyError:
                                z_dict[a + b] = {(a, k_prime)}
                # S2 stuff
                for k_prime in range(1, k):
                    left = dp_tree.nodes[v]["table"][-1]["parts"][k_prime]
                    right = dp_tree.nodes[child]["table"][-1]["parts"][k - k_prime]
                    for b in right:
                        if lower <= b <= upper:
                            for a in left:
                                try:
                                    z_dict[a].add((None, k_prime))
                                except KeyError:
                                    z_dict[a] = {(None, k_prime)}
                parts_dict[k] = z_dict
            dp_tree.nodes[v]["table"].append({"vertex": child, "parts": parts_dict})
        processed.add(v)
        root = v
    # backtracking
    return None


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
