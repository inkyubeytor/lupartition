import perfplot
import tests.utils as utils
from src.lupartition.methods.iset import iset_decision as iset
from src.lupartition.methods.naive import naive_decision as naive
from time import time


def generate_test(n):
    return utils.generate_tree(n, 500, 1500, True, "weight"), \
        "weight", 10, 50 * n, 150 * n


out = perfplot.bench(
    setup=generate_test,
    kernels=[
        lambda a: naive(*a),
        lambda a: iset(*a),
    ],
    labels=["naive", "iset"],
    n_range=[2 ** k for k in range(5, 14)],
)
out.show()
out.save(f"perf{time()}.png", transparent=True, bbox_inches="tight")
