import networkx as nx

from typing import Any, Callable, Hashable, Iterable, Set


def copy(graph: nx.Graph,
         attribute: Hashable,
         parts: int,
         default: Callable[[], Any]) -> nx.Graph:
    """
    Creates a "Fresh Data" copy of the input graph, adding the given attribute
    key as an attribute `"weight"` and creating an attribute `"table"` with a
    dynamic programming table containing `parts` empty sets.
    :param graph: The input graph to copy.
    :param attribute: The attribute to use for weights.
    :param parts: The length of the dynamic programming table.
    :param default: A constructor for the starting value for each table entry.
    :return: A copy of `graph` usable for dynamic programming algorithms.
    """
    # Perform the "Fresh Data" copy
    dp_graph = graph.__class__()
    dp_graph.add_nodes_from(graph)
    dp_graph.add_edges_from(graph.edges)

    for node, node_data in graph.nodes.items():
        dp_graph.nodes[node]["weight"] = node_data[attribute]
        dp_graph.nodes[node]["table"] = [default() for _ in range(parts)]

    return dp_graph


def flatten(sets: Iterable[Set]) -> Set:
    """
    Flattens an iterable of sets.
    :param sets: Any iterable of sets.
    :return: The union of all input sets.
    """
    out = set()
    for s in sets:
        out |= s
    return out
