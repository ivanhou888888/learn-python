"""元组

@see: https://www.w3schools.com/python/python_tuples.asp
@see: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

元组是一个有序且不可更改的集合。在 Python 中，元组用圆括号编写。

元组具有以下属性：
- 你不能更改元组中的值。
- 你不能删除元组中的项。
"""

import pytest


def test_tuples():
    """元组"""
    fruits_tuple = ("apple", "banana", "cherry")

    assert isinstance(fruits_tuple, tuple)
    assert fruits_tuple[0] == "apple"
    assert fruits_tuple[1] == "banana"
    assert fruits_tuple[2] == "cherry"

    # 你不能更改元组中的值。
    with pytest.raises(Exception):
        # pylint: disable=unsupported-assignment-operation
        fruits_tuple[0] = "pineapple"

    # 也可以使用 tuple() 构造函数来创建元组（注意双圆括号）。
    # len() 函数返回元组的长度。
    fruits_tuple_via_constructor = tuple(("apple", "banana", "cherry"))

    assert isinstance(fruits_tuple_via_constructor, tuple)
    assert len(fruits_tuple_via_constructor) == 3

    # 初始化元组时也可以省略括号。
    another_tuple = 12345, 54321, 'hello!'
    assert another_tuple == (12345, 54321, 'hello!')

    # 元组可以嵌套：
    nested_tuple = another_tuple, (1, 2, 3, 4, 5)
    assert nested_tuple == ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

    # 如你所见，输出时元组总是用括号括起来，以便正确解释嵌套元组；
    # 输入时可以带或不带括号，尽管通常括号是必要的
    # （如果元组是更大表达式的一部分）。不能给元组的单个项赋值，
    # 但是可以创建包含可变对象（如列表）的元组。

    # 一个特殊的问题是构造包含 0 或 1 个项的元组：语法有一些额外的怪癖来适应这些。
    # 空元组由一对空括号构造；包含一个项的元组通过在值后面加逗号来构造
    # （仅用括号括起单个值是不够的）。丑陋，但有效。例如：
    empty_tuple = ()
    # pylint: disable=len-as-condition
    assert len(empty_tuple) == 0

    # pylint: disable=trailing-comma-tuple
    singleton_tuple = 'hello',  # <-- 注意尾随逗号
    assert len(singleton_tuple) == 1
    assert singleton_tuple == ('hello',)

    # 以下示例称为元组打包：
    packed_tuple = 12345, 54321, 'hello!'

    # 反向操作也是可能的。
    first_tuple_number, second_tuple_number, third_tuple_string = packed_tuple
    assert first_tuple_number == 12345
    assert second_tuple_number == 54321
    assert third_tuple_string == 'hello!'

    # 这被恰当地称为序列解包，适用于右侧的任何序列。
    # 序列解包要求等号左侧的变量数量与序列中的元素数量相同。
    # 注意，多重赋值实际上只是元组打包和序列解包的组合。

    # 使用元组交换。
    # 在 Python 中，可以使用元组将数据从一个变量交换到另一个变量。
    # 这消除了使用 'temp' 变量的需要。
    first_number = 123
    second_number = 456
    first_number, second_number = second_number, first_number

    assert first_number == 456
    assert second_number == 123
