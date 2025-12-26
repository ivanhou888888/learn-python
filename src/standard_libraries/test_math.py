"""数学运算

@see: https://docs.python.org/3/tutorial/stdlib.html#mathematics

math 模块很有用，因为许多数学函数已经实现并优化。
"""

import math
import random
import statistics


def test_math():
    """数学运算。

    math 模块提供对底层 C 库函数的访问，用于浮点数学运算。
    """
    assert math.cos(math.pi / 4) == 0.70710678118654757
    assert math.log(1024, 2) == 10.0


def test_random():
    """随机数。

    random 模块提供进行随机选择的工具。
    """

    # 从列表中随机选择。
    random_options = ['apple', 'pear', 'banana']
    random_choice = random.choice(random_options)  # 例如 'apple'
    assert random_choice in random_options

    # 无放回抽样。
    random_sample = random.sample(range(100), 10)  # 例如 [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
    for sample in random_sample:
        assert 0 <= sample <= 100

    # 选择随机数。
    random_float = random.random()  # 例如 0.17970987693706186
    assert 0 <= random_float <= 1

    # 从 range(6) 中选择的随机整数
    random_integer = random.randrange(6)  # 例如 4
    assert 0 <= random_integer <= 6


def test_statistics():
    """统计。

    statistics 模块计算数值数据的基本统计属性（均值、中位数、方差等）。
    """

    data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

    assert statistics.mean(data) == 1.6071428571428572
    assert statistics.median(data) == 1.25
    assert statistics.variance(data) == 1.3720238095238095
