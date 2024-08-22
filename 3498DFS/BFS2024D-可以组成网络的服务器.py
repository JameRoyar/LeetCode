# 在一个机房中，服务器的位置标识在 n*m 的整数矩阵网格中，1表示单元格上有服务器，0 表示没有。如果两台服务器位于同一行或者同一列中紧邻的位置，则认为它们之间可以组成一个局域网。请你统计机房中最大的局域网包含的服务器个数。
# 输入
# 第一行输入两个正整数，n和m，0 < n,m <= 100
#
# 之后为n*m的二维数组，代表服务器信息
#
# 输出
# 最大局域网包含的服务器个数。
# 样例输入 复制
# 2 2
# 1 0
# 1 1
# 样例输出 复制
# 3
# 提示
# [0][0]、[1][0]、[1][1]三台服务器相互连接，可以组成局域网

# build networks
n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

path = [[False] * m for i in range(n)]
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dfs(i, j, path):
    count = 1
    path[i][j] = True
    for x, y in directions:
        new_i, new_j = i + x, j + y
        if 0 <= new_i < n and 0 <= new_j < m and not path[new_i][new_j] and grid[new_i][new_j] == 1:
            count += dfs(new_i, new_j, path)
    return count


#bfs
def bfs(i, j, path):
    queue = [(i, j)]
    path[i][j] = True
    count = 1
    while queue:
        x, y = queue.pop(0)
        for x, y in directions:
            new_i, new_j = x + y, y + x
            if 0 <= new_i < n and 0 <= new_j < m and not path[new_i][new_j] and grid[new_i][new_j] == 1:
                queue.append((new_i, new_j))
                path[new_i][new_j] = True
                count += 1
    return count

max_count = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not path[i][j]:
            max_count = max(max_count, bfs(i, j, path))

print(max_count)
