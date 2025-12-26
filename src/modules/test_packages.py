"""包

@see: https://docs.python.org/3/tutorial/modules.html#packages

包是一种使用"点分模块名"来构造 Python 模块命名空间的方式。
例如，模块名 A.B 表示名为 A 的包中名为 B 的子模块。
就像使用模块可以使不同模块的作者不必担心彼此的全局变量名一样，
使用点分模块名可以使像 NumPy 或 Pillow 这样的多模块包的作者
不必担心彼此的模块名。

__init__.py 文件是必需的，以使 Python 将目录视为包含包；
这样做是为了防止具有常见名称（如 string）的目录无意中隐藏
稍后出现在模块搜索路径上的有效模块。在最简单的情况下，
__init__.py 可以只是一个空文件，但它也可以执行包的初始化代码
或设置 __all__ 变量，稍后描述。

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

# 包的用户可以从包中导入单个模块，例如。
import sound_package.effects.echo

# 导入子模块的另一种方式是：

# pylint: disable=reimported
from sound_package.effects import echo

# 另一种变体是直接导入所需的函数或变量：
from sound_package.effects.echo import echo_function

# 注意，当使用 from package import item 时，item 可以是包的子模块（或子包），
# 或者是包中定义的其他名称，如函数、类或变量。
# import 语句首先测试 item 是否在包中定义；如果没有，它假设它是一个模块并尝试加载它。
# 如果找不到，则引发 ImportError 异常。

# 相反，当使用 import item.subitem.subsubitem 这样的语法时，
# 除了最后一个之外的每个 item 都必须是一个包；
# 最后一个 item 可以是模块或包，但不能是前一个 item 中定义的类、函数或变量。


def test_packages():
    """包。"""
    assert sound_package.effects.echo.echo_function() == 'Do echo effect'
    assert echo.echo_function() == 'Do echo effect'
    assert echo_function() == 'Do echo effect'
