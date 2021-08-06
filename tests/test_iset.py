from src.lupartition import Mode, decision


class TestIsetDecision:
    def test_iset_decision_tree1(self,
                                 tree1_pos_test1,
                                 tree1_pos_test2,
                                 tree1_neg_test1,
                                 tree1_neg_test2,
                                 tree1_neg_test3):
        # Positive tests
        assert decision(*tree1_pos_test1, mode=Mode.ISET)
        assert decision(*tree1_pos_test2, mode=Mode.ISET)
        # Negative tests
        assert not decision(*tree1_neg_test1, mode=Mode.ISET)
        assert not decision(*tree1_neg_test2, mode=Mode.ISET)
        assert not decision(*tree1_neg_test3, mode=Mode.ISET)

    def test_iset_decision_tree2(self,
                                 tree2_pos_test1,
                                 tree2_pos_test2,
                                 tree2_neg_test1):
        # Positive tests
        assert decision(*tree2_pos_test1, mode=Mode.ISET)
        assert decision(*tree2_pos_test2, mode=Mode.ISET)
        # Negative tests
        assert not decision(*tree2_neg_test1, mode=Mode.ISET)

    def test_iset_decision_tree3(self,
                                 tree3_pos_test1,
                                 tree3_neg_test1):
        # Positive tests
        assert decision(*tree3_pos_test1, mode=Mode.ISET)
        # Negative tests
        assert not decision(*tree3_neg_test1, mode=Mode.ISET)
