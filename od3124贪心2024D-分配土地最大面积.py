# 3124: 【贪心】2024D-分配土地最大面积
# 内存限制：128 MB
# 时间限制：4.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：322
# 解决：135
# 题目描述
# 从前有个村庄，村民们喜欢在各种田地上插上小旗子，旗子上标识了各种不同的数字。某天集体村民决定将覆盖相同数字的最小矩阵形的土地的分配给为村里做出巨大贡献的村民，请问，此次分配土地，做出贡献的村民中最大会分配多大面积?
#
#
# 备注：旗子上的数字为 1-500，土地边长不超过 500
#
# 未插旗子的土地用 0 标识
#
# 输入
# 第一行输入 m 和 n，m 代表村子的土地的长，n 代表土地的宽 第二行开始输入地图上的具体标识
# 输出
# 输出需要分配的土地面积，即包含相同数字旗子的最小矩阵中的最大面积。
# 样例输入 复制
# 3 3
# 1 0 1
# 0 0 0
# 0 1 0
# 样例输出 复制
# 9
# 提示
# 土地上的旗子为 1，其坐标分别为(0,0)，(2,1)以及(0,2)，为了覆盖所有旗子，矩阵需要覆盖的横坐标为 0 和 2，纵坐标为 0 和 2，所以面积为 9，即(2-0+1)*(2-0+1)=9。
from collections import defaultdict
from math import inf


# 输入二维矩阵的长、宽
m, n = map(int, input().split())
grid = list()
# 循环m行，每次输入长度为n的一维数组
for _ in range(m):
    grid.append(list(map(int, input().split())))

# 构建哈希表dic，其中
# key为表示某种颜色的数字
# value为该种颜色对应的长度为4最值列表[top, bottom, left, right]
# 初始化top和left为正无穷（或者500，因为边长最大为500），
# 初始化，bottom和right为负无穷（或者-1）
dic = defaultdict(lambda : [inf, -inf, inf, -inf])

# 遍历整个二维矩阵grid
for x in range(m):
    for y in range(n):
        # 获得该种颜色
        color = grid[x][y]
        # 如果没有插旗子，则直接跳过
        if color == 0:
            continue
        # 考虑上下方向
        # 如果比最上边的点更靠上，更新top，即dic[color][0]
        if x < dic[color][0]:
            dic[color][0] = x
        # 如果比最下边的点更靠下，更新bottom，即dic[color][1]
        if x > dic[color][1]:
            dic[color][1] = x
        # 考虑左右方向
        # 如果比最左边的点更靠左，更新left，即dic[color][2]
        if y < dic[color][2]:
            dic[color][2] = y
        # 如果比最右边的点更靠右，更新right，即dic[color][3]
        if y > dic[color][3]:
            dic[color][3] = y

# 计算所有颜色中，最小覆盖面积的最大值
print(max((r-l+1)*(b-t+1) for t, b, l, r in dic.values()))