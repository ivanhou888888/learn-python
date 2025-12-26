"""生成器

@see: https://www.learnpython.org/en/Generators

生成器用于创建迭代器，但使用不同的方法。生成器是简单的函数，
以特殊的方式一次返回一个可迭代的项集合。

当使用 for 语句开始对一组项进行迭代时，生成器运行。
一旦生成器的函数代码到达 "yield" 语句，生成器就会将其执行返回给 for 循环，
从集合中返回一个新值。生成器函数可以生成任意多的值（可能是无限的），
依次产生每一个。
"""

import random


def lottery():
    """生成器函数示例。

    这是一个返回随机整数的生成器函数的简单示例。
    这个函数自己决定如何生成随机数，并一次执行一个 yield 语句，
    在两者之间暂停以将执行返回给主 for 循环。
    """
    # 返回 1 到 10 之间的前 3 个随机数
    # pylint: disable=unused-variable
    for _ in range(3):
        yield random.randint(1, 10)

    # 返回 10 到 20 之间的第 4 个数
    yield random.randint(10, 20)


def test_generators():
    """Yield 语句"""
    for number_index, random_number in enumerate(lottery()):
        if number_index < 3:
            assert 0 <= random_number <= 10
        else:
            assert 10 <= random_number <= 20
