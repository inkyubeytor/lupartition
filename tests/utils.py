"""
Utilities for tests
"""
from typing import Dict, Hashable

import networkx as nx


def check_partition(graph: nx.Graph,
                    key: Hashable,
                    parts: int,
                    lower: float,
                    upper: float,
                    partition: Dict[Hashable, int]) -> bool:
    """
    Checks the validity of an (l, u) partition.
    :param graph: The networkx graph to partition. Must have `key` as a node
        attribute.
    :param key: The key for the weight of a node. The type of the weight values
        must be convertible to floats.
    :param parts: The number of parts desired.
    :param lower: The lower weight of a partition.
    :param upper: The upper weight of a partition.
    :param partition: The partition to check against the other parameters.
    :return: Whether the partition is valid.
    """
    raise NotImplementedError
