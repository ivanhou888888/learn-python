"""日期和时间

@see: https://docs.python.org/3/tutorial/stdlib.html#dates-and-times

datetime 模块提供了以简单和复杂方式操作日期和时间的类。
虽然支持日期和时间算术，但实现的重点是高效的成员提取，
用于输出格式化和操作。该模块还支持时区感知的对象。
"""

from datetime import date


def test_datetime():
    """日期和时间"""

    real_now = date.today()
    assert real_now

    fake_now = date(2018, 8, 29)

    assert fake_now.day == 29
    assert fake_now.month == 8
    assert fake_now.year == 2018
    assert fake_now.ctime() == 'Wed Aug 29 00:00:00 2018'
    assert fake_now.strftime(
        '%m-%d-%y. %d %b %Y is a %A on the %d day of %B.'
    ) == '08-29-18. 29 Aug 2018 is a Wednesday on the 29 day of August.'

    # 日期支持日历算术。
    birthday = date(1964, 7, 31)
    age = fake_now - birthday

    assert age.days == 19752
