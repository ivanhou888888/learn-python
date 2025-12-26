"""读写文件

@see: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

读写文件的过程就像找到一本书并打开它。
首先，定位文件，打开到第一页，然后开始读/写直到到达文件末尾。
"""


def test_files_open():
    """打开文件

    open() 返回一个文件对象，最常用的是两个参数：
    open(filename, mode)。

    第一个参数是包含文件名的字符串。第二个参数是另一个字符串，
    包含几个描述文件使用方式的字符。mode 可以是：

    - 'r' 当文件只被读取时，
    - 'w' 仅用于写入（同名的现有文件将被擦除），
    - 'a' 打开文件进行追加；写入文件的任何数据都会自动添加到末尾。
    - 'r+' 打开文件进行读写。

    mode 参数是可选的；如果省略，将假定为 'r'。

    通常，文件以文本模式打开，这意味着你从文件读取和写入字符串，
    这些字符串以特定编码进行编码。如果未指定编码，则默认值取决于平台（参见 open()）。
    在模式后附加 'b' 以二进制模式打开文件：现在数据以字节对象的形式读取和写入。
    此模式应用于所有不包含文本的文件。

    在文本模式下，读取时的默认行为是将特定于平台的行尾
    （Unix 上的 \\n，Windows 上的 \\r\\n）转换为 \\n。
    在文本模式下写入时，默认行为是将 \\n 转换回特定于平台的行尾。
    这种对文件数据的幕后修改对于文本文件来说是可以的，
    但会损坏 JPEG 或 EXE 文件等二进制数据。在读写此类文件时要非常小心使用二进制模式。

    在处理文件对象时使用 with 关键字是一个好习惯。优点是文件在其套件完成后
    会正确关闭，即使在某个时刻引发了异常。使用 with 也比编写等效的 try-finally 块短得多：
    """

    # 不使用 'with' 语句打开文件。
    file = open('src/files/multi_line_file.txt', 'r')

    assert not file.closed

    read_data = file.read()

    assert read_data == (
        'first line\n'
        'second line\n'
        'third line'
    )

    file.close()

    assert file.closed

    # 使用 with 打开文件。
    with open('src/files/multi_line_file.txt', 'r') as file:
        read_data = file.read()

        assert read_data == (
            'first line\n'
            'second line\n'
            'third line'
        )

    assert file.closed

    # 如果你不使用 with 关键字，那么你应该调用 f.close() 来关闭文件，
    # 并立即释放它使用的任何系统资源。如果你没有显式关闭文件，
    # Python 的垃圾收集器最终会销毁对象并为你关闭打开的文件，
    # 但文件可能会保持打开一段时间。另一个风险是不同的 Python 实现
    # 会在不同的时间进行这种清理。
