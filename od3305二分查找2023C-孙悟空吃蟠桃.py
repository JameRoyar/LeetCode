# 3305: 【二分查找】2023C-孙悟空吃蟠桃
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：admin
# 提交：297
# 解决：143
# 题目描述
# 孙悟空喜欢吃蟠桃，一天他趁守卫蟠桃园的天兵天将离开了而偷偷的来到王母娘娘的蟠桃园偷吃蟠桃。
# 已知蟠桃园有 N 棵蟠桃树，第 i棵蟠桃树上有 N[i]（大于 0）个蟠桃，天兵天将将在 H（不小于蟠桃树棵数）小时后回来。
# 孙悟空可以决定他吃蟠桃的速度 K （单位：个/小时），每个小时他会选择一颗蟠桃树，从中吃掉 K 个蟠桃，如果这棵树上的蟠桃数小于 K ，他将吃掉这棵树上所有蟠桃，然后这一小时内不再吃其余蟠桃树上的蟠桃。
# 孙悟空喜欢慢慢吃，但仍想在天兵天将回来前将所有蟠桃吃完。
# 求孙悟空可以在 H 小时内吃掉所有蟠桃的最小速度 K（K 为整数）。
# 输入
# 第一行输入为 N 个数字，N 表示桃树的数量，这 N 个数字表示每颗桃树上蟠桃的数量
# 第二行输入为一个数字，表示守卫离开的时间 H。
# 其中数字通过空格分割，N、H 为正整数，每颗树上都有蟠桃
#  0 < N < 10000，0< H < 10000。
# 输出
# 吃掉所有蟠桃的最小速度 K（K 为整数），无解或者输入异常时输出 0 。
# 样例输入 复制
# 3 11 6 7 8
# 5
# 样例输出 复制
# 11
# from math import ceil
#
# n = list(map(int, input().split()))
# h = int(input())
#
# def cal(n,k):
#     return sum(ceil(num/k) for num in n)
# def minEatingSpeed(piles, h):
#     n = len(piles)
#     left = 0  # 恒为 False
#     right = max(piles)  # 恒为 True
#     while left + 1 < right:  # 开区间不为空
#         mid = (left + right) // 2
#         if sum((p - 1) // mid for p in piles) <= h - n:
#             right = mid  # 循环不变量：恒为 True
#         else:
#             left = mid  # 循环不变量：恒为 False
#     return right  # 最小的 True
#
#
# s = list(map(int, input().split()))
# h = int(input())
# print(minEatingSpeed(s, h))

n = list(map(int, input().split()))
k = int(input())

left = 0
right = len(n) - 1
while left < right:
    mid = left + int((right - left) / 2)
    if n[mid] == k:
        left = mid + 1
    elif n[mid] > k:
        right = mid - 1
    else:
        left = mid + 1
print(left)
