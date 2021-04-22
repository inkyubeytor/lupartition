from typing import Any, Dict, Optional

import networkx as nx


# TODO: determine type of key
# TODO: determine how to encode mode
# TODO: determine type of return dict (something like node -> int)
def partition(tree: nx.Graph,
              key: Any,
              parts: int,
              lower: float,
              upper: float,
              mode="naive") -> Optional[Dict]:
    """
    Partitions the input tree into `parts` partitions such that each partition
    has weight between `lower` and `upper`, inclusive, where weight is defined
    as the sum over nodes of the `key` attribute of a node. If no such
    partition is possible, returns `None`.

    :param tree: The networkx graph to partition. Must have `key` as a node
        attribute.
    :param key: The key for the weight of a node. The type of the weight values
        must be convertible to floats.
    :param parts: The number of parts to create.
    :param lower: The lower weight of a partition.
    :param upper: The upper weight of a partition.
    :param mode: The choice of algorithm to use.
    :return: A mapping of nodes to partition components, or `None` if no valid
        partition exists.
    """
    raise NotImplementedError
