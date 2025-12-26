"""CONTINUE 语句

@see: https://docs.python.org/3/tutorial/controlflow.html

continue 语句借鉴自 C，继续循环的下一次迭代。
"""


def test_continue_statement():
    """FOR 循环中的 CONTINUE 语句"""

    # 这个列表将只包含范围内的偶数。
    even_numbers = []
    # 这个列表将包含其他所有数字（在这种情况下是奇数）。
    rest_of_the_numbers = []

    for number in range(0, 10):
        # 检查除法后的余数是否为零（这意味着数字是偶数）。
        if number % 2 == 0:
            even_numbers.append(number)
            # 停止当前循环迭代并立即进入下一次迭代。
            continue

        rest_of_the_numbers.append(number)

    assert even_numbers == [0, 2, 4, 6, 8]
    assert rest_of_the_numbers == [1, 3, 5, 7, 9]
