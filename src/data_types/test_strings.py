"""字符串

@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_strings.asp
@see: https://www.w3schools.com/python/python_ref_string.asp

除了数字，Python 还可以操作字符串，字符串可以用多种方式表示。
它们可以用单引号 ('...') 或双引号 ("...") 括起来，结果相同。
"""

import pytest


def test_string_type():
    """字符串类型"""

    # 使用双引号的字符串。
    name_1 = "John"
    # 使用单引号的字符串。
    name_2 = 'John'
    # 使用不同类型引号创建的字符串被视为相同。
    assert name_1 == name_2
    assert isinstance(name_1, str)
    assert isinstance(name_2, str)

    # \ 可用于转义引号。
    # 使用 \' 转义单引号，或者改用双引号。
    single_quote_string = 'doesn\'t'
    double_quote_string = "doesn't"

    assert single_quote_string == double_quote_string

    # \n 表示换行。
    multiline_string = 'First line.\nSecond line.'
    # 不使用 print() 时，\n 会包含在输出中。
    # 但使用 print() 时，\n 会产生新行。
    assert multiline_string == 'First line.\nSecond line.'

    # 字符串可以被索引，第一个字符的索引为 0。
    # 没有单独的字符类型；字符只是长度为 1 的字符串。
    # 注意，由于 -0 与 0 相同，负索引从 -1 开始。
    word = 'Python'
    assert word[0] == 'P'  # 第一个字符。
    assert word[5] == 'n'  # 第五个字符。
    assert word[-1] == 'n'  # 最后一个字符。
    assert word[-2] == 'o'  # 倒数第二个字符。
    assert word[-6] == 'P'  # 从末尾数第六个或从开头数第零个。

    assert isinstance(word[0], str)

    # 除了索引，还支持切片。索引用于获取单个字符，
    # 而切片允许你获取子字符串：
    assert word[0:2] == 'Py'  # 从位置 0（包含）到 2（不包含）的字符。
    assert word[2:5] == 'tho'  # 从位置 2（包含）到 5（不包含）的字符。

    # 注意开始位置总是包含的，结束位置总是不包含的。
    # 这确保了 s[:i] + s[i:] 总是等于 s：
    assert word[:2] + word[2:] == 'Python'
    assert word[:4] + word[4:] == 'Python'

    # 切片索引有有用的默认值；省略的第一个索引默认为零，
    # 省略的第二个索引默认为被切片字符串的大小。
    assert word[:2] == 'Py'  # 从开头到位置 2（不包含）的字符。
    assert word[4:] == 'on'  # 从位置 4（包含）到末尾的字符。
    assert word[-2:] == 'on'  # 从倒数第二个（包含）到末尾的字符。

    # 记住切片工作方式的一种方法是将索引视为指向字符之间，
    # 第一个字符的左边缘编号为 0。然后，n 个字符的字符串的
    # 最后一个字符的右边缘索引为 n，例如：
    #
    # +---+---+---+---+---+---+
    #  | P | y | t | h | o | n |
    #  +---+---+---+---+---+---+
    #  0   1   2   3   4   5   6
    # -6  -5  -4  -3  -2  -1

    # 尝试使用过大的索引会导致错误。
    with pytest.raises(Exception):
        not_existing_character = word[42]
        assert not not_existing_character

    # 然而，超出范围的切片索引在切片时会被优雅地处理：
    assert word[4:42] == 'on'
    assert word[42:] == ''

    # Python 字符串不能被修改——它们是不可变的。因此，
    # 给字符串中的索引位置赋值会导致错误：
    with pytest.raises(Exception):
        # pylint: disable=unsupported-assignment-operation
        word[0] = 'J'

    # 如果你需要不同的字符串，应该创建一个新的：
    assert 'J' + word[1:] == 'Jython'
    assert word[:2] + 'py' == 'Pypy'

    # 内置函数 len() 返回字符串的长度：
    characters = 'supercalifragilisticexpialidocious'
    assert len(characters) == 34

    # 字符串字面量可以跨越多行。一种方式是使用三引号："""..."""
    # 或 '''...'''。行尾会自动包含在字符串中，但可以通过在行尾
    # 添加 \ 来防止这种情况。以下示例：
    multi_line_string = '''\
        First line
        Second line
    '''

    assert multi_line_string == '''\
        First line
        Second line
    '''


def test_string_operators():
    """基本操作

    字符串可以用 + 运算符连接（粘合在一起），
    用 * 重复：3 次 'un'，后跟 'ium'
    """

    assert 3 * 'un' + 'ium' == 'unununium'

    # 'Py' 'thon'
    python = 'Py' 'thon'
    assert python == 'Python'

    # 当你想要拆分长字符串时，这个特性特别有用：
    text = (
        'Put several strings within parentheses '
        'to have them joined together.'
    )
    assert text == 'Put several strings within parentheses to have them joined together.'

    # 如果你想连接变量或变量和字面量，使用 +：
    prefix = 'Py'
    assert prefix + 'thon' == 'Python'


