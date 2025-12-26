"""Lambda 表达式

@see: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

可以使用 lambda 关键字创建小型匿名函数。Lambda 函数可以在需要函数对象的任何地方使用。
它们在语法上被限制为单个表达式。从语义上讲，它们只是普通函数定义的语法糖。
像嵌套函数定义一样，lambda 函数可以引用包含作用域中的变量。
"""


def test_lambda_expressions():
    """Lambda 表达式"""

    # 这个函数返回其两个参数的和：lambda a, b: a+b
    # 像嵌套函数定义一样，lambda 函数可以引用包含作用域中的变量。

    def make_increment_function(delta):
        """这个示例使用 lambda 表达式返回一个函数"""
        return lambda number: number + delta

    increment_function = make_increment_function(42)

    assert increment_function(0) == 42
    assert increment_function(1) == 43
    assert increment_function(2) == 44

    # lambda 的另一个用途是将小函数作为参数传递。
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    # 按文本键排序 pairs。
    pairs.sort(key=lambda pair: pair[1])

    assert pairs == [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
