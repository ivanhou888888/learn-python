"""函数定义

@see: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
@see: https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

关键字 def 引入函数定义。它后面必须跟着函数名和带括号的形式参数列表。
构成函数体的语句从下一行开始，必须缩进。
"""


def fibonacci_function_example(number_limit):
    """生成一个不超过 number_limit 的斐波那契数列。

    函数体的第一条语句可以是一个字符串字面量；这个字符串字面量是函数的
    文档字符串，或 docstring。有些工具使用文档字符串自动生成在线或打印文档，
    或让用户交互式地浏览代码；在你编写的代码中包含文档字符串是一个好习惯，
    所以养成这个习惯吧。
    """

    # 函数的执行引入了一个新的符号表，用于函数的局部变量。
    # 更准确地说，函数中的所有变量赋值都将值存储在局部符号表中；
    # 而变量引用首先在局部符号表中查找，然后在封闭函数的局部符号表中查找，
    # 然后在全局符号表中查找，最后在内置名称表中查找。
    # 因此，全局变量不能在函数内直接赋值（除非在 global 语句中命名），
    # 尽管它们可以被引用。
    fibonacci_list = []
    previous_number, current_number = 0, 1
    while previous_number < number_limit:
        # 语句 result.append(a) 调用列表对象 result 的一个方法。
        # 方法是"属于"对象的函数，命名为 obj.methodname，其中 obj 是某个对象
        # （这可能是一个表达式），methodname 是由对象类型定义的方法名称。
        # 不同的类型定义不同的方法。不同类型的方法可以有相同的名称而不会引起歧义。
        # （可以使用类定义自己的对象类型和方法，参见类）
        # 示例中显示的 append() 方法是为列表对象定义的；它在列表末尾添加一个新元素。
        # 在这个例子中，它等同于 result = result + [a]，但更高效。
        fibonacci_list.append(previous_number)
        # 这是多重赋值语句。我们让当前数字成为前一个数字，
        # 前一个和当前数字的和成为新的当前数字。
        previous_number, current_number = current_number, previous_number + current_number

    # return 语句从函数返回一个值。没有表达式参数的 return 返回 None。
    # 从函数末尾掉落也返回 None。
    return fibonacci_list


def test_function_definition():
    """函数定义"""

    # 现在调用我们刚刚定义的函数。
    assert fibonacci_function_example(300) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

    # 函数定义在当前符号表中引入函数名。函数名的值具有解释器识别为
    # 用户定义函数的类型。这个值可以赋给另一个名称，然后也可以用作函数。
    # 这作为一种通用的重命名机制
    fibonacci_function_clone = fibonacci_function_example
    assert fibonacci_function_clone(300) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

    # 在 Python 中，函数是一等公民，它们是对象，这意味着我们可以用它们
    # 做很多有用的事情。

    # 将函数赋给变量。

    def greet(name):
        return 'Hello, ' + name

    greet_someone = greet

    assert greet_someone('John') == 'Hello, John'

    # 在其他函数内部定义函数。

    def greet_again(name):
        def get_message():
            return 'Hello, '

        result = get_message() + name
        return result

    assert greet_again('John') == 'Hello, John'

    # 函数可以作为参数传递给其他函数。

    def greet_one_more(name):
        return 'Hello, ' + name

    def call_func(func):
        other_name = 'John'
        return func(other_name)

    assert call_func(greet_one_more) == 'Hello, John'

    # 函数可以返回其他函数。换句话说，函数生成其他函数。

    def compose_greet_func():
        def get_message():
            return 'Hello there!'

        return get_message

    greet_function = compose_greet_func()
    assert greet_function() == 'Hello there!'

    # 内部函数可以访问封闭作用域。

    # 更常见的称为闭包。这是一个非常强大的模式，我们在构建装饰器时会遇到。
    # 另一件需要注意的事情是，Python 只允许对外部作用域进行读访问，而不是赋值。
    # 注意我们如何修改上面的示例，从内部函数的封闭作用域读取 "name" 参数
    # 并返回新函数。

    def compose_greet_func_with_closure(name):
        def get_message():
            return 'Hello there, ' + name + '!'

        return get_message

    greet_with_closure = compose_greet_func_with_closure('John')

    assert greet_with_closure() == 'Hello there, John!'
