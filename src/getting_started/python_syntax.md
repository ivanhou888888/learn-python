# Python 语法

**Python 语法与其他编程语言的比较**

- Python 的设计注重可读性，与英语有一些相似之处，并受到数学的影响。
- Python 使用换行来完成命令，而其他编程语言通常使用分号或括号。
- Python 依赖缩进（使用空白字符）来定义作用域，例如循环、函数和类的作用域。其他编程语言通常使用花括号来实现这一目的。

## Python 缩进

在其他编程语言中，代码缩进仅用于提高可读性，但在 Python 中，缩进非常重要。

Python 使用缩进来表示代码块。

```python
if 5 > 2:
  print("Five is greater than two!")
```

如果跳过缩进，Python 会报错。

## 注释

Python 具有注释功能，用于代码内文档说明。

注释以 `#` 开头，Python 会将该行的其余部分视为注释：

```python
#这是一条注释。
print("Hello, World!")
```

## 文档字符串

Python 还具有扩展的文档功能，称为文档字符串（docstrings）。

文档字符串可以是单行或多行的。文档字符串也是注释：

Python 在文档字符串的开头和结尾使用三引号：

```python
"""这是一个
多行文档字符串。"""
print("Hello, World!")
```

## 参考资料

- [w3schools.com](https://www.w3schools.com/python/python_syntax.asp)
