"""集合

@see: https://www.w3schools.com/python/python_sets.asp
@see: https://docs.python.org/3.7/tutorial/datastructures.html#sets

集合是一个无序且无索引的集合。
在 Python 中，集合用花括号编写。

集合对象还支持数学运算，如并集、交集、差集和对称差集。
"""


def test_sets():
    """集合"""
    fruits_set = {"apple", "banana", "cherry"}

    assert isinstance(fruits_set, set)

    # 也可以使用 set() 构造函数来创建集合。
    # 注意双圆括号
    fruits_set_via_constructor = set(("apple", "banana", "cherry"))

    assert isinstance(fruits_set_via_constructor, set)


def test_set_methods():
    """集合方法"""

    fruits_set = {"apple", "banana", "cherry"}

    # 你可以使用 "in" 语句检查项是否在集合中
    assert "apple" in fruits_set
    assert "pineapple" not in fruits_set

    # 使用 len() 方法返回项的数量。
    assert len(fruits_set) == 3

    # 你可以使用 add() 对象方法添加一个项。
    fruits_set.add("pineapple")
    assert "pineapple" in fruits_set
    assert len(fruits_set) == 4

    # 使用 remove() 方法删除一个项。
    fruits_set.remove("pineapple")
    assert "pineapple" not in fruits_set
    assert len(fruits_set) == 3

    # 演示两个单词中唯一字母的集合操作：
    first_char_set = set('abracadabra')
    second_char_set = set('alacazam')

    assert first_char_set == {'a', 'r', 'b', 'c', 'd'}  # 第一个单词中的唯一字母
    assert second_char_set == {'a', 'l', 'c', 'z', 'm'}  # 第二个单词中的唯一字母

    # 在第一个单词中但不在第二个单词中的字母。
    assert first_char_set - second_char_set == {'r', 'b', 'd'}

    # 在第一个单词或第二个单词或两者中的字母。
    assert first_char_set | second_char_set == {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

    # 两个单词中共同的字母。
    assert first_char_set & second_char_set == {'a', 'c'}

    # 在第一个或第二个单词中但不同时在两者中的字母。
    assert first_char_set ^ second_char_set == {'r', 'd', 'b', 'm', 'z', 'l'}

    # 与列表推导式类似，也支持集合推导式：
    word = {char for char in 'abracadabra' if char not in 'abc'}
    assert word == {'r', 'd'}
