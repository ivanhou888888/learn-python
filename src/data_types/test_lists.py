"""列表

# @see: https://www.learnpython.org/en/Lists
# @see: https://docs.python.org/3/tutorial/introduction.html
# @ee: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

Python 有多种复合数据类型，用于将其他值组合在一起。
最通用的是列表，它可以写成方括号之间用逗号分隔的值（项）的列表。
列表可能包含不同类型的项，但通常所有项都具有相同的类型。
"""

import pytest


def test_list_type():
    """列表类型"""

    # 列表与数组非常相似。它们可以包含任何类型的变量，
    # 并且可以包含任意数量的变量。列表也可以以非常简单的方式进行迭代。
    # 这是一个如何构建列表的示例。
    squares = [1, 4, 9, 16, 25]

    assert isinstance(squares, list)

    # 像字符串（和所有其他内置序列类型）一样，列表可以被索引和切片：
    assert squares[0] == 1  # 索引返回该项
    assert squares[-1] == 25
    assert squares[-3:] == [9, 16, 25]  # 切片返回一个新列表

    # 所有切片操作都返回一个包含请求元素的新列表。
    # 这意味着以下切片返回列表的一个新的（浅）副本：
    assert squares[:] == [1, 4, 9, 16, 25]

    # 列表还支持连接等操作：
    assert squares + [36, 49, 64, 81, 100] == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # 与不可变的字符串不同，列表是可变类型，
    # 即可以更改其内容：
    cubes = [1, 8, 27, 65, 125]  # 这里有问题，4 的立方是 64！
    cubes[3] = 64  # 替换错误的值
    assert cubes == [1, 8, 27, 64, 125]

    # 你也可以使用 append() 方法在列表末尾添加新项
    cubes.append(216)  # 添加 6 的立方
    cubes.append(7 ** 3)  # 和 7 的立方
    assert cubes == [1, 8, 27, 64, 125, 216, 343]

    # 也可以对切片进行赋值，这甚至可以改变列表的大小或完全清空它：
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    letters[2:5] = ['C', 'D', 'E']  # 替换一些值
    assert letters == ['a', 'b', 'C', 'D', 'E', 'f', 'g']
    letters[2:5] = []  # 现在删除它们
    assert letters == ['a', 'b', 'f', 'g']
    # 通过用空列表替换所有元素来清空列表
    letters[:] = []
    assert letters == []

    # 内置函数 len() 也适用于列表
    letters = ['a', 'b', 'c', 'd']
    assert len(letters) == 4

    # 可以嵌套列表（创建包含其他列表的列表），例如：
    list_of_chars = ['a', 'b', 'c']
    list_of_numbers = [1, 2, 3]
    mixed_list = [list_of_chars, list_of_numbers]
    assert mixed_list == [['a', 'b', 'c'], [1, 2, 3]]
    assert mixed_list[0] == ['a', 'b', 'c']
    assert mixed_list[0][1] == 'b'


def test_list_methods():
    """测试列表方法"""

    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.append(x)
    # 在列表末尾添加一个项。
    # 等同于 a[len(a):] = [x]。
    fruits.append('grape')
    assert fruits == ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'grape']

    # list.remove(x)
    # 从列表中删除第一个值等于 x 的项。
    # 如果没有这样的项，则引发 ValueError。
    fruits.remove('grape')
    assert fruits == ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    with pytest.raises(Exception):
        fruits.remove('not existing element')

    # list.insert(i, x)
    # 在给定位置插入一个项。第一个参数是要插入的元素之前的索引，
    # 所以 a.insert(0, x) 在列表前面插入，
    # a.insert(len(a), x) 等同于 a.append(x)。
    fruits.insert(0, 'grape')
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.index(x[, start[, end]])
    # 返回列表中第一个值等于 x 的项的从零开始的索引。
    # 如果没有这样的项，则引发 ValueError。
    # 可选参数 start 和 end 按切片表示法解释，用于将搜索限制在列表的特定子序列。
    # 返回的索引是相对于完整序列的开头计算的，而不是 start 参数。
    assert fruits.index('grape') == 0
    assert fruits.index('orange') == 1
    assert fruits.index('banana') == 4
    assert fruits.index('banana', 5) == 7  # 从位置 5 开始查找下一个 banana

    with pytest.raises(Exception):
        fruits.index('not existing element')

    # list.count(x)
    # 返回 x 在列表中出现的次数。
    assert fruits.count('tangerine') == 0
    assert fruits.count('banana') == 2

    # list.copy()
    # 返回列表的浅副本。等同于 a[:]。
    fruits_copy = fruits.copy()
    assert fruits_copy == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.reverse()
    # 原地反转列表中的元素。
    fruits_copy.reverse()
    assert fruits_copy == [
        'banana',
        'apple',
        'kiwi',
        'banana',
        'pear',
        'apple',
        'orange',
        'grape',
    ]

    # list.sort(key=None, reverse=False)
    # 原地对列表中的项进行排序（参数可用于排序自定义，
    # 参见 sorted() 了解其解释）。
    fruits_copy.sort()
    assert fruits_copy == [
        'apple',
        'apple',
        'banana',
        'banana',
        'grape',
        'kiwi',
        'orange',
        'pear',
    ]

    # list.pop([i])
    # 删除列表中给定位置的项，并返回它。如果没有指定索引，
    # a.pop() 删除并返回列表中的最后一项。（方法签名中 i 周围的方括号
    # 表示该参数是可选的，而不是你应该在该位置键入方括号。）
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    assert fruits.pop() == 'banana'
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']

    # list.clear()
    # 从列表中删除所有项。等同于 del a[:]。
    fruits.clear()
    assert fruits == []


