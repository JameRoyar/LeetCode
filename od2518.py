# 2518: 【模拟】2023C-字符串分割（二）
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：272
# 解决：93
# 题目描述
# 给定一个非空字符串S，其被N个'-'分隔成N+1的子串，给定正整数K，要求除第一个子串外，其余的子串每K个字符组成新的子串，并用'-'分隔。
#
# 对于新组成的每一个子串，如果它含有的小写字母比大写字母多，则将这个子串的所有大写字母转换为小写字母; 反之，如果它含有的大写字母比小写字母多，则将这个子串的所有小写字母转换为大写字母，大小写字母的数量相等时，不做转换。
#
# 输入
# 输入为两行，第一行为参数K，第二行为字符串S.
# 输出
# 输出转换后的字符串。
# 样例输入 复制
# 3
# 12abc-abCABc-4aB@
# 样例输出 复制
# 12abc-abc-ABC-4aB-@
# 提示
# 子串为12abc、abCABc、4aB@，第一个子串保留,后面的子串每3个字符一组为abC、ABc、4aB、@。
#
# abC中小写字母较多，转换为abc
#
# ABc中大写字母较多，转换为ABC
#
# 4aB中大小写字母都为1个，不做转换
#
# @中没有字母
#
# 连起来即12abc-abc-ABC-4aB-@

def res(sub):
    upper = 0
    lower = 0
    for ch in sub:
        if ch.islower():
            lower+=1
        if ch.isupper():
            upper+=1
    if upper == lower:
        return sub
    return sub.lower() if lower>upper else sub.upper()



#输入处理
n = int(input())
s = input().split("-")

#字符串处理
str1 = s[0]
str2 = "".join(s[1:])

ans = []
for idx in range(0, len(str2), n):
    sub = str2[idx:idx + n]
    ans.append(res(sub))

print("-".join([s[0]]+ans))