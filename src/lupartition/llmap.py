"""
A library implementing immutable, extensible maps with O(1) copy-insert
operations using linked lists.
"""

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class MapNode:
    key: Any
    value: Any
    # can annotate this with Optional[Self] in Python 3.11+
    next_node: Optional["MapNode"] = None


class LinkedListMapIterator:
    def __init__(self, curr_node):
        self.curr_node = curr_node

    def __next__(self):
        if self.curr_node is None:
            raise StopIteration
        else:
            k, v = self.curr_node.key, self.curr_node.value
            self.curr_node = self.curr_node.next_node
            return k, v


class LinkedListMap:
    def __init__(self, root=None):
        self.root = root

    def insert(self, key, value):
        return LinkedListMap(MapNode(key, value, self.root))

    def __iter__(self):
        return LinkedListMapIterator(self.root)

    def dict(self):
        return {k: v for k, v in self}


class LinkedListMaxMap(LinkedListMap):
    def __init__(self, acc, root=None):
        super().__init__(root)
        self.acc = acc

    def insert(self, key, value):
        return LinkedListMaxMap(max(self.acc, value),
                                MapNode(key, value, self.root))

    def max(self):
        return self.acc
