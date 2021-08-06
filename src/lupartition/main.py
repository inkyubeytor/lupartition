from enum import Enum
from typing import Dict, Generator, Hashable, Optional

import networkx as nx

from .iset import iset_decision, iset_partition
from .naive import naive_decision, naive_partition, naive_partition_all


class Mode(Enum):
    NAIVE = "naive"
    ISET = "iset"


def partition_all(tree: nx.Graph,
                  key: Hashable,
                  parts: int,
                  lower: float,
                  upper: float) -> Generator[Dict[Hashable, int], None, None]:
    """
    Returns all possible partitions of the input tree into `parts` partitions
    such that each partition has weight between `lower` and `upper`, inclusive,
    where weight is defined as the sum over nodes of the `key` attribute of a
    node.

    :param tree: The networkx graph to partition. Must have `key` as a node
        attribute.
    :param key: The key for the weight of a node. The type of the weight values
        must be convertible to floats.
    :param parts: The number of parts to create.
    :param lower: The lower weight of a partition.
    :param upper: The upper weight of a partition.
    :return: All possible mapping of nodes to partition components, where the
        ith component is represented by the integer i (zero-indexed).
    """
    return naive_partition_all(tree, key, parts, lower, upper)


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
    _partition = naive_partition if mode == mode.NAIVE else iset_partition
    return _partition(tree, key, parts, lower, upper)


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
    _decision = naive_decision if mode == mode.NAIVE else iset_decision
    return _decision(tree, key, parts, lower, upper)