def test_del_statement():
    """del 语句

    有一种方法可以根据索引而不是值从列表中删除项：del 语句。
    这与返回值的 pop() 方法不同。del 语句也可用于从列表中删除切片
    或清空整个列表（我们之前通过将空列表赋值给切片来完成）。
    """

    numbers = [-1, 1, 66.25, 333, 333, 1234.5]

    del numbers[0]
    assert numbers == [1, 66.25, 333, 333, 1234.5]

    del numbers[2:4]
    assert numbers == [1, 66.25, 1234.5]

    del numbers[:]
    assert numbers == []

    # del 也可用于删除整个变量：
    del numbers
    with pytest.raises(Exception):
        # 此后引用名称 a 是一个错误（至少在另一个值被赋给它之前）。
        assert numbers == []  # noqa: F821


def test_list_comprehensions():
    """列表推导式

    列表推导式提供了一种简洁的方式来创建列表。常见的应用是创建新列表，
    其中每个元素是对另一个序列或可迭代对象的每个成员应用某些操作的结果，
    或者创建满足特定条件的那些元素的子序列。

    列表推导式由包含表达式的方括号组成，后跟一个 for 子句，
    然后是零个或多个 for 或 if 子句。结果将是一个新列表，
    由在其后的 for 和 if 子句的上下文中评估表达式得到。
    """

    # 例如，假设我们想创建一个平方数列表，如：
    squares = []
    for number in range(10):
        squares.append(number ** 2)

    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 注意这会创建（或覆盖）一个名为 "number" 的变量，
    # 该变量在循环完成后仍然存在。我们可以在没有任何副作用的情况下计算平方数列表：
    squares = list(map(lambda x: x ** 2, range(10)))
    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 或者，等效地（更简洁和可读）：
    squares = [x ** 2 for x in range(10)]
    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 例如，如果两个列表的元素不相等，此列表推导式会组合它们。
    combinations = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    # 它等同于：
    combinations = []
    for first_number in [1, 2, 3]:
        for second_number in [3, 1, 4]:
            if first_number != second_number:
                combinations.append((first_number, second_number))

    assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    # 注意这两个代码片段中 for 和 if 语句的顺序是相同的。

    # 如果表达式是一个元组（例如前面示例中的 (x, y)），
    # 它必须加括号。

    # 让我们看更多示例：

    vector = [-4, -2, 0, 2, 4]

    # 创建一个值翻倍的新列表。
    doubled_vector = [x * 2 for x in vector]
    assert doubled_vector == [-8, -4, 0, 4, 8]

    # 过滤列表以排除负数。
    positive_vector = [x for x in vector if x >= 0]
    assert positive_vector == [0, 2, 4]

    # 对所有元素应用函数。
    abs_vector = [abs(x) for x in vector]
    assert abs_vector == [4, 2, 0, 2, 4]

    # 对每个元素调用方法。
    fresh_fruit = ['  banana', '  loganberry ', 'passion fruit  ']
    clean_fresh_fruit = [weapon.strip() for weapon in fresh_fruit]
    assert clean_fresh_fruit == ['banana', 'loganberry', 'passion fruit']

    # 创建一个 2 元组列表，如 (number, square)。
    square_tuples = [(x, x ** 2) for x in range(6)]
    assert square_tuples == [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

    # 使用带有两个 'for' 的列表推导式展平列表。
    vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flatten_vector = [num for elem in vector for num in elem]
    assert flatten_vector == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_nested_list_comprehensions():
    """嵌套列表推导式

    列表推导式中的初始表达式可以是任意表达式，包括另一个列表推导式。
    """

    # 考虑以下示例，一个 3x4 矩阵实现为 3 个长度为 4 的列表的列表：
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    # 以下列表推导式将转置行和列：
    transposed_matrix = [[row[i] for row in matrix] for i in range(4)]
    assert transposed_matrix == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # 正如我们在上一节中看到的，嵌套的列表推导式是在其后的 for 的上下文中评估的，
    # 所以这个示例等同于：
    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])

    assert transposed == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # 这又与以下相同：
    transposed = []
    for i in range(4):
        # 以下 3 行实现了嵌套的列表推导式
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)

    assert transposed == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # 在实际应用中，你应该优先使用内置函数而不是复杂的流程语句。
    # zip() 函数在这个用例中会做得很好：
    assert list(zip(*matrix)) == [
        (1, 5, 9),
        (2, 6, 10),
        (3, 7, 11),
        (4, 8, 12),
    ]
