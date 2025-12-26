"""TRY 语句

@see: https://www.w3schools.com/python/python_try_except.asp

"try" 语句用于异常处理。
当发生错误或我们所说的异常时，Python 通常会停止并生成错误消息。
这些异常可以使用 try 语句来处理。

"try" 块让你测试一段代码是否有错误。
"except" 块让你处理错误。
"else" 块让你在没有引发错误时执行代码。
"finally" 块让你执行代码，无论 try 和 except 块的结果如何。
"""


def test_try():
    """TRY 语句"""

    # try 块将生成一个错误，因为 x 未定义：
    exception_has_been_caught = False

    try:
        # pylint: disable=undefined-variable
        print(not_existing_variable)
    except NameError:
        exception_has_been_caught = True

    assert exception_has_been_caught

    # 你可以定义任意多个 except 块，例如，如果你想为特定类型的错误
    # 执行特殊的代码块：
    exception_message = ''

    try:
        # pylint: disable=undefined-variable
        print(not_existing_variable)
    except NameError:
        exception_message = 'Variable is not defined'

    assert exception_message == 'Variable is not defined'

    # 你可以使用 else 关键字定义一个代码块，
    # 在没有引发错误时执行。
    message = ''
    # pylint: disable=broad-except
    try:
        message += 'Success.'
    except NameError:
        message += 'Something went wrong.'
    else:
        message += 'Nothing went wrong.'

    assert message == 'Success.Nothing went wrong.'

    # finally 块，如果指定，将无论 try 块是否引发错误都会执行。
    message = ''
    try:
        # pylint: undefined-variable
        print(not_existing_variable)  # noqa: F821
    except NameError:
        message += 'Something went wrong.'
    finally:
        message += 'The "try except" is finished.'

    assert message == 'Something went wrong.The "try except" is finished.'
