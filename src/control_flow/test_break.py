"""BREAK 语句

@see: https://docs.python.org/3/tutorial/controlflow.html

break 语句，像在 C 中一样，跳出最内层的 "for" 或 "while" 循环。
"""


def test_break_statement():
    """BREAK 语句"""

    # 让我们在 0 到 100 的范围内找到我们需要的数字时终止循环。
    number_to_be_found = 42
    # 这个变量将记录我们进入 "for" 循环的次数。
    number_of_iterations = 0

    for number in range(100):
        if number == number_to_be_found:
            # 在这里中断，不继续循环。
            break
        else:
            number_of_iterations += 1

    # 我们需要确保 break 语句在找到数字后终止了循环。
    assert number_of_iterations == 42
