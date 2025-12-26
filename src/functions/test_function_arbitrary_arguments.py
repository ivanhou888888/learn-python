"""任意参数列表

@see: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists

函数可以用任意数量的参数调用。这些参数将被包装在一个元组中。
在可变数量的参数之前，可以有零个或多个普通参数。
"""


def test_function_arbitrary_arguments():
    """任意参数列表"""

    # 当存在形如 **name 的最终形式参数时，它接收一个字典，
    # 包含除了与形式参数对应的所有关键字参数。
    # 这可以与形如 *name 的形式参数结合使用，后者接收一个元组，
    # 包含形式参数列表之外的位置参数。
    # （*name 必须出现在 **name 之前。）例如，如果我们定义这样一个函数：
    def test_function(first_param, *arguments):
        """这个函数通过 "arguments" 元组接收其参数"""
        assert first_param == 'first param'
        assert arguments == ('second param', 'third param')

    test_function('first param', 'second param', 'third param')

    # 通常，这些可变参数将在形式参数列表的最后，因为它们会收集
    # 传递给函数的所有剩余输入参数。*args 参数之后出现的任何形式参数
    # 都是"仅关键字"参数，这意味着它们只能用作关键字而不是位置参数。
    def concat(*args, sep='/'):
        return sep.join(args)

    assert concat('earth', 'mars', 'venus') == 'earth/mars/venus'
    assert concat('earth', 'mars', 'venus', sep='.') == 'earth.mars.venus'
