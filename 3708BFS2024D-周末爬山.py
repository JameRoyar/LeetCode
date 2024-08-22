# 周末小明准备去爬山锻炼，0代表平地，山的高度使用1到9来表示，小明每次爬山或下山高度只能相差k及k以内，每次只能上下左右一个方向上移动一格，小明从左上角(0,0)位置出发
# 输入
# 第一行输入m n k(空格分隔)
#
# 代表 m*n 的二维山地图，k为小明每次爬山或下山高度差的最大值
#
# 然后接下来输入山地图，一共 m行n列，均以空格分隔。
#
# 取值范围：
#
# 0 < m ≤ 500
#
# 0 < n ≤ 500
#
# 0 < k < 5
#
# 输出
# 请问小明能爬到的最高峰多高，到该最高峰的最短步数，输出以空格分隔。
#
# 同高度的山峰输出较短步数。
#
# 如果没有可以爬的山峰，则高度和步数都返回0。
#
# 备注：所有用例输入均为正确格式，且在取值范围内，考生不需要考虑不合法的输入格式。
#
# 样例输入 复制
# 5 4 1
# 0 1 2 0
# 1 0 0 0
# 1 0 1 2
# 1 3 1 0
# 0 0 0 9
# 样例输出 复制
# 2 2
from collections import deque

# input
m, n, k = map(int, input().split())
mat = []
for i in range(m):
    mat.append(list(map(int, input().split())))

# bfs search the highest peak
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[False] * n for _ in range(m)]
step = 0
ans_step = 0
highest = mat[0][0]
q = deque()
q.append((0, 0))
visited[0][0] = True
while q:
    step += 1
    for _ in range(len(q)):
        x, y = q.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and abs(mat[x][y] - mat[nx][ny]) <= k:
                q.append((nx, ny))
                visited[nx][ny] = True
                if mat[nx][ny] > highest:
                    highest = mat[nx][ny]
                    ans_step = step

print(highest, ans_step)
