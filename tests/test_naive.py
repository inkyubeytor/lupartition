from src.lupartition import Mode, decision, partition
from tests.utils import check_partition


def test_naive_decision_tree1(tree1):
    # Positive tests
    assert decision(tree1, "weight", 3, 4, 6, Mode.NAIVE)
    assert decision(tree1, "weight", 2, 5, 10, Mode.NAIVE)
    # Negative tests
    assert not decision(tree1, "weight", 1, 4, 6, Mode.NAIVE)
    assert not decision(tree1, "weight", 4, 2, 3, Mode.NAIVE)
    assert not decision(tree1, "weight", 5, 2, 3, Mode.NAIVE)


def test_naive_decision_tree2(tree2):
    # Positive tests
    assert decision(tree2, "weight", 15, 1, 2, Mode.NAIVE)
    assert decision(tree2, "weight", 5, 3, 3, Mode.NAIVE)
    # Negative tests
    assert not decision(tree2, "weight", 4, 2, 3, Mode.NAIVE)


def test_naive_decision_tree3(tree3):
    # Positive tests
    assert decision(tree3, "mass", 3, 5.5, 8.5, Mode.NAIVE)
    # Negative tests
    assert not decision(tree3, "mass", 7, 0.5, 5.5, Mode.NAIVE)


def check_naive_partition(graph, key, parts, lower, upper):
    assignment = partition(graph, key, parts, lower, upper, Mode.NAIVE)
    return check_partition(graph, key, parts, lower, upper, assignment)


def test_naive_partition_tree1(tree1):
    # Positive tests
    assert check_naive_partition(tree1, "weight", 3, 4, 6)
    assert check_naive_partition(tree1, "weight", 2, 5, 10)
    # Negative tests
    assert not partition(tree1, "weight", 1, 4, 6, Mode.NAIVE)
    assert not partition(tree1, "weight", 4, 2, 3, Mode.NAIVE)
    assert not partition(tree1, "weight", 5, 2, 3, Mode.NAIVE)


def test_naive_partition_tree2(tree2):
    # Positive tests
    assert check_naive_partition(tree2, "weight", 15, 1, 2)
    assert check_naive_partition(tree2, "weight", 5, 3, 3)
    # Negative tests
    assert not partition(tree2, "weight", 4, 2, 3, Mode.NAIVE)


def test_naive_partition_tree3(tree3):
    # Positive tests
    assert check_naive_partition(tree3, "mass", 3, 5.5, 8.5)
    # Negative tests
    assert not partition(tree3, "mass", 7, 0.5, 5.5, Mode.NAIVE)
