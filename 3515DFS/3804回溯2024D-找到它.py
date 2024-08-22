# 题目描述
# 找到它是个小游戏，你需要在一个矩阵中找到给定的单词
#
# 假设给定单词HELLOWORLD，在矩阵中只要能找HELLOWORLD就算通过
#
# 注意区分英文字母大小写，并且你只能上下左右行走，不能走回头路
#
# 输入
# 输入第一行包含两个整数N M (0 < N, M < 21)
#
# 分别表示N行M列的矩阵
#
# 第二行是长度不超过100的单词W
#
# 在整个矩阵中给定单词W只会出现一次
#
# 从第3行到第N+2是只包含大小写英文字母的长度为M的字符串矩阵
#
# 输出
# 如果能在矩阵中连成给定的单词，则输出给定单词首字母在矩阵中的位置为第几行第几列
#
# 否则输出 NO
#
# 样例输入 复制
# 5 5
# HELLOWORLD
# CPUCY
# EKLQH
# CHELL
# LROWO
# DGRBC
# 样例输出 复制
# 3 2
# 状态更新和回滚写在横向遍历for循环内的回溯写法
# 我们需要思考的是，对于这种二维网格如何进行回溯？换句话说，如何构建回溯函数？
#
# 在回溯过程中我们需要知道以下信息：
#
# 当前进行到了单词中的哪一个字符？
#
# 当前在网格中搜索到了哪一个位置？
#
# 由于网格中的字符不能重复使用，那么哪一些字符是已经使用过的？
#
# 是否已经在网格中找到了这个单词？
#
# 对于第一点，我们的回溯函数中需要存在参数word_idx，来表示待搜索的单词此时遍历到的索引位置。
#
# 对于第二点，我们的回溯函数需要传入当前搜索的点的位置(x, y)
#
# 对于第三点，这个在二维网格类型的搜索问题中是非常常用的技巧，即构建一个大小和grid一样的check_list
#
# 对于第四点，我们可以直接声明一个全局变量isFind来表示是否已经找到该单词
#
# 除了这些参数之外，我们还需要传入二维矩阵grid本身，它的大小N和M等等。

# inut
n, m = map(int, input().split())
word = input()
grid = []
for i in range(n):
    grid.append(input())

# bfs traverse and backtrace
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[False for i in range(m)] for j in range(n)]
isFind = False


def backtrack(x, y, idx, grid, visited):
    global isFind
    if idx == len(word) - 1:
        isFind = True
        return
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == word[idx + 1]:
            visited[nx][ny] = True
            backtrack(nx, ny, idx + 1, grid, visited)
            visited[nx][ny] = False


for i in range(n):
    for j in range(m):
        if grid[i][j] == word[0]:
            visited[i][j] = True
            backtrack(i, j, 0, grid, visited)
            visited[i][j] = False
            if isFind:
                print(f"{i + 1} {j + 1}")
                break
    if isFind:
        break

if not isFind:
    print("NO")
