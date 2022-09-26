class CustomList(list):
    def __eq__(self, other):
        return len(self) == len(other)

    def __str__(self):
        if len(self) == 0:
            return "0"
        return " ".join(str(el) for el in self) + " " + str(sum(self))

    def __sub__(self, other):
        if other is not CustomList:
            other = CustomList(other)
        res = []
        i = 0
        while i < len(self) and i < len(other):
            res.append(self[i] - other[i])
            i += 1

        res.extend(self[i:] or [val * -1 for val in other[i:]])
        return CustomList(res)

    def __rsub__(self, other):
        return CustomList(other) - self

    def __add__(self, other):
        res = []
        i = 0
        while i < len(self) and i < len(other):
            res.append(self[i] + other[i])
            i += 1

        res.extend(self[i:] or other[i:])
        return CustomList(res)

    def __radd__(self, other):
        return self + CustomList(other)
