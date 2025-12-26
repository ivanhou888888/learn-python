"""序列化

@see: https://www.learnpython.org/en/Serialization

Python 提供内置的 JSON 库来编码和解码 JSON。
"""

import json


def test_json():
    """JSON 序列化。"""

    # JSON 数据有两种基本格式。字符串格式或对象数据结构。
    # 在 Python 中，对象数据结构由相互嵌套的列表和字典组成。
    # 对象数据结构允许使用 python 方法（用于列表和字典）
    # 从数据结构中添加、列出、搜索和删除元素。
    # 字符串格式主要用于将数据传递给另一个程序或加载到数据结构中。

    person_dictionary = {'first_name': 'John', 'last_name': 'Smith', 'age': 42}
    assert person_dictionary['first_name'] == 'John'
    assert person_dictionary['age'] == 42

    json_string = '{"first_name": "John", "last_name": "Smith", "age": 42}'

    # 要将 JSON 加载回数据结构，使用 "loads" 方法。
    # 此方法接受一个字符串并将其转换回 json 对象数据结构：
    person_parsed_dictionary = json.loads(json_string)

    assert person_parsed_dictionary == person_dictionary
    assert person_parsed_dictionary['first_name'] == 'John'
    assert person_parsed_dictionary['age'] == 42

    # 要将数据结构编码为 JSON，使用 "dumps" 方法。
    # 此方法接受一个对象并返回一个字符串：
    encoded_person_string = json.dumps(person_dictionary)

    assert encoded_person_string == json_string
