from functools import partial

from src.lupartition import Mode, decision, partition, partition_all
from tests.utils import check_partition, check_partitions

decision = partial(decision, mode=Mode.NAIVE)
partition = partial(partition, mode=Mode.NAIVE)


def check_naive_partition(graph, key, parts, lower, upper):
    assignment = partition(graph, key, parts, lower, upper)
    return check_partition(graph, key, parts, lower, upper, assignment)


def check_naive_partitions(graph, key, parts, lower, upper):
    # TODO: rewrite to take advantage of generator and prevent memory errors
    assignment = list(partition_all(graph, key, parts, lower, upper))
    print(f"Length = {len(assignment)}")
    return check_partitions(graph, key, parts, lower, upper, assignment)


class TestNaiveDecision:
    def test_naive_decision_tree1(self,
                                  tree1_pos_test1,
                                  tree1_pos_test2,
                                  tree1_neg_test1,
                                  tree1_neg_test2,
                                  tree1_neg_test3):
        # Positive tests
        assert decision(*tree1_pos_test1)
        assert decision(*tree1_pos_test2)
        # Negative tests
        assert not decision(*tree1_neg_test1)
        assert not decision(*tree1_neg_test2)
        assert not decision(*tree1_neg_test3)

    def test_naive_decision_tree2(self, tree2):
        # Positive tests
        assert decision(tree2, "weight", 15, 1, 2)
        assert decision(tree2, "weight", 5, 3, 3)
        # Negative tests
        assert not decision(tree2, "weight", 4, 2, 3)

    def test_naive_decision_tree3(self, tree3):
        # Positive tests
        assert decision(tree3, "mass", 3, 5.5, 8.5)
        # Negative tests
        assert not decision(tree3, "mass", 7, 0.5, 5.5)


class TestNaivePartition:

    def test_naive_partition_tree1(self, tree1):
        # Positive tests
        assert check_naive_partition(tree1, "weight", 3, 4, 6)
        assert check_naive_partition(tree1, "weight", 2, 5, 10)
        # Negative tests
        assert not partition(tree1, "weight", 1, 4, 6)
        assert not partition(tree1, "weight", 4, 2, 3)
        assert not partition(tree1, "weight", 5, 2, 3)

    def test_naive_partition_tree2(self, tree2):
        # Positive tests
        assert check_naive_partition(tree2, "weight", 15, 1, 2)
        assert check_naive_partition(tree2, "weight", 5, 3, 3)
        # Negative tests
        assert not partition(tree2, "weight", 4, 2, 3)

    def test_naive_partition_tree3(self, tree3):
        # Positive tests
        assert check_naive_partition(tree3, "mass", 3, 5.5, 8.5)
        # Negative tests
        assert not partition(tree3, "mass", 7, 0.5, 5.5)


class TestNaivePartitionAll:
    def test_rand_tree_int_small(self,
                                 rand_tree_int_small1,
                                 rand_tree_int_small2,
                                 rand_tree_int_small3,
                                 rand_tree_int_small4,
                                 rand_tree_int_small5):
        print("test_rand_tree_int_small")
        assert check_naive_partitions(*rand_tree_int_small1)
        assert check_naive_partitions(*rand_tree_int_small2)
        assert check_naive_partitions(*rand_tree_int_small3)
        assert check_naive_partitions(*rand_tree_int_small4)
        assert check_naive_partitions(*rand_tree_int_small5)

    def test_rand_tree_int_med(self,
                               rand_tree_int_med1):
        print("test_rand_tree_int_med")
        assert check_naive_partitions(*rand_tree_int_med1)

    def test_rand_tree_int_large(self,
                                 rand_tree_int_large1,
                                 rand_tree_int_large2):
        print("test_rand_tree_int_large")
        assert check_naive_partitions(*rand_tree_int_large1)
        assert check_naive_partitions(*rand_tree_int_large2)
