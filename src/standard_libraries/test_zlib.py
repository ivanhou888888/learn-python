"""数据压缩

@see: https://docs.python.org/3/tutorial/stdlib.html#data-compression

常见的数据归档和压缩格式由以下模块直接支持：zlib、gzip、bz2、lzma、zipfile 和 tarfile。
"""

import zlib


def test_zlib():
    """zlib。"""
    string = b'witch which has which witches wrist watch'
    assert len(string) == 41

    zlib_compressed_string = zlib.compress(string)
    assert len(zlib_compressed_string) == 37

    zlib_decompressed_string = zlib.decompress(zlib_compressed_string)
    assert zlib_decompressed_string == b'witch which has which witches wrist watch'

    assert zlib.crc32(string) == 226805979
