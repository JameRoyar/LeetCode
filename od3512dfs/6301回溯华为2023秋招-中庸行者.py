# 6301: 【回溯】华为2023秋招-中庸行者
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：145
# 解决：54
# 题目描述
# 给定一个m*n的整数阵作为地图，短阵数值为地形高度；
#
# 中庸行者选择地图中的任意一点作为起点，尝试往上、下、左、右四个相邻格子移动;
#
# 移动时有如下约束：
#
# 中庸行者只能上坡或者下坡，不能走到高度相同的点。
#
# 不允许连续上坡或者连续下坡，需要交替进行;
#
# 每个位置只能经过一次，不能重复行走；
#
# 请给出中庸行者在本地图内，能连续移动的最大次数。
#
# 输入
# 第一行两个数字，分别为行数和每行的列数
#
# 后续数据为矩阵地图内容
#
# 矩阵边长范围：[1,8]
#
# 地形高度范围：[0,100000]
#
# 输出
# 一个整数，代表中庸行者在本地图内，能连续移动的最大次数。
# 样例输入 复制
# 2 2
# 1 2
# 4 3
# 样例输出 复制
# 3
# 提示
# 3->4->1->2，一共移动3次。

# input
m, n = map(int, input().split())
mat = []
for i in range(m):
    mat.append(list(map(int, input().split())))

DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]
visited = [[False for _ in range(n)] for _ in range(m)]
flag = True
ans = 0


# track the mat
def dfs(i, j, mat, step, flag):
    global ans
    ans = max(ans, step)
    for dx, dy in DIR:
        x, y = i + dx, j + dy
        if 0 <= x < m and 0 <= y < n and (
                (mat[x][y] > mat[i][j] and flag) or (mat[x][y] < mat[i][j] and not flag)) and not visited[x][y]:
            visited[x][y] = True
            dfs(x, y, mat, step + 1, not flag)
            visited[x][y] = False


for i in range(m):
    for j in range(n):
        visited[i][j] = True
        dfs(i, j, mat, 0, True)
        visited[i][j] = False
        visited[i][j] = True
        dfs(i, j, mat, 0, False)
        visited[i][j] = False

print(ans)
