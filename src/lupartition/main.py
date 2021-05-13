from typing import Dict, Hashable, Optional
from enum import Enum

import networkx as nx


class Mode(Enum):
    NAIVE = "naive"
    ISET = "iset"


def partition(tree: nx.Graph,
              key: Hashable,
              parts: int,
              lower: float,
              upper: float,
              mode: Mode = Mode.ISET) -> Optional[Dict[Hashable, int]]:
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
    :return: A mapping of nodes to partition components, where the ith
        component is represented by the integer i (zero-indexed), or `None` if
        no valid partition exists.
    """
    raise NotImplementedError


def decision(tree: nx.Graph,
             key: Hashable,
             parts: int,
             lower: float,
             upper: float,
             mode: Mode = Mode.ISET) -> bool:
    """
    Checks for the existence of a partition of the input tree into `parts`
    partitions such that each partition has weight between `lower` and `upper`,
    inclusive, where weight is defined as the sum over nodes of the `key`
    attribute of a node.

    :param tree: The networkx graph to partition. Must have `key` as a node
        attribute.
    :param key: The key for the weight of a node. The type of the weight values
        must be convertible to floats.
    :param parts: The number of parts to create.
    :param lower: The lower weight of a partition.
    :param upper: The upper weight of a partition.
    :param mode: The choice of algorithm to use.
    :return: Whether a valid (l, u) partition exists of the input
    """
    raise NotImplementedError
