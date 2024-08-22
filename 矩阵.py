# 题目描述:
# 给定一个矩阵,包含N*M个整数,和一个包含K个整数的数组。
# 现在要求在这个矩阵中找一个宽度最小的子矩阵,要求子矩阵包含数组中所有的整数。
# 输入描述:
# 第一行输入两个正整数N,M,表示矩阵大小。
# 接下来N行M列表示矩阵内容。
# 下一行包含一个正整数K。
# 下一行包含K个整数,表示所需包含的数组,K个整数可能存在重复数字
# 所有输入数据小于1000。
# 输出描述:
# 输出包含一个整数,表示满足要求子矩阵的最小宽度,若找不到,输出-1.
# 补充说明:
# 示例1
# 输入:
# 25
# 12231
# 23232
# 3
# 123
# 输出:
# 2
# 说明:
# 矩阵第0、3列包含了1、2、3,矩阵第3、4列包含了1、2、3
# 示例2
# 输入:
# 25
# 12231
# 13234
# 3
# 114
# 输出:
# 5
# 说明:
# 矩阵第1、2、3、4、5列包含了1、1、4

def solve():
    n, m = map(int, input().split())  # 读取矩阵的行数n和列数m
    mp = []  # 用于存储矩阵的列表
    for _ in range(n):
        mp.append(list(map(int, input().split())))  # 逐行读取矩阵数据

    now, ask = {}, {}  # now用于记录当前统计的元素数量，ask用于记录所需元素的数量
    k = int(input())  # 读取数组中元素的数量
    for x in map(int, input().split()):
        ask[x] = ask.get(x, 0) + 1  # 读取并记录需要包含的每个元素的数量

    r, ans = 0, int(1e9)  # 初始化右指针r和最小宽度ans
    for l in range(m):  # 遍历每一列作为子矩阵的左边界
        while True:
            if ck(now, ask):
                break  # 当前窗口已包含所有所需元素时，停止扩张右边界
            if r == m:
                break  # 如果右边界已达到最右列，停止循环
            for j in range(n):
                now[mp[j][r]] = now.get(mp[j][r], 0) + 1  # 更新右边界列中元素的数量
            r += 1  # 右边界向右移动

        if not ck(now, ask):
            break  # 如果当前窗口不满足条件，则终止循环
        ans = min(ans, r - l)  # 更新最小宽度

        for j in range(n):
            now[mp[j][l]] -= 1  # 左边界向右移动，更新窗口内元素数量

    if ans == int(1e9):
        ans = -1  # 如果未找到合适的子矩阵，返回-1
    print(ans)  # 输出最小宽度


def ck(now, ask):
    for val, num in ask.items():
        if now.get(val, 0) < num:
            return False  # 如果当前元素数量少于所需数量，返回False
    return True  # 否则返回True，表示当前窗口满足所有条件


if __name__ == '__main__':
    solve()