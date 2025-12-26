"""用户输入

@see https://docs.python.org/3/library/functions.html#input

用户输入提示在交互式编程中非常有用。不仅在游戏中，
而且在标准文件操作中，你可能希望用户与程序交互。
因此，用户需要有机会能够输入信息。
"""


def user_input():
	"""输入提示"""

	# 打印语句以向用户发出我们正在等待输入的信号。
	user_input = input("请输入你的名字\n")

	# 根据输入打印消息。
	print(f"欢迎，{user_input}！")
