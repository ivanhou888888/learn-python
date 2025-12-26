"""类变量和实例变量

@see: https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables

一般来说，实例变量用于每个实例唯一的数据，
类变量用于类的所有实例共享的属性和方法。
"""


def test_class_and_instance_variables():
    """类变量和实例变量。"""

    # pylint: disable=too-few-public-methods
    class Dog:
        """Dog 类示例"""
        kind = 'canine'  # 所有实例共享的类变量。

        def __init__(self, name):
            self.name = name  # 每个实例唯一的实例变量。

    fido = Dog('Fido')
    buddy = Dog('Buddy')

    # 所有狗共享。
    assert fido.kind == 'canine'
    assert buddy.kind == 'canine'

    # fido 独有。
    assert fido.name == 'Fido'

    # buddy 独有。
    assert buddy.name == 'Buddy'

    # 共享数据在涉及可变对象（如列表和字典）时可能会产生令人惊讶的效果。
    # 例如，以下代码中的 tricks 列表不应该用作类变量，
    # 因为只有一个列表会被所有 Dog 实例共享。

    # pylint: disable=too-few-public-methods
    class DogWithSharedTricks:
        """错误使用共享变量的 Dog 类示例"""
        tricks = []  # 对可变对象错误使用类变量（见下文）。

        def __init__(self, name):
            self.name = name  # 每个实例唯一的实例变量。

        def add_trick(self, trick):
            """给狗添加技巧

            这个函数说明了对可变类变量 tricks 的错误使用（见下文）。
            """
            self.tricks.append(trick)

    fido = DogWithSharedTricks('Fido')
    buddy = DogWithSharedTricks('Buddy')

    fido.add_trick('roll over')
    buddy.add_trick('play dead')

    assert fido.tricks == ['roll over', 'play dead']  # 意外地被所有狗共享
    assert buddy.tricks == ['roll over', 'play dead']  # 意外地被所有狗共享

    # 类的正确设计应该使用实例变量：

    # pylint: disable=too-few-public-methods
    class DogWithTricks:
        """Dog 类示例"""

        def __init__(self, name):
            self.name = name  # 每个实例唯一的实例变量。
            self.tricks = []  # 为每只狗创建一个新的空列表

        def add_trick(self, trick):
            """给狗添加技巧

            这个函数说明了对可变类变量 tricks 的正确使用（见下文）。
            """
            self.tricks.append(trick)

    fido = DogWithTricks('Fido')
    buddy = DogWithTricks('Buddy')

    fido.add_trick('roll over')
    buddy.add_trick('play dead')

    assert fido.tricks == ['roll over']
    assert buddy.tricks == ['play dead']
