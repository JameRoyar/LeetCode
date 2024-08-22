'''
题目描述

给你一串末加密的字符串str，通过对字符串的每一个字母进行改变来实现加密，加密方式是在每一字母str[i]偏移特定数组元素a[i]的量，数组a前三位已经赋值：a[0]=1,a[1]=2,a[2]=4。


当i>=3时，数组元素a[i]=a[i-1]+a[i-2]+a[i-3]。


例如: 原文 abcde 加密后 bdgkr，其中偏移量分别是1,2,4,7,13。

输入

第一行为一个整数n (1 <= n <= 1000) ，表示有n组测试数据，每组数据包含一行，原文str(只含有小写字母，0 < 长度 <= 50)。

'''

n = int(input())
# s = []
# for i in range(n):
#    s[i] = input()
s = [input() for i in range(n)]


def zip(s):
    n = len(s)
    dp = [0] * n
    if n > 0:
        dp[0] = 1
    if n > 1:
        dp[1] = 2
    if n > 2:
        dp[2] = 4
    if n > 3:
        for i in range(3, n):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    carr = list(s)
    for i in range(n):
        carr[i] = (dp[i]+ord(carr[i])-97)%26+97

    return ''.join(map(chr, carr))

for i in range(n):
    print(zip(s[i]))