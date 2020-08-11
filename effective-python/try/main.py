class A:
    def __init__(self, a):
        self.a = a

    def print(self):
        print(a)

    @classmethod
    def cm(cls, a):
        return cls(a)


a = "aa"
c = A.cm(a)
c.print()
