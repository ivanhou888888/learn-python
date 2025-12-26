"""作用域和命名空间

@see: https://docs.python.org/3/tutorial/classes.html#scopes-and-namespaces-example

命名空间是从名称到对象的映射。大多数命名空间目前实现为 Python 字典，
但这通常不会以任何方式被注意到（除了性能），将来可能会改变。
命名空间的例子有：内置名称集合（包含 abs() 等函数和内置异常名称）；
模块中的全局名称；函数调用中的局部名称。
从某种意义上说，对象的属性集合也形成一个命名空间。
关于命名空间需要知道的重要事情是，不同命名空间中的名称之间绝对没有关系；
例如，两个不同的模块可能都定义一个 maximize 函数而不会混淆——
模块的用户必须在它前面加上模块名。

顺便说一下，我们对点后面的任何名称使用"属性"这个词——例如，在表达式 z.real 中，
real 是对象 z 的一个属性。严格来说，模块中名称的引用是属性引用：
在表达式 modname.func_name 中，modname 是一个模块对象，func_name 是它的一个属性。
在这种情况下，模块的属性和模块中定义的全局名称之间恰好有一个直接的映射：
它们共享同一个命名空间！

作用域是 Python 程序的一个文本区域，在这里命名空间可以直接访问。
这里的"直接访问"意味着对名称的非限定引用尝试在命名空间中查找该名称。

虽然作用域是静态确定的，但它们是动态使用的。在执行期间的任何时候，
至少有三个嵌套作用域，其命名空间可以直接访问：
- 最内层作用域，首先被搜索，包含局部名称。
- 任何封闭函数的作用域，从最近的封闭作用域开始搜索，包含非局部但也非全局的名称。
- 倒数第二个作用域包含当前模块的全局名称。
- 最外层作用域（最后搜索）是包含内置名称的命名空间。

注意！！！
-------------
从内部函数更改全局或非局部变量可能是一个不好的做法，
可能导致更难调试和更脆弱的代码！只有在你知道自己在做什么时才这样做。
"""

# pylint: disable=invalid-name
test_variable = 'initial global value'


def test_function_scopes():
    """作用域和命名空间示例"""

    # 这是一个演示如何引用不同作用域和命名空间的示例，
    # 以及 global 和 nonlocal 如何影响变量绑定：

    # pylint: disable=redefined-outer-name
    test_variable = 'initial value inside test function'

    def do_local():
        # 创建只能在当前 do_local() 函数内部访问的变量。
        # pylint: disable=redefined-outer-name
        test_variable = 'local value'
        return test_variable

    def do_nonlocal():
        # 访问外部作用域的变量并尝试更改它。
        # pylint: disable=redefined-outer-name
        nonlocal test_variable
        test_variable = 'nonlocal value'
        return test_variable

    def do_global():
        # 访问最全局作用域的变量并尝试更改它。
        # pylint: disable=redefined-outer-name,global-statement
        global test_variable
        test_variable = 'global value'
        return test_variable

    # 在这个级别，我们目前可以访问 test_function_scopes() 函数的局部变量。
    assert test_variable == 'initial value inside test function'

    # 执行局部赋值。
    # 它不会更改全局变量和 test_function_scopes() 作用域的变量。
    do_local()
    assert test_variable == 'initial value inside test function'

    # 执行非局部赋值。
    # 它不会更改全局变量，但会更改 test_function_scopes() 函数作用域的变量。
    do_nonlocal()
    assert test_variable == 'nonlocal value'

    # 执行全局赋值。
    # 这个会更改全局变量，但不会更改 test_function_scopes() 函数作用域的变量。
    do_global()
    assert test_variable == 'nonlocal value'


def test_global_variable_access():
    """测试从函数内部访问全局变量"""

    # test_variable 的全局值已经被前一个测试中的 do_global() 函数更改了，
    # 所以让我们检查一下。
    # pylint: disable=global-statement
    global test_variable
    assert test_variable == 'global value'

    # 在这个例子中，你可以看到从内部函数访问和更改全局变量
    # 可能会使调试更加困难，代码更不可预测。因为你可能期望
    # test_variable 仍然等于 'initial global value'，但它被"某人"更改了，
    # 你需要知道是谁更改了它的上下文。
    # 所以再次强调，只有在你知道自己在做什么时才访问全局和非局部作用域，
    # 否则可能被认为是不好的做法。
