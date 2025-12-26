"""PASS 语句

@see: https://docs.python.org/3/tutorial/controlflow.html

pass 语句什么都不做。当语法上需要语句但程序不需要任何操作时，可以使用它。
"""


def test_pass_in_function():
    """函数中的 PASS 语句

    当你在编写新代码时，"Pass" 可以用作函数或条件体的占位符，
    允许你在更抽象的层面上继续思考。

    下面的 pass 语句被静默忽略，但它使当前的 test_pass() 函数有效。
    """
    pass


def test_pass_in_loop():
    """循环中的 PASS。

    当语法上需要语句但程序不需要任何操作时，可以使用 "Pass"。例如：
    """

    # pylint: disable=unused-variable
    for number in range(100):
        # 它什么都不做，但 for 循环仍然有效。
        pass

    # 上面的例子相当无用，但它只是为了说明这个想法。
    # 更有用的例子可能是：
    #
    # while True:
    #   pass  # 忙等待键盘中断 (Ctrl+C)


# pylint: disable=too-few-public-methods
class MyEmptyClass:
    """类中的 PASS 语句

    "Pass" 通常用于创建像当前这样的最小类。
    """
    pass
