# 有一种特殊的加密算法，明文为一段数字串，经过密码本查找转换，生成另一段密文数字串。规则如下
#
# 1. 明文为一段数字串由0-9组成
#
# 2. 密码本为数字0-9组成的二维数组
#
# 3. 需要按明文串的数字顺序在密码本里找到同样的数字串，密码本里的数字串是由相邻的单元格数字组成，上下和左右是相邻的，注意:对角线不相邻，同一个单元格的数字不能重复使用。
#
# 4. 每一位明文对应密文即为密码本中找到的单元格所在的行和列序号(序号从0开始)组成的两个数字。如明文第i位Data[i]对应密码本单元格为Book[X][Y]，则明文第i位对应的密文为X Y，X和Y之间用空格隔开。
#
# 如果有多条密文，返回字符序最小的密文。如果密码本无法匹配，返回"error". 请你设计这个加密程序。
# 第一行输入1个正整数N，代表明文的长度(1 <= N <= 9)
#
# 第二行输入N个明文数字组成的序列Data[i](整数，0 <= Data[i] <= 9)
#
# 第三行输入1个正整数M，(1 <= M <= 9)
#
# 接下来输入一个M*M的矩阵代表密码本Book[i][i]，(整数，0 <= Book[i][i] <= 9)
#
# 输出
# 如明文 第i位Data[i]对应密码本单元格为Book[i][j]，则明文第i位对应的密文为X Y，X和Y之间用空格隔开。如果有多条密文，返回字符序最小的密文。如果密码本无法匹配，返回"error"。
# 样例输入 复制
# 4
# 0 0 2 4
# 4
# 0 0 2 4
# 1 3 4 6
# 3 4 1 5
# 6 6 6 5
# 样例输出 复制
# 0 0 0 1 0 2 0 3
DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# input
n = int(input())
code = list(map(int, input().split()))
m = int(input())
book = []
for i in range(m):
    book.append(list(map(int, input().split())))
ans = []
path = []
visited = [[False] * m for i in range(m)]


def dfs(code, index, path, visited, ans):
    if index == len(code):
        # ans.append("".join(map(str, path))
        ans.append(path[:])
        return
    for direction in DIR:
        x, y = path[-1][0] + direction[0], path[-1][1] + direction[1]
        if 0 <= x < m and 0 <= y < m and not visited[x][y] and book[x][y] == code[index]:
            path.append([x, y])
            visited[x][y] = True
            dfs(code, index + 1, path, visited, ans)
            path.pop()
            visited[x][y] = False


for i in range(m):
    for j in range(m):
        if book[i][j] == code[0]:
            path.append([i, j])
            visited[i][j] = True
            dfs(code, 1, path, visited, ans)
            path.pop()
            visited[i][j] = False

if len(ans) == 0:
    print("error")
else:
    res = []
    for i in range(len(ans)):
        new_list = []
        for j in range(len(ans[i])):
            new_list+=ans[i][j]
            res.append(new_list)
    res.sort()
    print(" ".join(str(i) for i in res[0]))
