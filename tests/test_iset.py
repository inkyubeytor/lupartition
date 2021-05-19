from src.lupartition.methods.iset import iset_decision


class TestIsetDecision:
    def test_iset_decision_tree1(self, tree1):
        # Positive tests
        assert iset_decision(tree1, "weight", 3, 4, 6)
        assert iset_decision(tree1, "weight", 2, 5, 10)
        # Negative tests
        assert not iset_decision(tree1, "weight", 1, 4, 6)
        assert not iset_decision(tree1, "weight", 4, 2, 3)
        assert not iset_decision(tree1, "weight", 5, 2, 3)

    def test_iset_decision_tree2(self, tree2):
        # Positive tests
        assert iset_decision(tree2, "weight", 15, 1, 2)
        assert iset_decision(tree2, "weight", 5, 3, 3)
        # Negative tests
        assert not iset_decision(tree2, "weight", 4, 2, 3)

    def test_iset_decision_tree3(self, tree3):
        # Positive tests
        assert iset_decision(tree3, "mass", 3, 5.5, 8.5)
        # Negative tests
        assert not iset_decision(tree3, "mass", 7, 0.5, 5.5)
