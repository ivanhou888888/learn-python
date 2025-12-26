"""身份运算符

@see: https://www.w3schools.com/python/python_operators.asp

身份运算符用于比较对象，不是比较它们是否相等，
而是比较它们是否实际上是同一个对象，具有相同的内存位置。
"""


def test_identity_operators():
    """身份运算符"""

    # 让我们基于以下列表来说明身份运算符。
    first_fruits_list = ["apple", "banana"]
    second_fruits_list = ["apple", "banana"]
    third_fruits_list = first_fruits_list

    # is
    # 如果两个变量是同一个对象，则返回 true。

    # 示例：
    # first_fruits_list 和 third_fruits_list 是同一个对象。
    assert first_fruits_list is third_fruits_list

    # is not
    # 如果两个变量不是同一个对象，则返回 true。

    # 示例：
    # first_fruits_list 和 second_fruits_list 不是同一个对象，
    # 即使它们有相同的内容
    assert first_fruits_list is not second_fruits_list

    # 为了演示 "is" 和 "==" 之间的区别：这个比较返回 True，
    # 因为 first_fruits_list 等于 second_fruits_list。
    assert first_fruits_list == second_fruits_list
