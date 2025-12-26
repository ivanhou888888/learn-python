"""错误和异常

@see: https://docs.python.org/3/tutorial/errors.html#errors-and-exceptions

即使语句或表达式在语法上是正确的，当尝试执行它时也可能导致错误。
在执行期间检测到的错误称为异常，它们不是无条件致命的。

可以编写处理选定异常的程序。
"""


def test_handle_exceptions():
    """异常处理

    try 语句的工作方式如下。

    - 首先，执行 try 子句（try 和 except 关键字之间的语句）。

    - 如果没有发生异常，则跳过 except 子句，try 语句的执行完成。

    - 如果在执行 try 子句期间发生异常，则跳过子句的其余部分。
    然后，如果其类型与 except 关键字后面命名的异常匹配，
    则执行 except 子句，然后在 try 语句之后继续执行。

    - 如果发生的异常与 except 子句中命名的异常不匹配，
    则将其传递给外部 try 语句；如果找不到处理程序，
    则它是未处理的异常，执行停止并显示消息。
    """

    # 让我们模拟除以零异常。
    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # 除以零
        # 我们根本不应该到达这里。
        assert result
    except ZeroDivisionError:
        # 由于除以零，我们应该到达这里。
        exception_has_been_handled = True

    assert exception_has_been_handled

    # 让我们模拟未定义变量访问异常。
    exception_has_been_handled = False
    try:
        # pylint: disable=undefined-variable
        result = 4 + spam * 3  # 名称 'spam' 未定义
        # 我们根本不应该到达这里。
        assert result
    except NameError:
        # 由于除以零，我们应该到达这里。
        exception_has_been_handled = True

    assert exception_has_been_handled

    # try 语句可以有多个 except 子句，为不同的异常指定处理程序。
    # 最多执行一个处理程序。处理程序只处理相应 try 子句中发生的异常，
    # 而不处理同一 try 语句的其他处理程序中的异常。
    # except 子句可以将多个异常命名为带括号的元组，例如：

    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # 除以零
        # 我们根本不应该到达这里。
        assert result
    except (ZeroDivisionError, NameError):
        # 由于除以零，我们应该到达这里。
        exception_has_been_handled = True

    assert exception_has_been_handled

    # 异常处理程序可以链接。
    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # 除以零
        # 我们根本不应该到达这里。
        assert result
    except NameError:
        # 由于除以零，我们应该到达这里。
        exception_has_been_handled = True
    except ZeroDivisionError:
        # 由于除以零，我们应该到达这里。
        exception_has_been_handled = True

    assert exception_has_been_handled

    # try … except 语句有一个可选的 else 子句，当存在时，必须跟在所有 except 子句之后。
    # 它对于必须在 try 子句不引发异常时执行的代码很有用。例如：

    exception_has_been_handled = False
    no_exceptions_has_been_fired = False

    try:
        result = 10
        # 我们根本不应该到达这里。
        assert result
    except NameError:
        # 由于除以零，我们应该到达这里。
        exception_has_been_handled = True
    else:
        no_exceptions_has_been_fired = True

    assert not exception_has_been_handled
    assert no_exceptions_has_been_fired
