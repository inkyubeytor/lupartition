class FrozenDict(dict):
    def __hash__(self):
        return hash(frozenset(self.items()))

    def __setitem__(self, key, value):
        raise TypeError("FrozenDict does not support assignment.")

    def insert(self, key, value):
        c = super().copy()
        c[key] = value
        return FrozenDict(c)

    def copy(self):
        return FrozenDict(super().copy())
