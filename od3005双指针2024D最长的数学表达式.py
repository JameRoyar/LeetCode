# 3005: 【双指针】2024D-提取字符串中最长数学表达式
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：100
# 解决：25
# 题目描述
# 提取字符串中的最长合法简单数学表达式，字符串长度最长的，并计算表达式的值。
#
# 如果没有，则返回0。 简单数学表达式只能包含以下内容：0-9数字，符号 +-*
#
# 说明：
#
# 1. 所有数字，计算结果都不超过long
#
# 2. 如果有多个长度一样的，请返回第一个表达式的结果
#
# 3. 数学表达式，必须是最长的，合法的
#
# 4. 操作符不能连续出现，如 +--+1 是不合法的
#
# 输入
# 字符串
# 输出
# 表达式值
# 样例输入 复制
# 1-2abcd
# 样例输出 复制
# -1
# 来源/分类
# 栈 双指针 华为OD真题-100分




# 输入获取
import re

s = input()


# 计算合法表达式的结果
def calcExpStr(exp):
    # 这里在表达式结尾追加"+0"是为了避免后面收尾操作，不理解的话，可以去掉此步，测试下"1-2"
    exp += '+0'

    # 记录表达式中各块的操作数
    stack = []
    # 各块操作数的"值"部分的缓存容器
    numStr = []

    # 各块操作数的"系数"部分，默认为1
    num_coef = 1

    # 如果合法的表达式可以+或-开头
    start = exp[0]
    if start == '+' or start == '-':
        # 将exp开头的符号去掉
        exp = exp[1:]

    if start == '-':
        # 如果表达式开头是负号，则开头操作数的系数为-1
        num_coef = -1

    # 处理剩余表达式
    for c in exp:
        if '9' >= c >= '0':
            numStr.append(c)
            continue

        # 如果扫描到的字符c是运算符，那么该运算符打断了前面操作数的扫描，前面操作数 = 系数 * 值
        num = num_coef * int("".join(numStr))
        stack.append(num)

        # 清空缓存容器，用于下一个操作数的”值“记录
        numStr.clear()

        if c == '+':
            # 如果运算符是加法，则后一个操作数的系数为1
            num_coef = 1
        elif c == '-':
            # 如果运算符是减法，则后一个操作数的系数为-1
            num_coef = -1
        elif c == '*':
            # 如果运算符是乘法，则后一个操作数的系数为栈顶值，比如2*3，其中2可以当作3的系数
            num_coef = stack.pop()

    # 表达式分块后，每一块独立计算，所有块的和就是表达式的结果
    return sum(stack)


# 获取最长合法表达式
def getMaxLenExp():
    # 下面正则无法匹配这样的数字串：+1+2
    # lst = re.compile(r"((?:\d+[+*-])*\d+)").findall(s)

    # 下面正则可以匹配到这样的数字串：+1+2
    lst = re.compile(r"([+-]?(?:\d+[+*-])*\d+)").findall(s)

    maxLenExp = ""

    for exp in lst:
        if len(exp) > len(maxLenExp):
            maxLenExp = exp

    return maxLenExp


# 算法入口
def getResult():
    maxLenExp = getMaxLenExp()

    if len(maxLenExp) == 0:
        return 0
    else:
        return calcExpStr(maxLenExp)


# 算法调用
print(getResult())
