import networkx as nx

from .utils import copy


def naive_partition(tree, key, parts, lower, upper):
    """
    Implements `partition` with the naive O(p^4 u^2 n) algorithm.
    """
    raise NotImplementedError


def naive_decision(tree, key, parts, lower, upper):
    """
    Implements the decision problem variant of the naive O(p^4 u^2 n) algorithm.
    """
    dp_tree = copy(tree, key, parts)
    # We adopt the convention that the (k-1)th element of the dp table for a
    # node v is our current S(T_v, k).

    # Initialize T0 for k = 1
    for node, node_data in dp_tree.nodes.items():
        node_data["table"][0].add(node_data["weight"])

    raise NotImplementedError
