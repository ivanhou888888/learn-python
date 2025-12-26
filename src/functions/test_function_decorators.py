"""函数装饰器

@see: https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

函数装饰器只是现有函数的包装器。在设计模式的上下文中，
装饰器动态地改变函数、方法或类的功能，而不必直接使用子类。
当你需要扩展不想修改的函数的功能时，这是理想的选择。
我们可以在任何地方实现装饰器模式，但 Python 通过提供更具表现力的特性和语法来促进实现。
"""


def test_function_decorators():
    """函数装饰器。"""

    # 函数装饰器只是现有函数的包装器。将上面提到的想法放在一起，
    # 我们可以构建一个装饰器。在这个例子中，让我们考虑一个函数，
    # 它用 p 标签包装另一个函数的字符串输出。

    # 这是我们想要装饰的函数。
    def greeting(name):
        return "Hello, {0}!".format(name)

    # 这个函数用 <p> 标签装饰另一个函数的输出。
    def decorate_with_p(func):
        def function_wrapper(name):
            return "<p>{0}</p>".format(func(name))
        return function_wrapper

    # 现在，让我们调用我们的装饰器并传递我们想要装饰的函数。
    my_get_text = decorate_with_p(greeting)

    # 好了，我们刚刚装饰了函数输出而没有改变函数本身。
    assert my_get_text('John') == '<p>Hello, John!</p>'  # 使用装饰器。
    assert greeting('John') == 'Hello, John!'  # 不使用装饰器。

    # 现在，Python 通过一些语法糖使创建和使用装饰器对程序员来说更简洁、更好。
    # 有一个简洁的快捷方式，就是在要装饰的函数之前提到装饰函数的名称。
    # 装饰器的名称应该以 @ 符号开头。

    @decorate_with_p
    def greeting_with_p(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_p('John') == '<p>Hello, John!</p>'

    # 现在让我们考虑我们想用另一个函数装饰我们的 greeting 函数，
    # 用 div 包装字符串输出。

    # 这将是我们的第二个装饰器。
    def decorate_with_div(func):
        def function_wrapper(text):
            return "<div>{0}</div>".format(func(text))
        return function_wrapper

    # 使用基本方法，装饰 get_text 将类似于
    # greeting_with_div_p = decorate_with_div(decorate_with_p(greeting_with_p))

    # 使用 Python 的装饰器语法，可以用更强的表现力实现同样的事情。
    @decorate_with_div
    @decorate_with_p
    def greeting_with_div_p(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_div_p('John') == '<div><p>Hello, John!</p></div>'

    # 这里需要注意的一件重要事情是，设置装饰器的顺序很重要。
    # 如果上面示例中的顺序不同，输出也会不同。

    # 向装饰器传递参数。

    # 回顾之前的示例，你可以注意到示例中的装饰器是多么冗余。
    # 2 个装饰器（decorate_with_div、decorate_with_p）每个都有相同的功能，
    # 但用不同的标签包装字符串。我们肯定可以做得更好。
    # 为什么不有一个更通用的实现，将要包装的标签作为字符串？好的！

    def tags(tag_name):
        def tags_decorator(func):
            def func_wrapper(name):
                return "<{0}>{1}</{0}>".format(tag_name, func(name))
            return func_wrapper
        return tags_decorator

    @tags('div')
    @tags('p')
    def greeting_with_tags(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_tags('John') == '<div><p>Hello, John!</p></div>'
