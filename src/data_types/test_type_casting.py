"""类型转换

@see: https://www.w3schools.com/python/python_casting.asp

有时你可能想要为变量指定一个类型。这可以通过类型转换来完成。
Python 是一种面向对象的语言，因此它使用类来定义数据类型，
包括其原始类型。

因此，Python 中的类型转换是使用构造函数完成的：

- int() - 从整数字面量、浮点字面量（通过向下取整到前一个整数）
或字符串字面量（前提是字符串表示一个整数）构造一个整数

- float() - 从整数字面量、浮点字面量或字符串字面量
（前提是字符串表示一个浮点数或整数）构造一个浮点数

- str() - 从各种数据类型构造一个字符串，包括字符串、
整数字面量和浮点字面量
"""


def test_type_casting_to_integer():
    """类型转换为整数"""

    assert int(1) == 1
    assert int(2.8) == 2
    assert int('3') == 3


def test_type_casting_to_float():
    """类型转换为浮点数"""

    assert float(1) == 1.0
    assert float(2.8) == 2.8
    assert float("3") == 3.0
    assert float("4.2") == 4.2


def test_type_casting_to_string():
    """类型转换为字符串"""

    assert str("s1") == 's1'
    assert str(2) == '2'
    assert str(3.0) == '3.0'
