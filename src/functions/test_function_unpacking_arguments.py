"""参数列表解包

@see: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists

参数解包可以通过 * 和 ** 运算符执行。详情见下文。
"""


def test_function_unpacking_arguments():
    """参数列表解包"""

    # 当参数已经在列表或元组中，但需要为需要单独位置参数的函数调用解包时，
    # 可能会出现这种情况。例如，内置的 range() 函数期望单独的 start 和 stop 参数。
    # 如果它们不是单独可用的，可以使用 *-运算符编写函数调用，
    # 从列表或元组中解包参数：

    # 使用单独参数的正常调用：
    assert list(range(3, 6)) == [3, 4, 5]

    # 使用从列表解包的参数调用。
    arguments_list = [3, 6]
    assert list(range(*arguments_list)) == [3, 4, 5]

    # 同样，字典可以使用 **-运算符传递关键字参数：
    def function_that_receives_names_arguments(first_word, second_word):
        return first_word + ', ' + second_word + '!'

    arguments_dictionary = {'first_word': 'Hello', 'second_word': 'World'}
    assert function_that_receives_names_arguments(**arguments_dictionary) == 'Hello, World!'
