# 3515: 【DFS/BFS】2024D-聚餐地点
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：181
# 解决：87
# 题目描述
# 小华和小为是很好的朋友，他们约定周末一起吃饭，通过手机交流，他们在地图上选择了很多聚餐地点
#
# （由于自然地形等原因，部分聚餐地点不可达），求小华和小为都能达到的聚餐地点有多少个。
#
# 输入
# 第一行输入 m 和 n，m 表示地图长度，n 表示地图宽度
#
# 第二行开始具体输入地图信息，地图信息包括
#
# 0 为通畅的道路
#
# 1 为障碍物（且仅 1 为障碍物）
#
# 2 为小华或小为，地图中必定有且仅有两个（非障碍物）
#
# 3 为被选中的聚餐地点（非障碍物）
#
# 输出
# 可以两方都到达的聚餐地点的数量，行末无空格
# 样例输入 复制
# 4 4
# 2 1 0 3
# 0 1 2 1
# 0 3 0 0
# 0 0 0 0

# dfs
# n, m = map(int, input().split())
# grid = list()
# for _ in range(n):
#     grid.append(list(map(int, input().split())))


# dfs
import sys

sys.setrecursionlimit(10000)
from collections import deque

# n, m = map(int, input().split())
# grid = list()
# for _ in range(n):
#     grid.append(list(map(int, input().split())))
n, m = 2, 4
grid = [[2, 1, 0, 3], [0, 1, 2, 1]]


def findStart(grid, n, m):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                return i, j


dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
ans = 0
flag = False
x, y = findStart(grid, n, m)
used = [[False] * m for _ in range(n)]

# def dfs(grid, i, j, used):
#     global ans, flag
#     used[i][j] = True
#     for a, b in dir:
#         x, y = i + a, j + b
#         if not (0 <= x < n) or not (0 <= y < m) or used[x][y] == True or grid[x][y] == 1:
#             continue
#         if grid[x][y] == 2:
#             flag = True
#         if grid[x][y] == 3:
#             ans += 1
#         dfs(grid, x, y, used)

# dfs(grid, x, y, used)

q = deque()
q.append((x, y))
used[x][y] = 1
while len(q) > 0:
    i, j = q.popleft()
    for a, b in dir:
        x, y = i + a, j + b
        if not (0 <= x < n) or not (0 <= y < m) or used[x][y] == True or grid[x][y] == 1:
            continue
        q.append((x, y))
        used[x][y] = 1
        if grid[x][y] == 2:
            flag = True
        if grid[x][y] == 3:
            ans += 1

print(ans) if flag else print(0)
