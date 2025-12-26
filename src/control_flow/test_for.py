"""FOR 语句

@see: https://docs.python.org/3/tutorial/controlflow.html

Python 中的 for 语句与你在 C 或 Pascal 中习惯的有所不同。
Python 的 for 语句不是总是迭代数字的算术级数（如 Pascal），
也不是让用户能够定义迭代步长和停止条件（如 C），
而是按照序列中出现的顺序迭代任何序列（列表或字符串）的项。
例如（无双关语意）：
"""


# pylint: disable=too-many-locals
def test_for_statement():
    """FOR 语句"""

    # 测量一些字符串：
    words = ['cat', 'window', 'defenestrate']
    words_length = 0

    for word in words:
        words_length += len(word)

    # "cat" 长度是 3
    # "window" 长度是 6
    # "defenestrate" 长度是 12
    assert words_length == (3 + 6 + 12)

    # 如果你需要在循环内部修改正在迭代的序列
    # （例如复制选定的项），建议你先制作一个副本。
    # 迭代序列不会隐式地制作副本。切片表示法使这特别方便：
    for word in words[:]:  # 循环遍历整个列表的切片副本。
        if len(word) > 6:
            words.insert(0, word)

    # 否则使用 for w in words:，示例将尝试创建一个无限列表，
    # 一遍又一遍地插入 defenestrate。

    assert words == ['defenestrate', 'cat', 'window', 'defenestrate']

    # 如果你确实需要迭代数字序列，内置函数 range() 会派上用场。
    # 它生成算术级数：
    iterated_numbers = []

    for number in range(5):
        iterated_numbers.append(number)

    assert iterated_numbers == [0, 1, 2, 3, 4]

    # 要迭代序列的索引，你可以如下组合 range() 和 len()：
    words = ['Mary', 'had', 'a', 'little', 'lamb']
    concatenated_string = ''

    # pylint: disable=consider-using-enumerate
    for word_index in range(len(words)):
        concatenated_string += words[word_index] + ' '

    assert concatenated_string == 'Mary had a little lamb '

    # 或者简单地使用 enumerate()。
    concatenated_string = ''

    for word_index, word in enumerate(words):
        concatenated_string += word + ' '

    assert concatenated_string == 'Mary had a little lamb '

    # 当循环遍历字典时，可以使用 items() 方法同时检索键和对应的值。
    knights_names = []
    knights_properties = []

    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for key, value in knights.items():
        knights_names.append(key)
        knights_properties.append(value)

    assert knights_names == ['gallahad', 'robin']
    assert knights_properties == ['the pure', 'the brave']

    # 当循环遍历序列时，可以使用 enumerate() 函数同时检索位置索引和对应的值
    indices = []
    values = []
    for index, value in enumerate(['tic', 'tac', 'toe']):
        indices.append(index)
        values.append(value)

    assert indices == [0, 1, 2]
    assert values == ['tic', 'tac', 'toe']

    # 要同时循环遍历两个或多个序列，可以使用 zip() 函数配对条目。
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    combinations = []

    for question, answer in zip(questions, answers):
        combinations.append('What is your {0}?  It is {1}.'.format(question, answer))

    assert combinations == [
        'What is your name?  It is lancelot.',
        'What is your quest?  It is the holy grail.',
        'What is your favorite color?  It is blue.',
    ]


def test_range_function():
    """Range 函数

    如果你确实需要迭代数字序列，内置函数 range() 会派上用场。
    它生成算术级数。

    在许多方面，range() 返回的对象表现得好像它是一个列表，但实际上它不是。
    它是一个对象，当你迭代它时返回所需序列的连续项，
    但它实际上并不创建列表，从而节省空间。

    我们说这样的对象是可迭代的，即适合作为函数和结构的目标，
    这些函数和结构期望从中获取连续的项直到供应耗尽。
    我们已经看到 for 语句就是这样一个迭代器。list() 函数是另一个；
    它从可迭代对象创建列表：
    """

    assert list(range(5)) == [0, 1, 2, 3, 4]

    # 给定的终点永远不是生成序列的一部分；range(10) 生成 10 个值，
    # 是长度为 10 的序列项的合法索引。可以让范围从另一个数字开始，
    # 或指定不同的增量（甚至是负数；有时这被称为"步长"）：

    assert list(range(5, 10)) == [5, 6, 7, 8, 9]
    assert list(range(0, 10, 3)) == [0, 3, 6, 9]
    assert list(range(-10, -100, -30)) == [-10, -40, -70]
