from typing import Set

import networkx as nx

from .utils import copy, copy_partition, flatten


def naive_partition(tree, key, parts, lower, upper):
    """
    Implements `partition` with the naive O(p^4 u^2 n) algorithm.
    """
    dp_tree = copy_partition(tree, key)

    # dp_tree                          - whole tree
    # dp_tree.nodes[v]                 - vertex v
    # dp_tree.nodes[v]["table"][i] - vertex v, child i is a dict with values
    #   "vertex": v_i,
    #   "parts": k -> Dict { z -> Set{ (z', k') for s1 | (None, k') for s2 } } }

    # Traverse the graph bottom up, defining children as
    # already-processed neighbors
    processed = set()
    root = None
    for v in nx.dfs_postorder_nodes(dp_tree):
        children = set(dp_tree.neighbors(v)) & processed
        parts_0 = {k: {} for k in range(2, parts + 1)}
        parts_0[1] = {dp_tree.nodes[v]["weight"]: {(None, 0)}}
        dp_tree.nodes[v]["table"] = [{"vertex": None, "parts": parts_0}]
        for child in children:
            parts_dict = {}
            for k in range(1, parts + 1):
                z_dict = {}
                # S1 stuff
                for k_prime in range(1, k + 1):
                    left = dp_tree.nodes[v]["table"][-1]["parts"][k_prime]
                    right = dp_tree.nodes[child]["table"][-1]["parts"][
                        k - k_prime + 1]
                    for a in left:
                        for b in right:
                            try:
                                z_dict[a + b].add((a, k_prime))
                            except KeyError:
                                z_dict[a + b] = {(a, k_prime)}
                # S2 stuff
                for k_prime in range(1, k):
                    left = dp_tree.nodes[v]["table"][-1]["parts"][k_prime]
                    right = dp_tree.nodes[child]["table"][-1]["parts"][
                        k - k_prime]
                    for b in right:
                        if lower <= b <= upper:
                            for a in left:
                                try:
                                    z_dict[a].add((None, k_prime))
                                except KeyError:
                                    z_dict[a] = {(None, k_prime)}
                parts_dict[k] = z_dict
            dp_tree.nodes[v]["table"].append(
                {"vertex": child, "parts": parts_dict})
        processed.add(v)
        root = v

    # backtracking
    try:
        next(filter(lambda y: lower <= y <= upper,
                    dp_tree.nodes[root]["table"][-1]["parts"][parts]))
    except StopIteration:
        return None

    assignment = {root: 0}
    input_queue = [(root, None, parts, len(dp_tree.nodes[v]["table"]) - 1, 0)]

    def process(v, z, k, i, v_part_num):
        if i == 0:
            return

        if z is None:  # make a new partition
            z = next(filter(lambda y: lower <= y <= upper,
                            dp_tree.nodes[v]["table"][i]["parts"][k]))

        vp = dp_tree.nodes[v]["table"][i]["vertex"]
        zp, kp = dp_tree.nodes[v]["table"][i]["parts"][k][z].pop()
        if zp is None:
            new_part_num = 1 + max(assignment.values(), default=0)
            assignment[vp] = new_part_num
            input_queue.append((v, z, kp, i - 1, v_part_num))
            input_queue.append((vp, None, k - kp,
                                len(dp_tree.nodes[vp]["table"]) - 1,
                                new_part_num))
        else:
            assignment[vp] = v_part_num
            input_queue.append((v, zp, kp, i - 1, v_part_num))
            input_queue.append((vp, z - zp, k - kp + 1,
                                len(dp_tree.nodes[vp]["table"]) - 1,
                                v_part_num))

    while input_queue:
        process(*input_queue.pop())

    print(assignment)
    return assignment


