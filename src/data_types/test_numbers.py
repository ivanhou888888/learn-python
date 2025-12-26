"""数字

@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_numbers.asp

Python 中有三种数字类型：
- int（整数，例如 2, 4, 20）
    - bool（布尔值，例如 False 和 True，表现为 0 和 1）
- float（浮点数，例如 5.0, 1.6）
- complex（复数，例如 5+6j, 4-3j）
"""


def test_integer_numbers():
    """整数类型

    int，即整数，是一个没有小数的正数或负数，
    长度不受限制。
    """

    positive_integer = 1
    negative_integer = -3255522
    big_integer = 35656222554887711

    assert isinstance(positive_integer, int)
    assert isinstance(negative_integer, int)
    assert isinstance(big_integer, int)


def test_booleans():
    """布尔类型

    布尔值表示真值 False 和 True。表示 False 和 True 值的两个对象
    是仅有的布尔对象。布尔类型是整数类型的子类型，
    布尔值在几乎所有上下文中的行为都像值 0 和 1，
    唯一的例外是当转换为字符串时，分别返回字符串 "False" 或 "True"。
    """

    true_boolean = True
    false_boolean = False

    assert true_boolean
    assert not false_boolean

    assert isinstance(true_boolean, bool)
    assert isinstance(false_boolean, bool)

    # 尝试将布尔值转换为字符串。
    assert str(true_boolean) == "True"
    assert str(false_boolean) == "False"


def test_float_numbers():
    """浮点类型

    float，即"浮点数"，是一个包含一个或多个小数的正数或负数。
    """

    float_number = 7.0
    # 声明浮点数的另一种方式是使用 float() 函数。
    float_number_via_function = float(7)
    float_negative = -35.59

    assert float_number == float_number_via_function
    assert isinstance(float_number, float)
    assert isinstance(float_number_via_function, float)
    assert isinstance(float_negative, float)

    # 浮点数也可以是科学计数法，使用 "e" 表示 10 的幂。
    float_with_small_e = 35e3
    float_with_big_e = 12E4

    assert float_with_small_e == 35000
    assert float_with_big_e == 120000
    assert isinstance(12E4, float)
    assert isinstance(-87.7e100, float)


def test_complex_numbers():
    """复数类型"""

    complex_number_1 = 5 + 6j
    complex_number_2 = 3 - 2j

    assert isinstance(complex_number_1, complex)
    assert isinstance(complex_number_2, complex)
    assert complex_number_1 * complex_number_2 == 27 + 8j


def test_number_operators():
    """基本运算"""

    # 加法。
    assert 2 + 4 == 6

    # 乘法。
    assert 2 * 4 == 8

    # 除法总是返回浮点数。
    assert 12 / 3 == 4.0
    assert 12 / 5 == 2.4
    assert 17 / 3 == 5.666666666666667

    # 取模运算符返回除法的余数。
    assert 12 % 3 == 0
    assert 13 % 3 == 1

    # 整除会舍弃小数部分。
    assert 17 // 3 == 5

    # 将数字提升到特定的幂。
    assert 5 ** 2 == 25  # 5 的平方
    assert 2 ** 7 == 128  # 2 的 7 次方

    # 完全支持浮点数；混合类型操作数的运算符
    # 会将整数操作数转换为浮点数。
    assert 4 * 3.75 - 1 == 14.0
