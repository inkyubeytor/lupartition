import networkx as nx
from collections import defaultdict
from src.lupartition.methods.naive import naive_decision, naive_partition
from tests.test_graphs import tree1, tree2, tree3


def valid_partition_checker(assignment, tree, key, lower, upper):
    rev_assign = defaultdict(set)
    for k, v in assignment.items():
        rev_assign[v].add(k)
    for p in rev_assign.values():
        # check connectedness
        subtree = tree.subgraph(p)
        if not nx.is_connected(subtree):
            return False
        # check weight
        weight = sum(tree.nodes[node][key] for node in p)
        if not lower <= weight <= upper:
            return False
    return True

def test_naive_decision_tree1():
    # Positive tests
    assert naive_decision(tree1, "weight", 3, 4, 6)
    assert naive_decision(tree1, "weight", 2, 5, 10)
    # Negative tests
    assert not naive_decision(tree1, "weight", 1, 4, 6)
    assert not naive_decision(tree1, "weight", 4, 2, 3)
    assert not naive_decision(tree1, "weight", 5, 2, 3)


def test_naive_decision_tree2():
    # Positive tests
    assert naive_decision(tree2, "weight", 15, 1, 2)
    assert naive_decision(tree2, "weight", 5, 3, 3)
    # Negative tests
    assert not naive_decision(tree2, "weight", 4, 2, 3)


def test_naive_decision_tree3():
    # Positive tests
    assert naive_decision(tree3, "mass", 3, 5.5, 8.5)
    # Negative tests
    assert not naive_decision(tree3, "mass", 7, 0.5, 5.5)


def test_naive_decision():
    test_naive_decision_tree1()
    test_naive_decision_tree2()
    test_naive_decision_tree3()


def test_naive_partition_tree1():
    # Positive tests
    assert valid_partition_checker(naive_partition(tree1, "weight", 3, 4, 6), tree1, "weight", 4, 6)
    assert valid_partition_checker(naive_partition(tree1, "weight", 2, 5, 10), tree1, "weight", 5, 10)
    # Negative tests
    assert not naive_partition(tree1, "weight", 1, 4, 6)
    assert not naive_partition(tree1, "weight", 4, 2, 3)
    assert not naive_partition(tree1, "weight", 5, 2, 3)


def test_naive_partition_tree2():
    # Positive tests
    assert valid_partition_checker(naive_partition(tree2, "weight", 15, 1, 2), tree2, "weight", 1, 2)
    assert valid_partition_checker(naive_partition(tree2, "weight", 5, 3, 3), tree2, "weight", 3, 3)
    # Negative tests
    assert not naive_partition(tree2, "weight", 4, 2, 3)


def test_naive_partition_tree3():
    # Positive tests
    assert valid_partition_checker(naive_partition(tree3, "mass", 3, 5.5, 8.5), tree3, "mass", 5.5, 8.5)
    # Negative tests
    assert not naive_partition(tree3, "mass", 7, 0.5, 5.5)


def test_naive_partition():
    test_naive_partition_tree1()
    test_naive_partition_tree2()
    test_naive_partition_tree3()


if __name__ == "__main__":
    # test_naive_decision()
    test_naive_partition()
