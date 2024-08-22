# 2529: 【模拟】2023C-螺旋数字矩阵
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：191
# 解决：87
# 题目描述
# 疫情期间，小明隔离在家，百无聊赖，在纸上写数字玩。
#
# 他发明了一种写法：给出数字个数n和行数m (0 < n < 999，0 < m < 999)，从左上角的1开始，按照顺时针螺旋向内写方式，依次写出2, 3, ..., n，最终形成一个m行矩阵。
#
# 小明对这个矩阵有些要求：
#
# 1. 每行数字的个数一样多
#
# 2. 列的数量尽可能少
#
# 3. 填充数字时优先填充外部
#
# 4. 数字不够时，使用单个*号占位
#
# 输入
# 两个整数，空格隔开，依次表示n、m
# 输出
# 符合要求的唯一短阵
# 样例输入 复制
# 9 4
# 样例输出 复制
# 1 2 3
# * * 4
# 9 * 5
# 8 7 6

from math import ceil

# 递归函数
# ans为答案螺旋矩阵
# start_i, end_i, start_j, end_j分别为子矩阵的起始、终止的i和j下标
# cur_num为未填充子矩阵左上角的第一个数
# n为终止数字
def help(ans, start_i, end_i, start_j, end_j, cur_num, n):
    # 如果不存在遍历区间，则不会进入下面四个for循环中的任意一个
    # 会持续进行递归，导致编译栈溢出
    # 这种情况就是当n为某个奇数的平方且c = m = sqrt(n)的时候会出现
    # 譬如填充5*5的矩阵且n = 25，最中间那个数字会出现的情况
    # 额外判断这种条件，将最中间的数字填充上并退出递归即可
    if start_i == end_i and start_j == end_j:
        ans[start_i][start_j] = cur_num
        return
    # 未填充矩阵的上边界：从左往右，固定start_i，正序遍历j
    for j in range(start_j, end_j):
        ans[start_i][j] = str(cur_num)
        cur_num += 1
        if cur_num > n: return
    # 未填充矩阵的右边界：从上往下，固定end_j，正序遍历i
    for i in range(start_i, end_i):
        ans[i][end_j] = str(cur_num)
        cur_num += 1
        if cur_num > n: return
    # 未填充矩阵的下边界：从右往左，固定end_i，逆序遍历j
    for j in range(end_j, start_j, -1):
        ans[end_i][j] = str(cur_num)
        cur_num += 1
        if cur_num > n: return
    # 未填充矩阵的做边界：从下往上，固定start_j，逆序遍历j
    for i in range(end_i, start_i, -1):
        ans[i][start_j] = str(cur_num)
        cur_num += 1
        if cur_num > n: return
    # 对未填充数组进行递归
    # start_i, end_i, start_j, end_j需要修改
    help(ans, start_i+1, end_i-1, start_j+1, end_j-1, cur_num, n)

# 输入数字n，行数m
n, m = map(int, input().split())
# 计算列数c，n除以m后向上取整
c = ceil(n / m)

# 初始化答案螺旋数组，先用"*"填充
ans = [["*"] * c for _ in range(m)]

# 递归入口：start_i, end_i, start_j, end_j
# 分别传入0, m-1, 0, c-1
help(ans, 0, m-1, 0, c-1, 1, n)
# 逐行输出螺旋矩阵
for row in ans:
    print(*row)