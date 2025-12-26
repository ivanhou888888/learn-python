"""默认参数值

@see: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values

最有用的形式是为一个或多个参数指定默认值。这创建了一个可以用比定义时
允许的更少参数调用的函数。
"""


def power_of(number, power=2):
    """将数字提升到特定的幂。

    你可能注意到默认情况下函数将数字提升到 2 次幂。
    """
    return number ** power


def test_default_function_arguments():
    """测试默认函数参数"""

    # 这个 power_of 函数可以用几种方式调用，因为它的第二个参数有默认值。
    # 首先我们可以完全省略第二个参数来调用它。
    assert power_of(3) == 9
    # 我们也可能想通过使用以下函数调用来覆盖第二个参数。
    assert power_of(3, 2) == 9
    assert power_of(3, 3) == 27
