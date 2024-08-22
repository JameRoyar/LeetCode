# 输入 m 和 n 两个数，m 和 n 表示一个 m*n 的棋盘。输入棋盘内的数据。棋盘中存在数字和"."两种字符，如果是数字表示该位置是一匹马，如果是"."表示该位置为空的，棋盘内的数字表示为该马能走的最大步数。
#
# 例如棋盘内某个位置一个数字为 k，表示该马只能移动 1~k 步的距离。
#
# 棋盘内的马移动类似于中国象棋中的马移动，先在水平或者垂直方向上移动一格，然后再将其移动到对角线位置。
#
# 棋盘内的马可以移动到同一个位置，同一个位置可以有多匹马。
#
# 请问能否将棋盘上所有的马移动到同一个位置，若可以请输入移动的最小步数。若不可以输出 0。
#
# 输入
# 输入m 和 n 两个数，m 和 n 表示一个 m*n 的棋盘。输入棋盘内的数据。
# 输出
# 能否将棋盘上所有的马移动到同一个位置，若可以请输入移动的最小步数。若不可以输出 0。
# 样例输入 复制
# 3 5
# 4 7 . 4 8
# 4 7 4 4 .
# 7 . . . .
# 样例输出 复制
# 17
from collections import deque
from math import inf

# input
m, n = map(int, input().split())
chess = []
for i in range(m):
    chess.append(list(input().split()))

ans = inf
DIRECTIONS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]


# for a horse in map calculate the mat which contain per step it can visit
def bfs(i, j, m, n, step):
    map = [[-1] * n for _ in range(m)]
    q = deque()
    q.append((i, j))
    level = 0
    map[i][j] = level
    while q:
        level += 1
        if level > step:
            break
        for _ in range(len(q)):
            new_i,new_j = q.popleft()
            for direction in DIRECTIONS:
                x, y = direction
                x += new_i
                y += new_j
                if 0 <= x < m and 0 <= y < n and map[x][y] == -1:
                    map[x][y] = level
                    q.append((x, y))
    return map


# for every horse calculate its map and merge them
def mergeMaps(chess):
    ans_map = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if chess[i][j] != ".":
                map = bfs(i, j, m, n, int(chess[i][j]))
                for x in range(m):
                    for y in range(n):
                        if map[x][y] == -1 or ans_map[x][y] == -1:
                            ans_map[x][y] = -1
                        if map[x][y] != -1 and ans_map[x][y] != -1:
                            ans_map[x][y] += map[x][y]
    return ans_map


# find the mini step
def findAns(ans_map):
    global ans
    for i in range(m):
        for j in range(n):
            if ans_map[i][j] != -1 and ans_map[i][j] < ans:
                ans = ans_map[i][j]


ans_map = mergeMaps(chess)
findAns(ans_map)
print(ans)
