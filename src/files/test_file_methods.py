"""文件对象方法

@see: https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects

从文件读取并不总是必须是顺序的。有一些方法可以查找文件中的特定位置，
就像翻到书中的某一页一样。
"""


def test_file_methods():
    """文件对象方法"""

    multi_line_file = open('src/files/multi_line_file.txt', 'r')
    binary_file = open('src/files/binary_file', 'r')

    # 要读取文件的内容，调用 f.read(size)，它读取一定数量的数据并将其作为
    # 字符串（在文本模式下）或字节对象（在二进制模式下）返回。
    # size 是一个可选的数字参数。当 size 被省略或为负数时，
    # 将读取并返回文件的全部内容；如果文件是你机器内存的两倍大，那是你的问题。
    # 否则，最多读取并返回 size 字节。如果已到达文件末尾，f.read() 将返回空字符串 ('')。
    read_data = multi_line_file.read()

    # pylint: disable=duplicate-code
    assert read_data == 'first line\nsecond line\nthird line'

    # 要更改文件对象的位置，使用 f.seek(offset, from_what)。
    # 位置是通过将 offset 添加到参考点来计算的；参考点由 from_what 参数选择。
    # from_what 值为 0 从文件开头测量，1 使用当前文件位置，2 使用文件末尾作为参考点。
    # from_what 可以省略，默认为 0，使用文件开头作为参考点。
    assert binary_file.seek(0) == 0  # 转到文件中的第 0 个字节
    assert binary_file.seek(6) == 6  # 转到文件中的第 6 个字节

    assert binary_file.read(1) == '6'

    # f.readline() 从文件读取一行；换行符 (\\n) 留在字符串的末尾，
    # 只有在文件的最后一行如果文件不以换行符结尾时才省略。
    # 这使得返回值是明确的；如果 f.readline() 返回空字符串，
    # 则已到达文件末尾，而空行由 '\\n' 表示，即只包含一个换行符的字符串。
    multi_line_file.seek(0)

    assert multi_line_file.readline() == 'first line\n'
    assert multi_line_file.readline() == 'second line\n'
    assert multi_line_file.readline() == 'third line'
    assert multi_line_file.readline() == ''

    multi_line_file.close()
    binary_file.close()
