import networkx as nx

from typing import Any, Iterable, Set


def cartesian_sum(s1: Set, s2: Set) -> Set:
    """
    Returns the Cartesian sum (sum of all pairs of Cartesian product) of the
    input sets.
    :param s1: An input set of elements (must implement `+`).
    :param s2: A second input set of the same type as the first.
    :return: An output set of the Cartesian product of `s1`, `s2` with the
        same type as the input sets.
    """
    return {a + b for a in s1 for b in s2}


def copy(graph: nx.Graph, attribute: Any, parts: int) -> nx.Graph:
    """
    Creates a "Fresh Data" copy of the input graph, adding the given attribute
    key as an attribute `"weight"` and creating an attribute `"table"` with a
    dynamic programming table containing `parts` empty sets.
    :param graph: The input graph to copy.
    :param attribute: The attribute to use for weights.
    :param parts: The length of the dynamic programming table.
    :return: A copy of `graph` usable for dynamic programming algorithms.
    """
    # Perform the "Fresh Data" copy
    dp_graph = graph.__class__()
    dp_graph.add_nodes_from(graph)
    dp_graph.add_edges_from(graph.edges)

    for node, node_data in graph.nodes.items():
        dp_graph.nodes[node]["weight"] = node_data[attribute]
        dp_graph.nodes[node]["table"] = [set() for _ in range(parts)]

    return dp_graph


def flatten(sets: Iterable[Set]) -> Set:
    """
    Merges an iterable of sets.
    :param sets: Any iterable of sets.
    :return: The union of all input sets.
    """
    out = set()
    for s in sets:
        out |= s
    return out
