from src.lupartition.methods.naive import naive_decision, naive_partition
from tests.test_graphs import tree1, tree2, tree3


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
    naive_partition(tree1, "weight", 3, 4, 6)


def test_naive_partition():
    test_naive_partition_tree1()


if __name__ == "__main__":
    test_naive_decision()
    test_naive_partition()
