"""字典

@see: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
@see: https://www.w3schools.com/python/python_dictionaries.asp

字典是一个无序、可更改且有索引的集合。在 Python 中，字典用花括号编写，
它们有键和值。

字典有时在其他语言中被称为"关联内存"或"关联数组"。
与按数字范围索引的序列不同，字典是按键索引的，
键可以是任何不可变类型；字符串和数字总是可以作为键。
如果元组只包含字符串、数字或元组，则可以用作键；
如果元组直接或间接包含任何可变对象，则不能用作键。
你不能使用列表作为键，因为列表可以使用索引赋值、切片赋值
或 append() 和 extend() 等方法进行原地修改。

最好将字典视为一组键值对，要求键是唯一的（在一个字典内）。
一对花括号创建一个空字典：{}。
在花括号内放置逗号分隔的键值对列表会向字典添加初始键值对；
这也是字典在输出时的写法。
"""


def test_dictionary():
    """字典"""

    fruits_dictionary = {
        'cherry': 'red',
        'apple': 'green',
        'banana': 'yellow',
    }

    assert isinstance(fruits_dictionary, dict)

    # 你可以通过键访问集合元素。
    assert fruits_dictionary['apple'] == 'green'
    assert fruits_dictionary['banana'] == 'yellow'
    assert fruits_dictionary['cherry'] == 'red'

    # 要检查单个键是否在字典中，使用 in 关键字。
    assert 'apple' in fruits_dictionary
    assert 'pineapple' not in fruits_dictionary

    # 将苹果颜色更改为 "red"。
    fruits_dictionary['apple'] = 'red'

    # 向字典添加新的键值对
    fruits_dictionary['pineapple'] = 'yellow'
    assert fruits_dictionary['pineapple'] == 'yellow'

    # 对字典执行 list(d) 返回字典中使用的所有键的列表，
    # 按插入顺序排列（如果你想要排序，只需使用 sorted(d)）。
    assert list(fruits_dictionary) == ['cherry', 'apple', 'banana', 'pineapple']
    assert sorted(fruits_dictionary) == ['apple', 'banana', 'cherry', 'pineapple']

    # 也可以使用 del 删除键值对。
    del fruits_dictionary['pineapple']
    assert list(fruits_dictionary) == ['cherry', 'apple', 'banana']

    # dict() 构造函数直接从键值对序列构建字典。
    dictionary_via_constructor = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

    assert dictionary_via_constructor['sape'] == 4139
    assert dictionary_via_constructor['guido'] == 4127
    assert dictionary_via_constructor['jack'] == 4098

    # 此外，字典推导式可用于从任意键和值表达式创建字典：
    dictionary_via_expression = {x: x**2 for x in (2, 4, 6)}
    assert dictionary_via_expression[2] == 4
    assert dictionary_via_expression[4] == 16
    assert dictionary_via_expression[6] == 36

    # 当键是简单字符串时，有时使用关键字参数指定对更容易。
    dictionary_for_string_keys = dict(sape=4139, guido=4127, jack=4098)
    assert dictionary_for_string_keys['sape'] == 4139
    assert dictionary_for_string_keys['guido'] == 4127
    assert dictionary_for_string_keys['jack'] == 4098
