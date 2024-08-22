# 2581: 【系统设计】2023C-模拟目录管理
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：83
# 解决：26
# 题目描述
# 实现一个模拟目录管理功能的软件，输入一个命令序列，输出最后一条命令运行结果。
#
#
#  支持命令：
#
# 1) 创建目录命令：mkdir 目录名称，如mkdir abc为在当前目录创建abc目录，如果已存在同名目录则不执行任何操作。此命令无输出。
#
# 2) 进入目录命令：cd 目录名称，如cd abc为进入abc目录，特别地，cd ..为返回上级目录，如果目录不存在则不执行任何操作。此命令无输出。
#
# 3) 查看当前所在路径命令：pwd，输出当前路径字符串。
#
#
# 约束:
#
# 1) 目录名称仅支持小写字母；mkdir和cd命令的参数仅支持单个目录，如mkdir abc和cd abc;不支持嵌套路径和绝对路径，如mkdir abc/efg，cd abc/efq是不支持的。
#
# 2) 目录符号为/，根目录/作为初始目录。
#
# 3) 任何不符合上述定义的无效命令不做任何处理并且无输出。
#
# 输入
# 输入N行字符串，每一行字符串是一条命令
# 输出
# 输出最后一条命令运行结果字符串
# 样例输入 复制
# mkdir abc
# cd abc
# pwd

class File:
    def __init__(self, name):
        self.name = name  # 文件或目录的名称
        self.parent = None  # 父目录
        self.sub_file = {}  # 子文件或子目录的字典

    def mkdir(self, dir):
        # 如果目录已经存在，直接返回
        if dir in self.sub_file:
            return
        # 创建新的目录，并设置父目录
        new_file = File(dir)
        new_file.parent = self
        self.sub_file[dir] = new_file

    def cd(self, dir):
        # 切换到父目录
        if dir == "..":
            if self.parent is not None:
                return self.parent
        # 切换到子目录
        if dir in self.sub_file:
            return self.sub_file[dir]
        # 如果目录不存在，保持在当前目录
        return self

    def pwd(self):
        temp = self
        path = "/"
        # 从当前目录向上遍历，构建完整路径
        while temp.parent is not None:
            path = "/" + temp.name + path
            temp = temp.parent
        return path

if __name__ == "__main__":
    root = File("")
    cur = root

    while True:
        try:
            command = input()  # 读取用户输入的命令
            if command.startswith("mkdir"):
                dir = command[6:]
                cur.mkdir(dir)
            elif command.startswith("cd"):
                dir = command[3:]
                cur = cur.cd(dir)
            elif command == "pwd":
                print(cur.pwd())
            elif command == "exit":
                break  # 退出循环
        except EOFError:
            break  # 处理EOFError以便于从文件中读取命令

