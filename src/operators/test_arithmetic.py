"""算术运算符

@see: https://www.w3schools.com/python/python_operators.asp

算术运算符与数值一起使用，执行常见的数学运算
"""


def test_arithmetic_operators():
    """算术运算符"""

    # 加法。
    assert 5 + 3 == 8

    # 减法。
    assert 5 - 3 == 2

    # 乘法。
    assert 5 * 3 == 15
    assert isinstance(5 * 3, int)

    # 除法。
    # 除法的结果是浮点数。
    assert 5 / 3 == 1.6666666666666667
    assert 8 / 4 == 2
    assert isinstance(5 / 3, float)
    assert isinstance(8 / 4, float)

    # 取模。
    assert 5 % 3 == 2

    # 幂运算。
    assert 5 ** 3 == 125
    assert 2 ** 3 == 8
    assert 2 ** 4 == 16
    assert 2 ** 5 == 32
    assert isinstance(5 ** 3, int)

    # 整除。
    assert 5 // 3 == 1
    assert 6 // 3 == 2
    assert 7 // 3 == 2
    assert 9 // 3 == 3
    assert isinstance(5 // 3, int)
