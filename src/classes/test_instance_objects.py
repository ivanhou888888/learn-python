"""类定义语法

@see: https://docs.python.org/3/tutorial/classes.html#instance-objects
"""


def test_instance_objects():
    """实例对象。

    现在我们可以用实例对象做什么？实例对象理解的唯一操作是属性引用。
    有两种有效的属性名：
    - 数据属性
    - 方法。
    """

    # 数据属性不需要声明；像局部变量一样，它们在第一次赋值时就存在了。
    # 例如，如果 x 是上面创建的 MyCounter 的实例，
    # 以下代码将打印值 16，而不留下任何痕迹。

    # pylint: disable=too-few-public-methods
    class DummyClass:
        """虚拟类"""
        pass

    dummy_instance = DummyClass()

    # pylint: disable=attribute-defined-outside-init
    dummy_instance.temporary_attribute = 1
    assert dummy_instance.temporary_attribute == 1
    del dummy_instance.temporary_attribute
