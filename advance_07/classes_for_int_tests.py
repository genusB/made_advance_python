class NumberInt:
    value = 5

    def __int__(self):
        return self.value


class NumberIndex:
    value = 5

    def __index__(self):
        return self.value
