"""
Create graphs for use in test cases here.
"""
from typing import Tuple

import networkx as nx
import pytest

import tests.utils as utils


@pytest.fixture
def tree1() -> nx.Graph:
    """
    :return: A line graph on 5 vertices with varying weights.
    """
    tree = nx.Graph()
    tree.add_nodes_from([
        (0, {"weight": 2}),
        (1, {"weight": 3}),
        (2, {"weight": 5}),
        (3, {"weight": 2}),
        (4, {"weight": 3})
    ])
    tree.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4)])
    return tree


@pytest.fixture
def tree1_pos_test1(tree1) -> Tuple[nx.Graph, str, int, int, int]:
    return tree1, "weight", 3, 4, 6


@pytest.fixture
def tree1_pos_test2(tree1) -> Tuple[nx.Graph, str, int, int, int]:
    return tree1, "weight", 2, 5, 10


@pytest.fixture
def tree1_neg_test1(tree1) -> Tuple[nx.Graph, str, int, int, int]:
    return tree1, "weight", 1, 4, 6


@pytest.fixture
def tree1_neg_test2(tree1) -> Tuple[nx.Graph, str, int, int, int]:
    return tree1, "weight", 4, 2, 3


@pytest.fixture
def tree1_neg_test3(tree1) -> Tuple[nx.Graph, str, int, int, int]:
    return tree1, "weight", 5, 2, 3


@pytest.fixture
def tree2() -> nx.Graph:
    """
    :return: A complete binary tree of depth 4 with uniform weights of 1.
    """
    tree = nx.Graph()
    tree.add_nodes_from([(i, {"weight": 1}) for i in range(15)])
    tree.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6),
                         (3, 7), (3, 8), (4, 9), (4, 10),
                         (5, 11), (5, 12), (6, 13), (6, 14)])
    return tree


@pytest.fixture
def tree2_pos_test1(tree2) -> Tuple[nx.Graph, str, int, int, int]:
    return tree2, "weight", 15, 1, 2


@pytest.fixture
def tree2_pos_test2(tree2) -> Tuple[nx.Graph, str, int, int, int]:
    return tree2, "weight", 5, 3, 3


@pytest.fixture
def tree2_neg_test1(tree2) -> Tuple[nx.Graph, str, int, int, int]:
    return tree2, "weight", 4, 2, 3


@pytest.fixture
def tree3() -> nx.Graph:
    """
    :return: A complete binary tree on 7 vertices with the ith vertex having
    weight i. This test uses a non-default keyword for the weight attribute
    and uses the float type for weights in order to test graph parsing.
    """
    tree = nx.Graph()
    tree.add_nodes_from([(str(i), {"mass": float(i)}) for i in range(7)])
    tree.add_edges_from([("0", "1"), ("0", "2"),
                         ("1", "3"), ("1", "4"),
                         ("2", "5"), ("2", "6")])
    return tree


@pytest.fixture
def tree3_pos_test1(tree3) -> Tuple[nx.Graph, str, int, float, float]:
    return tree3, "mass", 3, 5.5, 8.5


@pytest.fixture
def tree3_neg_test1(tree3) -> Tuple[nx.Graph, str, int, float, float]:
    return tree3, "mass", 7, 0.5, 5.5


@pytest.fixture
def rand_tree_int_small1() -> Tuple[nx.Graph, str, int, int, int]:
    return utils.generate_tree(20, 1, 7, True, "weight"), \
           "weight", 5, 12, 20


@pytest.fixture
def rand_tree_int_small2() -> Tuple[nx.Graph, str, int, int, int]:
    return utils.generate_tree(20, 1, 7, True, "weight"), \
           "weight", 5, 10, 22


@pytest.fixture
def rand_tree_int_small3() -> Tuple[nx.Graph, str, int, int, int]:
    return utils.generate_tree(20, 1, 7, True, "weight"), \
           "weight", 4, 15, 25


@pytest.fixture
def rand_tree_int_small4() -> Tuple[nx.Graph, str, int, int, int]:
    return utils.generate_tree(20, 1, 7, True, "weight"), \
           "weight", 4, 10, 30


@pytest.fixture
def rand_tree_int_small5() -> Tuple[nx.Graph, str, int, int, int]:
    return utils.generate_tree(20, 1, 7, True, "weight"), \
           "weight", 2, 35, 45


@pytest.fixture
def rand_tree_int_large1() -> Tuple[nx.Graph, str, int, int, int]:
    return utils.generate_tree(2000, 1, 11, True, "weight"), \
           "weight", 10, 800, 1200


@pytest.fixture
def rand_tree_int_large2() -> Tuple[nx.Graph, str, int, int, int]:
    return utils.generate_tree(2000, 1, 11, True, "weight"), \
           "weight", 20, 350, 650
