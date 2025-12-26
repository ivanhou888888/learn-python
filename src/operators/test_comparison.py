"""比较运算符

@see: https://www.w3schools.com/python/python_operators.asp

比较运算符用于比较两个值。
"""


def test_comparison_operators():
    """比较运算符"""

    # 等于。
    number = 5
    assert number == 5

    # 不等于。
    number = 5
    assert number != 3

    # 大于。
    number = 5
    assert number > 3

    # 小于。
    number = 5
    assert number < 8

    # 大于或等于
    number = 5
    assert number >= 5
    assert number >= 4

    # 小于或等于
    number = 5
    assert number <= 5
    assert number <= 6
