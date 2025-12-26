"""多重继承

@see: https://docs.python.org/3/tutorial/classes.html#multiple-inheritance

某些类可能从多个类派生。这意味着派生类将具有其属性，
以及它派生自的所有类的属性。
"""


def test_multiple_inheritance():
    """多重继承"""

    # pylint: disable=too-few-public-methods
    class Clock:
        """时钟类"""

        time = '11:23 PM'

        def get_time(self):
            """获取当前时间

            方法是硬编码的，仅用于多重继承说明。
            """
            return self.time

    # pylint: disable=too-few-public-methods
    class Calendar:
        """日历类"""

        date = '12/08/2018'

        def get_date(self):
            """获取当前日期

            方法是硬编码的，仅用于多重继承说明。
            """
            return self.date

    # Python 也支持一种多重继承形式。具有多个基类的类定义如下所示。
    class CalendarClock(Clock, Calendar):
        """使用多重继承的类。

        对于大多数目的，在最简单的情况下，你可以将从父类继承的属性搜索
        视为深度优先、从左到右，在层次结构中有重叠的地方不会在同一个类中搜索两次。
        因此，如果在 CalendarClock 中找不到属性，则在 Clock 中搜索，
        然后（递归地）在 Clock 的基类中搜索，如果在那里找不到，
        则在 Calendar 中搜索，依此类推。

        实际上，它比这稍微复杂一些；方法解析顺序动态变化以支持对 super() 的协作调用。
        这种方法在其他一些多重继承语言中被称为 call-next-method，
        比单继承语言中的 super 调用更强大。

        动态排序是必要的，因为所有多重继承的情况都表现出一个或多个菱形关系
        （其中至少一个父类可以通过从最底层类的多条路径访问）。
        例如，所有类都继承自 object，所以任何多重继承的情况都提供了多条到达 object 的路径。
        为了防止基类被访问多次，动态算法以一种保留每个类中指定的从左到右顺序、
        只调用每个父类一次且是单调的（意味着一个类可以被子类化而不影响其父类的优先顺序）
        的方式线性化搜索顺序。
        """

    calendar_clock = CalendarClock()

    assert calendar_clock.get_date() == '12/08/2018'
    assert calendar_clock.get_time() == '11:23 PM'