def test_string_methods():
    """字符串方法"""

    hello_world_string = "Hello, World!"

    # strip() 方法删除开头或结尾的任何空白字符。
    string_with_whitespaces = " Hello, World! "
    assert string_with_whitespaces.strip() == "Hello, World!"

    # len() 方法返回字符串的长度。
    assert len(hello_world_string) == 13

    # lower() 方法返回小写字符串。
    assert hello_world_string.lower() == 'hello, world!'

    # upper() 方法返回大写字符串。
    assert hello_world_string.upper() == 'HELLO, WORLD!'

    # replace() 方法用另一个字符串替换一个字符串。
    assert hello_world_string.replace('H', 'J') == 'Jello, World!'

    # split() 方法在找到分隔符实例时将字符串拆分为子字符串。
    assert hello_world_string.split(',') == ['Hello', ' World!']

    # 将第一个字符转换为大写
    assert 'low letter at the beginning'.capitalize() == 'Low letter at the beginning'

    # 返回指定值在字符串中出现的次数。
    assert 'low letter at the beginning'.count('t') == 4

    # 在字符串中搜索指定值并返回找到它的位置。
    assert 'Hello, welcome to my world'.find('welcome') == 7

    # 将每个单词的第一个字符转换为大写
    assert 'Welcome to my world'.title() == 'Welcome To My World'

    # 返回一个字符串，其中指定值被替换为指定值。
    assert 'I like bananas'.replace('bananas', 'apples') == 'I like apples'

    # 将可迭代对象的元素连接到字符串末尾。
    my_tuple = ('John', 'Peter', 'Vicky')
    assert ', '.join(my_tuple) == 'John, Peter, Vicky'

    # 如果字符串中的所有字符都是大写，则返回 True。
    assert 'ABC'.isupper()
    assert not 'AbC'.isupper()

    # 检查文本中的所有字符是否都是字母。
    assert 'CompanyX'.isalpha()
    assert not 'Company 23'.isalpha()

    # 如果字符串中的所有字符都是十进制数字，则返回 True。
    assert '1234'.isdecimal()
    assert not 'a21453'.isdecimal()


def test_string_formatting():
    """字符串格式化

    通常你会希望对输出格式有更多控制，而不仅仅是打印空格分隔的值。
    有几种格式化输出的方法。
    """

    # 要使用格式化字符串字面量，在开头引号或三引号之前以 f 或 F 开始字符串。
    # 在这个字符串内，你可以在 { 和 } 字符之间编写 Python 表达式，
    # 可以引用变量或字面量值。
    year = 2018
    event = 'conference'

    assert f'Results of the {year} {event}' == 'Results of the 2018 conference'

    # str.format() 方法需要更多手动操作。你仍然使用 { 和 } 来标记
    # 变量将被替换的位置，并可以提供详细的格式化指令，
    # 但你还需要提供要格式化的信息。
    yes_votes = 42_572_654  # 等同于 42572654
    no_votes = 43_132_495   # 等同于 43132495
    percentage = yes_votes / (yes_votes + no_votes)

    assert '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage) == ' 42572654 YES votes  49.67%'

    # 当你不需要花哨的输出，只是想快速显示一些变量进行调试时，
    # 你可以使用 repr() 或 str() 函数将任何值转换为字符串。
    # str() 函数用于返回相当易于人类阅读的值表示，
    # 而 repr() 用于生成可以被解释器读取的表示
    # （如果没有等效语法，则会强制产生 SyntaxError）。
    # 对于没有特定人类可读表示的对象，str() 将返回与 repr() 相同的值。
    # 许多值，如数字或列表和字典等结构，使用任一函数都有相同的表示。
    # 字符串特别有两种不同的表示。

    greeting = 'Hello, world.'
    first_num = 10 * 3.25
    second_num = 200 * 200

    assert str(greeting) == 'Hello, world.'
    assert repr(greeting) == "'Hello, world.'"
    assert str(1/7) == '0.14285714285714285'

    # repr() 的参数可以是任何 Python 对象：
    assert repr((first_num, second_num, ('spam', 'eggs'))) == "(32.5, 40000, ('spam', 'eggs'))"

    # 格式化字符串字面量

    # 格式化字符串字面量（简称 f-strings）允许你通过在字符串前加上 f 或 F
    # 并将表达式写成 {expression} 来在字符串中包含 Python 表达式的值。

    # 可选的格式说明符可以跟在表达式后面。这允许更好地控制值的格式化方式。
    # 以下示例将 pi 四舍五入到小数点后三位。
    pi_value = 3.14159
    assert f'The value of pi is {pi_value:.3f}.' == 'The value of pi is 3.142.'

    # 在 ':' 后传递一个整数将使该字段成为最小字符宽度。
    # 这对于使列对齐很有用：
    table_data = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    table_string = ''
    for name, phone in table_data.items():
        table_string += f'{name:7}==>{phone:7d}'

    assert table_string == ('Sjoerd ==>   4127'
                            'Jack   ==>   4098'
                            'Dcab   ==>   7678')

    # 字符串 format() 方法

    # str.format() 方法的基本用法如下：
    assert 'We are {} who say "{}!"'.format('knights', 'Ni') == 'We are knights who say "Ni!"'

    # 括号及其中的字符（称为格式字段）被替换为传递给 str.format() 方法的对象。
    # 括号中的数字可用于引用传递给 str.format() 方法的对象的位置
    assert '{0} and {1}'.format('spam', 'eggs') == 'spam and eggs'
    assert '{1} and {0}'.format('spam', 'eggs') == 'eggs and spam'

    # 如果在 str.format() 方法中使用关键字参数，则通过使用参数名称来引用它们的值。
    formatted_string = 'This {food} is {adjective}.'.format(
        food='spam',
        adjective='absolutely horrible'
    )

    assert formatted_string == 'This spam is absolutely horrible.'

    # 位置参数和关键字参数可以任意组合
    formatted_string = 'The story of {0}, {1}, and {other}.'.format(
        'Bill',
        'Manfred',
        other='Georg'
    )

    assert formatted_string == 'The story of Bill, Manfred, and Georg.'

    # 如果你有一个很长的格式字符串不想拆分，最好能够通过名称而不是位置
    # 引用要格式化的变量。这可以通过简单地传递字典并使用方括号 '[]'
    # 访问键来完成

    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    formatted_string = 'Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table)

    assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'

    # 这也可以通过使用 '**' 符号将表作为关键字参数传递来完成。
    formatted_string = 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)

    assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'
