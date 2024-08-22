# 3400: 【DP】2024
# D - 分班
# 内存限制：128
# MB
# 时间限制：2.000
# S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：336
# 解决：112
# 题目描述
#
# 幼儿园两个班的小朋友在排队时混在了一起，每位小朋友都知道自己是否与前面一位小朋友是否同班，请你帮忙把同班的小朋友找出来。小朋友的编号为整数，与前一位小朋友同班用Y表示，不同班用N表示。
#
# 输入
#
# 输入为空格分开的小朋友编号和是否同班标志。
#
#
# 比如: 6 / N
# 2 / Y
# 3 / N
# 4 / Y，表示共4位小朋友，2
# 和6同班， 3
# 和2不同班，4
# 和3同班。
#
#
# 其中，小朋友总数不超过999，每个小朋友编号大于0，小于等于999。不考虑输入格式错误问题。
#
# 输出
# 输出为两行，每一行记录一个班小朋友的编号，编号用空格分开。 且:
#
# 1.
# 编号需要按照大小升序排列，分班记录中第一个编号小的排在第一行；
#
# 2.
# 若只有一个班的小朋友，第二行为空行；
#
# 3.
# 若输入不符合要求，则直接输出字符串ERROR。
#
# 样例输入
# 复制
# 6 / N
# 2 / Y
# 3 / N
# 4 / Y
# 样例输出
# 复制
# 2
# 6
# 3
# 4

child = list()
yn = list()

while True:
    try:
        s = input()
        ch, cla = s.split("/")
        child.append(int(ch))
        yn.append(cla)
    except:
        print("ERROR!")
        break

n = len(child)
dp = [None] * n
dp[0] = True
for i in range(1, n):
    if yn[i] == "Y":
        dp[i] = dp[i - 1]
    if yn[i] == "N":
        dp[i] = not dp[i - 1]

class1, class2 = list(), list()
for i in range(n):
    class1.append(child[i]) if dp[i] else class2.append(child[i])

class1.sort()
class2.sort()

if len(class2) == 0:
    print(" ".join(map(str, class1)))
    print("")
else:
    if class1[0] > class2[0]:
        class1, class2 = class2, class1
    print(" ".join(map(str, class1)))
    print(" ".join(map(str, class2)))
