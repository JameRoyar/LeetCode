'''
给定两个字符串，从字符串2中找出字符串1中的所有字符，去重并按照ASCII值从小到大排序。

输入字符串1：长度不超过1024

输入字符串2：长度不超过1000000

字符范围满足ASCII编码要求，按照ASCII的值由小到大排序

输入
bach

bbaaccedfg

输出
abc

输入字符串1 为给定字符串bach，输入字符串2为bbaaccedfg，从字符串2中找出字符串1的字符，去除重复的字符，并且按照ASCII值从小到大排序，得到输出的结果为abc。

字符串1中的字符h在字符串2中找不到不输出
'''

aim = list(input())
str = list(input())


def findStr(s, st):
    ans = []
    st = list(set(st))
    for i in st:
        if i in s:
            ans.append(i)
    if ans:
        print("".join(sorted(ans)))
        return


findStr(aim, str)
