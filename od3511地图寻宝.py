# 题目描述
# 小华按照地图去寻宝，地图上被划分成 m 行和 n 列的方格，横纵坐标范围分别是 [0, n-1] 和 [0, m-1]。
#
# 在横坐标和纵坐标的数位之和不大于 k 的方格中存在黄金（每个方格中仅存在一克黄金），但横坐标和纵坐标数位之和大于 k 的方格存在危险不可进入。
#
# 小华从入口 (0,0) 进入，任何时候只能向左，右，上，下四个方向移动一格。 请问小华最多能获得多少克黄金？
#
# 输入
# 坐标取值范围如下： 0 ≤ m ≤ 50，0 ≤ n ≤ 50
#
# k 的取值范围如下： 0 ≤ k ≤ 100
#
# 输入中包含 3 个字数，分别是 m, n, k
#
# 输出
# 输出小华最多能获得多少克黄金
# 样例输入 复制
# 40 40 18
# 样例输出 复制
# 1484

import sys

sys.setrecursionlimit(100000)
from collections import deque

# input
m, n, k = map(int, input().split())
# define destination
destination = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# calculate the sum of digits
def calculate_digits_sum(num):
    return sum(int(i) for i in str(num))


# build bit map
bit_map = [[0 for i in range(n)] for j in range(m)]
for i in range(m):
    for j in range(n):
        bit_map[i][j] = calculate_digits_sum(i) + calculate_digits_sum(j)
ans = 0
path = [[0 for i in range(n)] for j in range(m)]


def dfs(i, j, path, bit_map):
    global ans
    path[i][j] = 1
    ans += 1
    for x, y in destination:
        i_new = i + x
        j_new = j + y
        if 0<=i_new<m and 0<=j_new<n and path[i_new][j_new]==0 and bit_map[i_new][j_new]<=k:
            dfs(i_new, j_new, path, bit_map)


# dfs(0, 0, path, bit_map)
# print(ans)

q = deque()
q.append((0, 0))
path[0][0]=1

def bfs(q, path, bit_map):
    while q:
        global ans
        i, j = q.popleft()
        ans += 1
        for x, y in destination:
            i_new, j_new = i + x, j + y
            if 0<=i_new<m and 0<=j_new<n and path[i_new][j_new]==0 and bit_map[i_new][j_new]<=k:
                q.append((i_new, j_new))
                path[i_new][j_new] = 1


bfs(q, path, bit_map)
print(ans)
