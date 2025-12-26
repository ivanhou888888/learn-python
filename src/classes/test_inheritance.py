"""继承

@see: https://docs.python.org/3/tutorial/classes.html#inheritance

继承是面向对象编程的原则之一。由于类可能共享很多相同的代码，
继承允许派生类重用相同的代码并相应地修改
"""


# pylint: disable=too-few-public-methods
class Person:
    """基类示例"""
    def __init__(self, name):
        self.name = name

    def get_name(self):
        """获取人名"""
        return self.name


# 派生类定义的语法如下所示。
# pylint: disable=too-few-public-methods
class Employee(Person):
    """派生类示例

    基类（在我们的例子中是 Person）必须在包含派生类定义的作用域中定义。
    在基类名的位置，也允许其他任意表达式。

    派生类可以覆盖其基类的方法。因为方法在调用同一对象的其他方法时没有特殊权限，
    调用同一基类中定义的另一个方法的基类方法可能最终调用覆盖它的派生类方法。

    派生类中的覆盖方法实际上可能想要扩展而不是简单地替换同名的基类方法。
    有一种简单的方法可以直接调用基类方法：只需调用 BaseClassName.methodname(self, arguments)。
    这对客户端有时也很有用。（注意，这只有在基类在全局作用域中可以作为 BaseClassName 访问时才有效。）
    """
    def __init__(self, name, staff_id):
        Person.__init__(self, name)
        # 你也可以在这里使用 super() 以避免显式使用父类名：
        # >>> super().__init__(name)
        self.staff_id = staff_id

    def get_full_id(self):
        """获取完整的员工 ID"""
        return self.get_name() + ', ' + self.staff_id


def test_inheritance():
    """继承。"""

    # 派生类的实例化没有什么特别的：DerivedClassName() 创建类的新实例。
    # 方法引用按如下方式解析：搜索相应的类属性，如有必要沿着基类链向下搜索，
    # 如果这产生一个函数对象，则方法引用是有效的。
    person = Person('Bill')
    employee = Employee('John', 'A23')

    assert person.get_name() == 'Bill'
    assert employee.get_name() == 'John'
    assert employee.get_full_id() == 'John, A23'

    # Python 有两个与继承一起工作的内置函数：
    #
    # - 使用 isinstance() 检查实例的类型：isinstance(obj, int) 只有当
    # obj.__class__ 是 int 或从 int 派生的某个类时才为 True。
    #
    # - 使用 issubclass() 检查类继承：issubclass(bool, int) 为 True，
    # 因为 bool 是 int 的子类。然而，issubclass(float, int) 为 False，
    # 因为 float 不是 int 的子类。

    assert isinstance(employee, Employee)
    assert not isinstance(person, Employee)

    assert isinstance(person, Person)
    assert isinstance(employee, Person)

    assert issubclass(Employee, Person)
    assert not issubclass(Person, Employee)
