"""模块

@see: https://docs.python.org/3/tutorial/modules.html

随着程序变长，你可能想把它分成几个文件以便于维护。
你可能还想在多个程序中使用你编写的一个方便的函数，
而不必将其定义复制到每个程序中。

为了支持这一点，Python 有一种方法可以将定义放在文件中，
并在脚本或解释器的交互式实例中使用它们。这样的文件称为模块；
模块中的定义可以导入到其他模块或主模块中
（你在顶层执行的脚本和计算器模式中可以访问的变量集合）。

模块是包含 Python 定义和语句的文件。文件名是模块名加上后缀 .py。
在模块内，模块名（作为字符串）可作为全局变量 __name__ 的值使用。

当解释器执行 import 语句时，它在从以下来源组装的目录列表中搜索模块：

- 运行输入脚本的目录，或者如果解释器以交互方式运行则为当前目录
- PYTHONPATH 环境变量中包含的目录列表（如果已设置）。
（PYTHONPATH 的格式取决于操作系统，但应该模仿 PATH 环境变量。）
- 安装 Python 时配置的依赖于安装的目录列表

生成的搜索路径可在 Python 变量 sys.path 中访问，该变量从名为 sys 的模块获得：

>>> import sys
>>> sys.path

@see: https://realpython.com/python-modules-packages/
"""

# 这不会将 fibonacci_module 中定义的函数名直接输入到当前符号表中；
# 它只在那里输入模块名 fibonacci_module。
import fibonacci_module

# import 语句有一个变体，可以将模块中的名称直接导入到导入模块的符号表中。例如：

# pylint: disable=reimported
from fibonacci_module import fibonacci_at_position, fibonacci_smaller_than

# 甚至有一个变体可以导入模块定义的所有名称。这会导入所有名称，
# 除了以下划线 (_) 开头的名称。在大多数情况下，Python 程序员不使用此功能，
# 因为它会将一组未知的名称引入解释器，可能会隐藏你已经定义的一些内容。
# >>> from fibonacci_module import *

# 如果模块名后面跟着 as，则 as 后面的名称直接绑定到导入的模块：
import fibonacci_module as fibonacci_module_renamed

# 它也可以在使用 from 时使用，效果类似：
from fibonacci_module import fibonacci_at_position as fibonacci_at_position_renamed

# 当导入名为 spam 的模块时，解释器首先搜索具有该名称的内置模块。
# 如果找不到，它会在变量 sys.path 给出的目录列表中搜索名为 spam.py 的文件。
# sys.path 从以下位置初始化：
#
# - 包含输入脚本的目录（或未指定文件时的当前目录）。
# - PYTHONPATH（目录名列表，语法与 shell 变量 PATH 相同）。
# - 依赖于安装的默认值。


def test_modules():
    """模块"""

    assert fibonacci_module.fibonacci_at_position(7) == 13
    assert fibonacci_at_position(7) == 13
    assert fibonacci_module_renamed.fibonacci_at_position(7) == 13
    assert fibonacci_at_position_renamed(7) == 13

    assert fibonacci_module.fibonacci_smaller_than(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert fibonacci_smaller_than(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert fibonacci_module_renamed.fibonacci_smaller_than(10) == [0, 1, 1, 2, 3, 5, 8]

    # 如果你打算经常使用一个函数，你可以将它赋给一个局部名称。
    fibonacci = fibonacci_module.fibonacci_smaller_than
    assert fibonacci(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    # 内置函数 dir() 用于找出模块定义了哪些名称。它返回一个排序的字符串列表。
    assert dir(fibonacci_module) == [
        '__builtins__',
        '__cached__',
        '__doc__',
        '__file__',
        '__loader__',
        '__name__',
        '__package__',
        '__spec__',
        'fibonacci_at_position',
        'fibonacci_smaller_than',
    ]
