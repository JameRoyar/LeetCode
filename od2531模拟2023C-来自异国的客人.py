# 2531: 【模拟】2023C-来自异国的客人
# 有位客人来自异国，在该国使用m进制计数。该客人有个幸运数字n(n < m)，每次购物时，其总是喜欢计算本次支付的花费（折算为异国的价格后）中存在多少幸运数字。问: 当其购买一个在我国价值k的产品时，其中包含多少幸运数字?
# 输入
# 第一行输入为k n m
#
# k 表示 该客人购买的物品价值 (以十进制计算的价格)
#
# n 表示 该客人的幸运数字
#
# m 表示 该客人所在国度的采用的进制
#
# 输出
# 输出幸运数字的个数，行末无空格.
# 样例输入 复制
# 10 2 4
# 样例输出 复制
# 2
# 将十进制数字n转化为m进制的函数
# 由于m可能超过9，因此用列表而非字符串储存最终的结果
def convert_from_10_to_m(n, m):
    # 处理特殊情况
    if n == 0:
        return [0]
    # 用一个数组记录最终的转化结果
    result = list()
    # 进行循环，直到n变为0
    while n > 0:
        # 通过取余数得到当前位的数字digit
        digit = n % m
        # 将余数转化为对应的字符并添加到结果字符串的开头
        result.append(digit)
        # 更新n为n除以m的整数部分
        n //= m
    # 由于低位是先被存在result中的，最后需要进行反转才能得到最终结果
    # 由于本题最终是统计包含的幸运数字n，所以此处也可以不反转
    return result[::-1]


# 输入十进制数字k，幸运数字n，进制m
k, n, m = map(int, input().split())

# 调用函数进行转换并输出k转化为m进制的结果k
res = convert_from_10_to_m(k, m)

# 统计res中包含多少个n
print(sum(int(digit) == n for digit in res))
