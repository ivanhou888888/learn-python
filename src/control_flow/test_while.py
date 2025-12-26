"""WHILE 语句

@see: https://docs.python.org/3/tutorial/controlflow.html
@see: https://docs.python.org/3/reference/compound_stmts.html#the-while-statement

while 循环在条件保持为真时执行。在 Python 中，像在 C 中一样，
任何非零整数值都是真；零是假。条件也可以是字符串或列表值，
实际上是任何序列；任何长度非零的都是真，空序列是假。

示例中使用的测试是一个简单的比较。标准比较运算符的写法与 C 相同：
<（小于）、>（大于）、==（等于）、<=（小于或等于）、>=（大于或等于）
和 !=（不等于）。
"""


def test_while_statement():
    """WHILE 语句"""

    # 让我们使用 while 循环将数字提升到某个幂。
    number = 2
    power = 5

    result = 1

    while power > 0:
        result *= number
        power -= 1

    # 2^5 = 32
    assert result == 32
