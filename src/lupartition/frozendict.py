class FrozenDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hash_value = None

    def __hash__(self):
        if self.hash_value is None:
            self.hash_value = hash(frozenset(self.items()))
        return self.hash_value

    def __setitem__(self, key, value):
        raise TypeError("FrozenDict does not support assignment.")

    def insert(self, key, value):
        c = super().copy()
        c[key] = value
        return FrozenDict(c)

    def copy(self):
        return FrozenDict(super().copy())
