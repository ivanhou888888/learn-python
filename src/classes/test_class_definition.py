"""类定义语法

@see: https://docs.python.org/3/tutorial/classes.html

Python 是一种面向对象的编程语言。
Python 中几乎所有东西都是对象，具有其属性和方法。
类就像一个对象构造器，或者创建对象的"蓝图"。
"""


def test_class_definition():
    """类定义。"""

    # 类定义，像函数定义（def 语句）一样，必须在它们生效之前执行。
    # （你可以想象将类定义放在 if 语句的分支中，或者放在函数内部。）

    class GreetingClass:
        """类定义示例

        这个类包含两个公共方法，不包含构造函数。
        """
        name = 'user'

        def say_hello(self):
            """类方法。"""
            # self 参数是对类本身的引用，用于访问属于类的变量。
            # 它不必命名为 self，你可以随意命名，
            # 但它必须是类中任何函数的第一个参数。
            return 'Hello ' + self.name

        def say_goodbye(self):
            """类方法。"""
            return 'Goodbye ' + self.name

    # 当进入类定义时，会创建一个新的命名空间，并用作局部作用域——
    # 因此，所有对局部变量的赋值都进入这个新的命名空间。
    # 特别是，函数定义在这里绑定新函数的名称。

    # 类实例化使用函数表示法。只需假装类对象是一个无参数函数，
    # 返回类的新实例。例如，以下代码将创建类的新实例，
    # 并将此对象赋给局部变量。
    greeter = GreetingClass()

    assert greeter.say_hello() == 'Hello user'
    assert greeter.say_goodbye() == 'Goodbye user'
