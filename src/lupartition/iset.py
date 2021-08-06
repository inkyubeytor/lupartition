from typing import Set

import networkx as nx

from .utils import copy, flatten


def iset_partition(tree, key, parts, lower, upper):
    """
    Implements `partition` with the polynomial O(p^4 n) algorithm.
    """
    raise NotImplementedError


def iset_decision(tree, key, parts, lower, upper):
    """
    Implements `decision` with the polynomial O(p^4 n) algorithm.
    """
    dp_tree = copy(tree, key, parts, set)
    # We adopt the convention that the (k-1)th element of the dp table for a
    # node v is our current S(T_v, k).

    # Initialize T0 for k = 1
    for node, node_data in dp_tree.nodes.items():
        node_data["table"][0].add((node_data["weight"], node_data["weight"]))

    # Traverse the graph bottom up, defining children as
    # already-processed neighbors
    processed = set()
    root = None
    for v in nx.dfs_postorder_nodes(dp_tree):
        children = set(dp_tree.neighbors(v)) & processed
        for child in children:
            new_table = []
            for k in range(1, parts + 1):
                i1 = flatten(cartesian_sum_iset(
                    dp_tree.nodes[v]["table"][k_prime - 1],
                    dp_tree.nodes[child]["table"][k - k_prime]
                )
                    for k_prime in range(1, k + 1))
                i2 = flatten(
                    dp_tree.nodes[v]["table"][k_prime - 1]
                    for k_prime in range(1, k)
                    if any(map(lambda x: lower <= x[1] <= upper or
                               x[0] <= upper <= x[1],
                               dp_tree.nodes[child]["table"][k - k_prime - 1]))
                )
                new_table.append(iset_merge(i1 | i2, upper - lower))
            dp_tree.nodes[v]["table"] = new_table
        processed.add(v)
        root = v
    return any(map(lambda x: lower <= x[1] <= upper or x[0] <= upper <= x[1],
                   dp_tree.nodes[root]["table"][parts - 1]))


def cartesian_sum_iset(s1: Set, s2: Set) -> Set:
    """
    Returns the Cartesian sum (sum of all pairs of Cartesian product) of the
    input interval sets.
    :param s1: An input interval set.
    :param s2: A second interval set.
    :return: An output interval set of the Cartesian sum of `s1`, `s2`.
    """
    return {(a1 + b1, a2 + b2) for a1, a2 in s1 for b1, b2 in s2}


def iset_merge(s: Set, d: float) -> Set:
    """
    Implements the interval merge operation on a set of intervals to create a
    valid interval set.
    :param s: A set of intervals to merge as necessary.
    :param d: The difference between the lower and upper bounds, used for
        defining interference between intervals.
    :return: A valid interval set without interfering intervals.
    """
    if len(s) == 0:
        return set()

    out = set()
    current = list(sorted(s, reverse=True))
    while len(current) > 1:
        a_low, a_high = current.pop()
        b_low, b_high = current.pop()
        if b_low - a_high <= d:
            current.append((a_low, max(a_high, b_high)))
        else:
            current.append((b_low, b_high))
            out.add((a_low, a_high))
    out.add(current.pop())
    return out
