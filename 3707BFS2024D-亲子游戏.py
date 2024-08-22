# 宝宝和妈妈参加亲子游戏，在一个二维矩阵（N*N）的格子地图上，宝宝和妈妈抽签决定各自的位置，地图上每个格子有不同的糖果数量，部分格子有障碍物。
#
# 游戏规则是妈妈必须在最短的时间（每个单位时间只能走一步）到达宝宝的位置，路上的所有糖果都可以拿走，不能走障碍物的格子，只能上下左右走。
#
# 请问妈妈在最短到达宝宝位置的时间内最多拿到多少糖果（优先考虑最短时间到达的情况下尽可能多拿糖果）。
#
# 输入
# 第一行输入为N（N <= 50），N标识二维矩阵的大小 之后N行，每行有N个值，表格矩阵每个位置的值
#
# 其中：
#
# -3：妈妈
#
# -2：宝宝
#
# -1：障碍
#
# >=0：糖果数(0表示没有糖果，但是可以走)
#
# 输出
# 输出妈妈在最短到达宝宝位置的时间内最多拿到多少糖果，行末无多余空格
# 样例输入 复制
# 4
# 3 2 1 -3
# 1 -1 1 1
# 1 1 -1 2
# -2 1 2 3
# 样例输出 复制
# 9
from collections import deque

# input
n = int(input())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

# 1. 找到妈妈和宝宝的位置
mama = []
baby = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == -3:
            mama = [i, j]
        if matrix[i][j] == -2:
            baby = [i, j]
# 2. 从妈妈的位置开始，用BFS遍历地图，找到最短路径
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[False for i in range(n)] for j in range(n)]
step = 0
flag = 0
q = deque()
q.append((mama[0], mama[1]))
visited[mama[0]][mama[1]] = True
while q:
    for _ in range(len(q)):
        i, j = q.popleft()
        if [i, j] == baby:
            flag = 1
            break
        for direction in DIRECTIONS:
            ni, nj = i + direction[0], j + direction[1]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and matrix[ni][nj] != -1:
                q.append((ni, nj))
                visited[ni][nj] = True
    if flag == 1:
        break
    step += 1
# 3. 在最短路径上，找到糖果
if flag == 0:
    print(-1)
else:
    dp = [[-1 for i in range(n)] for j in range(n)]
    q = deque()
    q.append((mama[0], mama[1]))
    dp[mama[0]][mama[1]] = 0
    while step >= 0:
        for _ in range(len(q)):
            i, j = q.popleft()
            for direction in DIRECTIONS:
                ni, nj = i + direction[0], j + direction[1]
                if 0 <= ni < n and 0 <= nj < n and matrix[ni][nj] != -1:
                    if dp[ni][nj] == -1:
                        q.append((ni, nj))
                    if [ni, nj] != baby:
                        dp[ni][nj] = max(dp[i][j] + matrix[ni][nj], dp[ni][nj])
                    else:
                        dp[ni][nj] = max(dp[ni][nj], dp[i][j])
        step -= 1

    # 4. 输出最多糖果
    print(dp[baby[0]][baby[1]])
