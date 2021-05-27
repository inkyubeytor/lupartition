"""
Utilities for tests
"""
from random import randint, uniform
from typing import Dict, Hashable, Union

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


def generate_tree(nodes: int,
                  lower: Union[float, int],
                  upper: Union[float, int],
                  integral: bool,
                  key: str) \
        -> nx.Graph:
    """
    Generates a networkx vertex-weighted tree.
    :param nodes: The number of vertices to generate.
    :param lower: The (positive) lower bound on weight to randomly assign to
        the nodes.
    :param upper: The upper bound on weight to randomly assign to the nodes.
    :param integral: Whether to use integral weights.
    :param key: The key to use for node attributes.
    :return:
    """
    gen = randint if integral else uniform
    tree = nx.generators.random_tree(nodes)
    for vertex in tree.nodes:
        tree.nodes[vertex][key] = gen(lower, upper)
    return tree
