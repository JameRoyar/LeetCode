# 4205: 【前缀和】2024D-查找接口成功率最优时间段
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：121
# 解决：47
# 题目描述
# 服务之间交换的接口成功率作为服务调用关键质量特性，某个时间段内的接口失败率使用一个数组表示，数组中每个元素都是单位时间内失败率数值，数组中的数值为 0~100 的整数，给定一个数值(minAverageLost)表示某个时间段内平均失败率容忍值，即平均失败率小于等于 minAverageLost，找出数组中最长时间段，如果未找到则直接返回 NULL。
# 输入
# 输入有两行内容，第一行为minAverageLost，第二行为数组，数组元素通过空格" "分隔，minAverageLost 及数组中元素取值范围为 0~100 的整数，数组元素的个数不会超过 100 个。
# 输出
# 找出平均值小于等于 minAverageLost 的最长时间段，输出数组下标对，格式{beginIndex}-{endIndx}(下标从 0 开始)，如果同时存在多个最长时间段，则输出多个下标对且下标对之间使用空格" "拼接，多个下标对按下标从小到大排序。
# 样例输入 复制
# 2
# 0 0 100 2 2 99 0 2
# 样例输出 复制
# 0-1 3-4 6-7
# 提示
# A、输入解释：minAverageLost = 2，数组[0, 0, 100, 2, 2, 99, 0, 2]
#
# B、通过计算小于等于 2 的最长时间段为：数组下标为 0-1 即[0, 0]，数组下标为 3-4 即[2, 2]，数组下标为 6-7 即[0, 2]，这三个部分都满足平均值小于等 2 的要求，因此输出 0-1 3-4 6-7

n = int(input())
lst = list(map(int, input().split()))


def find_interval(lst, n):
    ans = []
    max_len = 0
    for i in range(len(lst) - 1):
        for j in range(i, len(lst)):
            if sum(lst[i:j + 1]) <= n * len(lst[i:j + 1]):
                ans.append((i, j))
                max_len = max(max_len, j - i + 1)
    ans = [(i, j) for i, j in ans if j - i + 1 == max_len]
    return ' '.join(f"{i}-{j}" for (i, j) in ans)


print(find_interval(lst, n))

# 6701: 【前缀和】美团2023秋招-平均数为k的最长连续子数组
# 内存限制：128 MB
# 时间限制：3.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：84
# 解决：40
# 题目描述
# 给定n个正整数组成的数组，求平均数正好等于k的最长连续子数组的长度。
# 输入
# 第一行输入两个正整数n和k，用空格隔开。
#
# 第二行输入n个正整数ai，用来表示数组。
#
# 1 <= n <= 200000
#
# 1 < = k, ai <= 10^9
#
# 输出
# 如果不存在任何一个连续子数组的平均数等于k，则输出-1。
#
# 否则输出平均数正好等于k的最长连续子数组的长度。
#
# 样例输入 复制
# 5 2
# 1 3 2 4 1

n,k = map(int,input().split())
lst = list(map(int, input().split()))

def find_interval(lst, n):
    ans = []
    max_len = 0
    for i in range(len(lst) - 1):
        for j in range(i, len(lst)):
            if sum(lst[i:j + 1]) == n * len(lst[i:j + 1]):
                ans.append((i, j))
                max_len = max(max_len, j - i + 1)

    if max_len == 0: return -1
    return max_len


print(find_interval(lst, k))
