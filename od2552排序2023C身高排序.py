# ，请加微信 联系 od1336
# 2552: 【排序】2023C-身高排序
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：191
# 解决：126
# 题目描述
# 小明今年升学到了小学一年级，来到新班级后，发现其他小朋友身高参差不齐，然后就想基于各小朋友和自己的身高差，对他们进行排序，请帮他实现排序。
# 输入
# 第一行为正整数H和N，其中0 < H < 200 为小明的身高，0 < N < 50 为新班级其他小朋友个数。
#
# 第二行为 N 个正整数H1 ~ Hn分别是其他小朋友的身高，取值范围0 < Hi < 200，且N个正整数各不相同。
#
# 输出
# 输出排序结果，各正整数以空格分割，和小明身高差绝对值最小的小朋友排在前面，和小明身高差绝对值最大的小朋友排在后面，如果两个小朋友和小明身高差一样，则个子较小的小朋友排在前面。
# 样例输入 复制
# 100 10
# 95 96 97 98 99 101 102 103 104 105
# 样例输出 复制
# 99 101 98 102 97 103 96 104 95 105
import collections

# # raw_input
# h, n = map(int, input().split())
# lst = list(map(int, input().split()))
#
# # solution
# hlst = [abs(h - hi) for hi in lst]
# idx = list(zip(lst, hlst))
#
# idx.sort(key=lambda x: (x[1], x[0]))
# print(" ".join(str(item[0]) for item in idx))

# raw_input
# n = int(input())
# a1, a2, a3, a4, a5 = map(int, input().split())
# lst = list()
# for _ in range(n):
#     name, b1, b2, b3, b4, b5 = input().split()
#     hot = a1 * int(b1) + a2 * int(b2) + a3 * int(b3) + a4 * int(b4) + a5 * int(b5)
#     lst.append((name, hot))
#
# lst.sort(key=lambda x: (-x[1], x[0].lower()))
# for name, hot in lst:
#     print(name)

# lst = input().split(",")
# tmp = list()
# for i in range(len(lst)):
#     name = lst[i][0:2]
#     num = lst[i][2:]
#     tmp.append((name, num))
# tmp.sort(key=lambda x: (x[0], int(x[1])))
# print(",".join([x[0]+x[1] for x in tmp]))

# n, m = map(int, input().split())
# k = list(input().split())
# lst = list()
# for _ in range(n):
#     lst.append(list(input().split()))
# e = input()
#
# if e in k:
#     a = k.index(e)
#     lst.sort(key=lambda x: (x[a + 1]), reverse=True)
# else:
#     lst.sort(key=lambda x: (sum(int(x[i]) for i in range(1, m + 1))), reverse=True)
# print(" ".join(k[0] for k in lst))

lst = list(map(int, input().split(",")))
dic = collections.defaultdict(int)

for i in lst:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
# print(",".join(str(sorted(dic.items(), key=lambda x: -x[1]))))
print(",".join(str(k) for k in dic.keys()))
