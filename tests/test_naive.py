from methods.naive import naive_partition, naive_decision
from tests.test_graphs import tree1


def test_naive_tree1():
    assert naive_decision(tree1, "weight", 3, 4, 6)
    assert not naive_decision(tree1, "weight", 1, 4, 6)
    assert naive_decision(tree1, "weight", 2, 5, 10)


if __name__ == "__main__":
    test_naive_tree1()
