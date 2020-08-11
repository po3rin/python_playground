class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print(name)
        return type.__new__(meta, name, bases, class_dict)


class MyClass(metaclass=Meta):
    stuff = None

    def foo(self):
        pass

    def __init_subclass__(cls):
        print(cls.stuff)


class MySubClass(MyClass):
    other = 567
    stuff = 2222

    def barfoo(self):
        pass
