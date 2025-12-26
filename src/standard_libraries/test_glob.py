"""文件通配符

@see: https://docs.python.org/3/tutorial/stdlib.html#file-wildcards

glob 模块提供了一个函数，用于从目录通配符搜索中创建文件列表：
"""

import glob


def test_glob():
    """文件通配符。"""

    # 列表的 == 运算符依赖于列表中元素的顺序。
    # 在某些情况下（如在 Linux Mint、python3.6 上），glob() 函数返回的列表
    # 顺序可能与预期相反。因此，让我们在比较之前使用内置的 sorted() 函数
    # 对两个列表进行排序。
    assert sorted(glob.glob('src/standard_libraries/glob_files/*.txt')) == sorted([
        'src/standard_libraries/glob_files/first_file.txt',
        'src/standard_libraries/glob_files/second_file.txt'
    ])
