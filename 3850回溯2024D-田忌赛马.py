# 给定两个只包含数字的数组 a, b，调整数组 a 里面数字的顺序，使得尽可能多的 a[i] > b[i]。数组 a 和 b 中的数字各不相同。
#
# 输出所有可以达到最优结果的 a 数组数量
#
# 输入
# 输入的第一行是数组 a 中的数字， 输入的第二行是数组 b 中的数字， 其中只包含数字，每两个数字之间相隔一个空格，a，b 数组大小不超过 10
# 输出
# 输出所有可以达到最优结果的 a 数组数量
# 样例输入 复制
# 11 12 20
# 10 13 7
# 样例输出 复制
# 2
# 提示
# 有两个 a 数组的排列可以达到最优结果，[12, 20, 11]和[11, 20, 12]，故输出 2
#
# 达到最优结果的数组数量
# 注意到a,b 数组大小不超过 1θ,很容易想到可以用回溯枚举的方式,列举出所有具有 max_win_num 组胜利的数组 a的排列。
# 这里的回溯无非是在数组a的全排列α的基础上,加上若干题意的限制条件。
# 数组大小最大为10,一共存在 10!=3628800~=10~6 种排列情况,如果不加以剪枝,全部枚举出来,可能会导致超时。
# 对于每一层递归,考虑剩余可选择的元素个数rest_not_used=used.count(False)。本题存在两种剪枝策略:
# 1. 当 rest_not_used 个元素全部都选上,数组 a 的胜利总组数 rest_not_used + win_num 都无法到达 max_win_num 组时,在当前状态继续
# 进行递归已经没有意义了,可以直接剪枝
# 2. 当当前胜利组数已经等于最大胜利组数,即 win_num == max_win_num 成立时,剩余的 rest_not_used 个元素一共可以带来
# factorial(rest_not_used)种排列,无需通过回溯获得这些排列的具体结果,直接令答案数量加上 factorial(rest_not_used)即可
# 题目：【回溯】2023C-田忌赛马
# 分值：200
# 作者：许老师-闭着眼睛学数理化
# 算法：贪心/回溯
# 代码看不懂的地方，请直接在群上提问
from math import factorial

# # 导入计算阶乘的函数
# from math import factorial
#
#
# def dfs(a, b, idx_b, n, win_num, used):
#     global ans
#     # 数组a中，还没选择的个数rest_not_used
#     # 即为used中值为False的个数
#     # 或者n-idx_b，也是rest_not_used的值
#     rest_not_used = used.count(False)
#     # 剪枝：
#     # 如果rest_not_used个元素全部都选上
#     # 都无法到达max_win_num组，则无需继续考虑，直接剪枝
#     if max_win_num > win_num + rest_not_used:
#         return
#     # 如果当前排列能够胜利的组数win_num等于max_win_num
#     # 说明剩余尚未选择的rest_not_used个元素，
#     # 无论如何排列，都一定是一组要求的答案
#     # 根据排列组合，剩余的rest_not_used个元素，
#     # 一共有factorial(rest_not_used)中排列方式
#     if win_num == max_win_num:
#         ans += factorial(rest_not_used)
#         return
#     # 考虑所有位置
#     for idx_a in range(n):
#         # 如果已经使用，则直接跳过
#         if used[idx_a]:
#             continue
#         # 状态更新
#         used[idx_a] = True
#         # a[idx_a]和b[idx_b]进行比较
#         # 如果前者大于后者，则win_num需要+1，否则不变
#         # 同时idx_b需要+1
#         dfs(a, b, idx_b+1, n, win_num + int(a[idx_a] > b[idx_b]), used)
#         # 回滚
#         used[idx_a] = False
#
#
# # 输入a，b数组
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# n = len(a)
#
# # 基于贪心思想，计算出a数组经过排序之后的最大胜利组数
# max_win_num = 0
#
# # 对数组a、b进行从大到小的排序
# a.sort(reverse=True)
# b.sort(reverse=True)
# # 初始化两个指针，分别指向a和b的开头位置
# idx_a, idx_b = 0, 0
#
# # 循环
# # 贪心策略：拿当前a中最大的值a[idx_a]
# # 和b中小于a[idx_a]的数中的最大值，进行配对
# while idx_b < n:
#     # 如果当前a的最大值大于当前b的最大值
#     # 让a[idx_a]和b[idx_b]进行匹配
#     if a[idx_a] > b[idx_b]:
#         idx_a += 1
#         idx_b += 1
#         max_win_num += 1
#     # 否则让idx_b右移，寻找一个能够跟a[idx_a]匹配的最大值
#     else:
#         idx_b += 1
#
# ans = 0
#
# # 如果a全输，则没有最优策略，直接输出0
# if max_win_num == 0:
#     print(ans)
# # 否则，才有进行回溯，计算具有最优策略的a数组排列的数量
# else:
#     used = [False] * n
#     dfs(a, b, 0, n, 0, used)
#     print(ans)

# input
a = list(map(int, input().split()))
b = list(map(int, input().split()))
n = len(a)
a.sort(reverse=True)
b.sort(reverse=True)
# calculate max_win
idx_a, idx_b = 0, 0
max_win = 0
while idx_b < n:
    if a[idx_a] > b[idx_b]:
        idx_a += 1
        idx_b += 1
        max_win += 1
    else:
        idx_b += 1

# dfs
ans = 0
visited = [False] * n


def dfs(win_num, idx):
    global ans
    number_left = visited.count(False)
    if max_win > win_num + number_left:
        return
    if win_num == max_win:
        ans += factorial(number_left)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        dfs(win_num + int(a[i] > b[idx]),idx+1)
        visited[i] = False


if max_win == 0:
    print(ans)
else:
    dfs(0,0)
    print(ans)
