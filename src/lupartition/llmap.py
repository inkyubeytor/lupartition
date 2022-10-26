"""
A library implementing immutable, extensible maps with O(1) copy-insert
operations using linked lists.
"""

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    data: Any
    # can annotate this with Optional[Self] in Python 3.11+
    next_node: Optional["Node"] = None


class LinkedListIterator:
    def __init__(self, curr_node):
        self.curr_node = curr_node

    def __next__(self):
        if self.curr_node is None:
            raise StopIteration
        else:
            d = self.curr_node.data
            self.curr_node = self.curr_node.next_node
            return d


class LinkedList:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        return LinkedList(Node(data, self.root))

    def __iter__(self):
        return LinkedListIterator(self.root)

    def pop(self):
        if self.root is None:
            raise IndexError
        data = self.root.data
        self.root = self.root.next_node
        return data


class LinkedListMaxMap(LinkedList):
    def __init__(self, acc, root=None):
        super().__init__(root)
        self.acc = acc

    def insert(self, data):
        raise NotImplementedError

    def assign(self, key, value):
        return LinkedListMaxMap(max(self.acc, value),
                                Node((key, value), self.root))

    def max(self):
        return self.acc

    def to_dict(self):
        return {k: v for k, v in self}
