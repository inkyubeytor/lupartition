from functools import partial

from src.lupartition import Mode, decision, partition

decision = partial(decision, mode=Mode.ISET)
partition = partial(partition, mode=Mode.ISET)


class TestIsetDecision:
    def test_iset_decision_tree1(self,
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

    def test_iset_decision_tree2(self,
                                 tree2_pos_test1,
                                 tree2_pos_test2,
                                 tree2_neg_test1):
        # Positive tests
        assert decision(*tree2_pos_test1)
        assert decision(*tree2_pos_test2)
        # Negative tests
        assert not decision(*tree2_neg_test1)

    def test_iset_decision_tree3(self,
                                 tree3_pos_test1,
                                 tree3_neg_test1):
        # Positive tests
        assert decision(*tree3_pos_test1)
        # Negative tests
        assert not decision(*tree3_neg_test1)


class TestIsetPartition:
    pass
