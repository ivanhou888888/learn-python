"""逻辑运算符

@see: https://www.w3schools.com/python/python_operators.asp

逻辑运算符用于组合条件语句。
"""


def test_logical_operators():
    """逻辑运算符"""

    # 让我们用这些数字来说明逻辑运算符。
    first_number = 5
    second_number = 10

    # and
    # 如果两个语句都为真，则返回 True。
    assert first_number > 0 and second_number < 20

    # or
    # 如果其中一个语句为真，则返回 True
    assert first_number > 5 or second_number < 20

    # not
    # 反转结果，如果结果为真则返回 False。
    # pylint: disable=unneeded-not
    assert not first_number == second_number
    assert first_number != second_number
