"""类定义语法

@see: https://docs.python.org/3/tutorial/classes.html#method-objects

类可以有两种类型的属性引用：数据或方法。类方法通过
[变量名].[方法名]([参数]) 调用，而类数据缺少 ()。
"""


class MyCounter:
    """计数器类的简单示例"""
    counter = 10

    def get_counter(self):
        """返回计数器"""
        return self.counter

    def increment_counter(self):
        """增加计数器"""
        self.counter += 1
        return self.counter


def test_method_objects():
    """方法对象。"""

    # 另一种实例属性引用是方法。方法是"属于"对象的函数。
    # （在 Python 中，术语"方法"不是类实例独有的：其他对象类型也可以有方法。
    # 例如，列表对象有名为 append、insert、remove、sort 等的方法。
    # 然而，在下面的讨论中，我们将专门使用术语"方法"来表示类实例对象的方法，
    # 除非另有明确说明。）

    # 但要注意 counter.get_counter() 与 MyCounter.get_counter() 不是同一回事——
    # 它是一个方法对象，而不是函数对象。

    # 通常，方法在绑定后立即被调用
    counter = MyCounter()
    assert counter.get_counter() == 10

    # 然而，不必立即调用方法：counter.get_counter() 是一个方法对象，
    # 可以存储起来稍后调用。例如：
    get_counter = counter.get_counter
    assert get_counter() == 10

    # 当方法被调用时到底发生了什么？你可能注意到上面调用 counter.get_counter()
    # 时没有参数，尽管 get_counter() 的函数定义指定了一个参数（self）。
    # 参数发生了什么？当然，当一个需要参数的函数在没有任何参数的情况下被调用时，
    # Python 会引发异常——即使参数实际上没有被使用……

    # 实际上，你可能已经猜到了答案：方法的特殊之处在于实例对象作为函数的
    # 第一个参数传递。在我们的例子中，调用 counter.get_counter() 完全等同于
    # MyCounter.get_counter(counter)。一般来说，用 n 个参数的列表调用方法
    # 等同于用通过在第一个参数之前插入方法的实例对象创建的参数列表调用相应的函数。

    assert counter.get_counter() == 10
    assert MyCounter.get_counter(counter) == 10