def naive_partition_all(tree, key, parts, lower, upper):
    """
    Implements `partition` with the naive O(p^4 u^2 n) algorithm.
    """
    dp_tree = copy_partition(tree, key)

    # dp_tree                          - whole tree
    # dp_tree.nodes[v]                 - vertex v
    # dp_tree.nodes[v]["table"][i] - vertex v, child i is a dict with values
    #   "vertex": v_i,
    #   "parts": k -> Dict { z -> Set{ (z', k') for s1 | (None, k') for s2 } } }

    # Traverse the graph bottom up, defining children as
    # already-processed neighbors
    processed = set()
    root = None
    for v in nx.dfs_postorder_nodes(dp_tree):
        children = set(dp_tree.neighbors(v)) & processed
        parts_0 = {k: {} for k in range(2, parts + 1)}
        parts_0[1] = {dp_tree.nodes[v]["weight"]: {(None, 0)}}
        dp_tree.nodes[v]["table"] = [{"vertex": None, "parts": parts_0}]
        for child in children:
            parts_dict = {}
            for k in range(1, parts + 1):
                z_dict = {}
                # S1 stuff
                for k_prime in range(1, k + 1):
                    left = dp_tree.nodes[v]["table"][-1]["parts"][k_prime]
                    right = dp_tree.nodes[child]["table"][-1]["parts"][
                        k - k_prime + 1]
                    for a in left:
                        for b in right:
                            try:
                                z_dict[a + b].add((a, k_prime))
                            except KeyError:
                                z_dict[a + b] = {(a, k_prime)}
                # S2 stuff
                for k_prime in range(1, k):
                    left = dp_tree.nodes[v]["table"][-1]["parts"][k_prime]
                    right = dp_tree.nodes[child]["table"][-1]["parts"][
                        k - k_prime]
                    for b in right:
                        if lower <= b <= upper:
                            for a in left:
                                try:
                                    z_dict[a].add((None, k_prime))
                                except KeyError:
                                    z_dict[a] = {(None, k_prime)}
                parts_dict[k] = z_dict
            dp_tree.nodes[v]["table"].append(
                {"vertex": child, "parts": parts_dict})
        processed.add(v)
        root = v

    # backtracking
    try:
        next(filter(lambda y: lower <= y <= upper,
                    dp_tree.nodes[root]["table"][-1]["parts"][parts]))
    except StopIteration:
        return

    start = {root: 0}
    input_queue = \
        [(root, None, parts, len(dp_tree.nodes[root]["table"]) - 1, 0)]

    # a queue is a list of partial assignments with associated operations
    # left to perform on them
    queue = [(start, input_queue)]

    # each process step takes one assignment + assignment queue and processes
    # one element from the assignment queue
    def process(assignment, assignment_queue):
        try:
            # pop "real" process arguments here (the process arguments as seen
            # in the single partition implementation
            v, z, k, i, v_part_num = assignment_queue.pop()
        except IndexError:
            # if the assignment queue is empty, we're done processing this
            # and it must be a completed assignment
            return assignment
        if i == 0:
            # if i == 0, we can ignore this update, just as we returned early
            # in the single partition version. In case the queue has more
            # events, we add it back to the old queue
            queue.append((assignment, assignment_queue))
            return

        # all possible z values we must check
        z_values = [z] if z is not None else \
            [y for y in dp_tree.nodes[v]["table"][i]["parts"][k]
             if lower <= y <= upper]

        # new child vertex
        vp = dp_tree.nodes[v]["table"][i]["vertex"]

        for z in z_values:
            # loop over all possible new z and k values
            for zp, kp in dp_tree.nodes[v]["table"][i]["parts"][k][z]:
                # regardless of values, make copies of assignment and queue
                # to work with from now on
                new_a = assignment.copy()
                new_q = assignment_queue.copy()

                # same branching steps as single partition version, but now
                # using the new assignment and queue
                if zp is None:
                    new_part_num = 1 + max(new_a.values(), default=0)
                    new_a[vp] = new_part_num
                    new_q.append((v, z, kp, i - 1, v_part_num))
                    new_q.append((vp, None, k - kp,
                                  len(dp_tree.nodes[vp]["table"]) - 1,
                                  new_part_num))
                else:
                    new_a[vp] = v_part_num
                    new_q.append((v, zp, kp, i - 1, v_part_num))
                    new_q.append((vp, z - zp, k - kp + 1,
                                  len(dp_tree.nodes[vp]["table"]) - 1,
                                  v_part_num))

                # add new assignment and queue to outer queue
                queue.append((new_a, new_q))

        # possible memory optimization: del assignment and old queue here

    # continue processing outer queue, accumulating final results, until done
    # deduplication optimization:
    # probably need to reprocess every output partition as it comes to use
    # some sort of ordering that forces partitions identical up to renaming to
    # be identical, then use frozendicts to deduplicate set of outputs
    while queue:
        if assignment := process(*queue.pop()):
            yield assignment


def naive_decision(tree, key, parts, lower, upper):
    """
    Implements the decision problem variant of the naive O(p^4 u^2 n) algorithm.
    """
    dp_tree = copy(tree, key, parts, set)
    # We adopt the convention that the (k-1)th element of the dp table for a
    # node v is our current S(T_v, k).

    # Initialize T0 for k = 1
    for node, node_data in dp_tree.nodes.items():
        node_data["table"][0].add(node_data["weight"])

    # Traverse the graph bottom up, defining children as
    # already-processed neighbors
    processed = set()
    root = None
    for v in nx.dfs_postorder_nodes(dp_tree):
        children = set(dp_tree.neighbors(v)) & processed
        for child in children:
            new_table = []
            for k in range(1, parts + 1):
                s1 = flatten(cartesian_sum(
                    dp_tree.nodes[v]["table"][k_prime - 1],
                    dp_tree.nodes[child]["table"][k - k_prime]
                )
                    for k_prime in range(1, k + 1))
                s2 = flatten(
                    dp_tree.nodes[v]["table"][k_prime - 1]
                    for k_prime in range(1, k)
                    if any(map(lambda x: lower <= x <= upper,
                               dp_tree.nodes[child]["table"][k - k_prime - 1]))
                )
                new_table.append(s1 | s2)
            dp_tree.nodes[v]["table"] = new_table
        processed.add(v)
        root = v
    return any(map(lambda x: lower <= x <= upper,
                   dp_tree.nodes[root]["table"][parts - 1]))


def cartesian_sum(s1: Set, s2: Set) -> Set:
    """
    Returns the Cartesian sum (sum of all pairs of Cartesian product) of the
    input sets.
    :param s1: An input set of elements (must implement `+`).
    :param s2: A second input set of the same type as the first.
    :return: An output set of the Cartesian sum of `s1`, `s2` with the same
        type as the input sets.
    """
    return {a + b for a in s1 for b in s2}
