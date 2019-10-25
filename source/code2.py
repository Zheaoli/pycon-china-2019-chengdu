import functools
import types


def demo_wrap(func):
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        func(*args, **kwargs)

    return wraps


class DemoMeta(type):
    def __new__(cls, name, bases, dict):
        for key, item in dict.items():
            if "abc" in key and isinstance(item, types.FunctionType):
                dict[key] = demo_wrap(item)
        return super().__new__(cls, name, bases, dict)
    # def __init__(cls, name, bases, dict):
    #     print(cls.abc)


class Demo(metaclass=DemoMeta):
    def abc(self):
        return 1

    def _abc(self):
        return 1


print(Demo().abc())
