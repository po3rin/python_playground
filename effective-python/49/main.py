import json


class Serialize:
    def __init__(self, *args):
        self.args = args

    def serialze(self):
        return json.dumps({"args": self.args})


class Point2D(Serialize):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D({self.x},{self.y})"


# p = Point2D(5, 3)
# print(p)
# print(p.serialze())


class Deserialize(Serialize):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params["args"])


class BetterPoint2D(Deserialize):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D({self.x},{self.y})"


before = BetterPoint2D(5, 3)
print(before)

data = before.serialze()
print(data)

after = BetterPoint2D(5, 3)
print(after)
