"""斐波那契数列模块

@see: https://docs.python.org/3/tutorial/modules.html

模块是包含 Python 定义和语句的文件。文件名是模块名加上后缀 .py。
在模块内，模块名（作为字符串）可作为全局变量 __name__ 的值使用。
"""


def fibonacci_at_position(position):
    """返回指定位置的斐波那契数"""
    current_position = 0
    previous_number, current_number = 0, 1
    while current_position < position:
        current_position += 1
        previous_number, current_number = current_number, previous_number + current_number
    return previous_number


def fibonacci_smaller_than(limit):
    """返回不超过 limit 的斐波那契数列"""
    result = []
    previous_number, current_number = 0, 1
    while previous_number < limit:
        result.append(previous_number)
        previous_number, current_number = current_number, previous_number + current_number
    return result


# 当你用以下方式运行 Python 模块时：
#
# >>> python fibonacci.py <arguments>
#
# 模块中的代码将被执行，就像你导入它一样，但 __name__ 设置为 "__main__"。
# 这意味着通过在模块末尾添加此代码，你可以使文件既可用作脚本，
# 也可用作可导入模块，因为解析命令行的代码只有在模块作为"主"文件执行时才运行：
#
# >>> python fibonacci.py 50
if __name__ == '__main__':
    import sys
    print(fibonacci_smaller_than(int(sys.argv[1])))
