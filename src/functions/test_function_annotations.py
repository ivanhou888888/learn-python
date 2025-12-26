"""函数注解

@see: https://docs.python.org/3/tutorial/controlflow.html#function-annotations

函数注解是关于用户定义函数使用的类型的完全可选的元数据信息。

注解作为字典存储在函数的 __annotations__ 属性中，
对函数的任何其他部分没有影响。参数注解通过参数名后的冒号定义，
后跟一个求值为注解值的表达式。返回注解通过字面量 -> 定义，
后跟一个表达式，位于参数列表和表示 def 语句结束的冒号之间。
"""


def breakfast(ham: str, eggs: str = 'eggs') -> str:
    """早餐创建器。

    这个函数有一个位置参数、一个关键字参数和带注解的返回值。
    """
    return ham + ' and ' + eggs


def test_function_annotations():
    """函数注解。"""

    assert breakfast.__annotations__ == {'eggs': str, 'ham': str, 'return': str}
