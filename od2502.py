'''
题目描述
有一种简易压缩算法: 针对全部由小写英文字母组成的字符串，将其中连续超过两个相同字母的部分压缩为连续个数加该字母，其他部分保持原样不变。

例如: 字符串"aaabbccccd"经过压缩成为字符串"3abb4cd"。

请您编写解压函数，根据输入的字符串，判断其是否为合法压缩过的字符串若输入合法则输出解压缩后的字符串，否则输出字符串"!error"来报告错误。
'''



'''
# 这是一个函数，其功能是将字符串 s 转换为另一个字符串，该字符串是 s 中每个非数字字符的 n 次出现的字符串的乘积。下面是加上注释后的代码：
def result(s):
    # 定义一个字符串变量 ans，初始为空字符串
    ans = ""
    # 定义一个变量 i，初始值为 0
    i = 0
    # 开始循环，直到 i 等于字符串 s 的长度
    while i < len(s):
        # 如果当前字符不是数字或小写字母，则返回错误信息
        if not (s[i].isdigit() or s[i].islower()):
            # 如果当前字符是数字，则将其添加到一个数字列表中
            return "!error"
        # 如果当前字符是数字，则执行以下操作
        if s[i].isdigit():
            # 定义一个列表变量 num，初始为空列表
            num = []
            # 将当前字符添加到列表变量 num 中
            num.append(s[i])
            # 定义一个变量 j，初始值为 i + 1
            j = i + 1
            # 开始循环，直到 j 等于字符串 s 的长度或当前字符不是数字
            while s[j].isdigit():
                # 将当前字符添加到列表变量 num 中
                num.append(s[j])
                # 将 j 增加 1
                j += 1
            # 如果 j 等于字符串 s 的长度或当前字符不是数字或小写字母，则返回错误信息
            if not (s[j].isdigit() or s[j].islower()):
                return "!error"
            # 如果列表变量 num 的长度为 1 且整数变量 int("".join(num)) 小于等于 2，则返回错误信息
            if len(num) == 1 and int(num[0]) <= 2:
                return "!error"
            else:
                # 定义一个整数变量 cot，表示当前字符出现的次数
                cot = int("".join(num))
                # 定义一个字符串变量 tmp，表示当前字符出现 c 次的字符串
                tmp = s[j] * cot
                # 将字符串变量 tmp 添加到字符串变量 ans 中
                ans += tmp

                # 打印字符串变量 ans
                i = j
        # 如果当前字符不是数字或小写字母，则将其添加到字符串变量 ans 中
        else:
            ans += s[i]
        # 将 i 增加 1
        i += 1
    # 返回字符串变量 ans
    return ans


# 调用函数 result，并将字符串 s 作为参数传递
print(result(s))
'''

s = 'dd3cd4fd3f'
def compressing_str(s):
    sb = []
    i = 0
    while i < len(s):
        if not (s[i].isdigit() or s[i].islower()):
            return "!error"
        elif s[i].isdigit():
            num = int(s[i])
            i += 1
            # 继续读取数字直到非数字字符
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            # 错误检查
            if i >= len(s) or not s[i].islower() or num <= 2 or (sb and s[i] == sb[-1]):
                return "!error"
            for j in range(num):
                sb.append(s[i])
        elif s[i].islower():
            # 错误检查
            if len(sb) >= 2 and sb[-2:] == s[i] * 2:
                return "!error"
            if i + 1 < len(s) and s[i] != s[i + 1]:
                return "!error"
            sb.append(s[i])
        else:
            return "!error"
        i += 1
    return ''.join(sb)


print(compressing_str(s))

'''
========[test_4.out]=========
Expected						      |	Yours
aaaffdddccjjjjjjabcdsss
							      |	!error

==============================
'''
