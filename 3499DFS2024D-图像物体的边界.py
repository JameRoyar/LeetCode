# 给定一个二维数组M行N列，二维数组里的数字代表图片的像素，为了简化问题，仅包含像素1和5两种像素，每种像素代表一个物体，2个物体相邻的格子为边界，求像素1代表的物体的边界个数。像素1代表的物体的边界指与像素5相邻的像素1的格子，边界相邻的属于同一个边界，相邻需要考虑8个方向(上，下，左，右，左上，左下，右上，右下)
# 其他约束:
# 地图规格约束为:
# 0<M<100
# 0<N<100
#
# 1 如下图，与像素5的格子相邻的像素1的格子(0,0)、(0,1)、(0,2)、(1,0)、(1,2)、(2,0)、(2,1)、(2,2)、(4,4)、(4,5)、(5,4)为边界，另(0,0)、(0,1)、(0,2)、(1,0)、(1,2)、(2,0)、(2,1)、(2,2)相邻，为1个边界，(4,4)、(4,5)、(5,4)相邻，为1个边界，所以下图边界个数为2。
#
#
#
# 2 如下图，与像素5的格子相邻的像素1的格子(0,0)、(0,1)、(0,2)、(1,0)、(1,2)、(2,0)、(2,1)、(2,2)、(3,3)、(3,4)、(3,5)、(4,3)、(4,5)、(5,3)、(5,4)、(5,5)为边界，另这些边界相邻，所以下图边界个数为1。注：(2,2)、(3,3)相邻
#
#
#
# 输入
# 第一行，行数M，列数N
#
# 第二行开始，是M行N列的像素的二维数组，仅包含像素1和5
#
# 输出
# 像素1代表的物体的边界个数。如果没有边界输出0（比如只存在像素1，或者只存在像素5）

# input
m, n = map(int, input().split())
Map = []
for i in range(m):
    Map.append(list(map(int, input().split())))
DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
ans = 0
# handle the 5 surround to 3
for  i in range(m):
     for j in range(n):
         if Map[i][j] == 5:
              for direction in DIRECTIONS:
                  x, y = i + direction[0], j + direction[1]
                  if 0 <= x < m and 0 <= y < n and Map[x][y] == 1:
                     Map[x][y] = 3

visited = [[False]*n for _ in range(m)]
def dfs(i,j,m,n,Map,visited):
    visited[i][j] = True
    for direction in DIRECTIONS:
        x, y = i + direction[0], j + direction[1]
        if 0 <= x < m and 0 <= y < n and Map[x][y] == 3 and not visited[x][y]:
            dfs(x,y,m,n,Map,visited)

# handle the 1 surround to 1
for i in range(m):
    for j in range(n):
        if Map[i][j] == 3 and not visited[i][j]:
            dfs(i,j,m,n,Map,visited)
            ans+=1

print(ans)
