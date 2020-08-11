class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts[item] = counts.get(item, 0) + 1
        return counts


foo = FrequencyList(["a", "b", "c", "a"])
print(len(foo))
print(foo.frequency())
print(foo[0])


class CustomList:
    def __init__(self, data):
        self.l = data

    def __getitem__(self, index):
        return self.l[index]


bar = CustomList(["a", "b", "c", "a"])
print(bar[2])
