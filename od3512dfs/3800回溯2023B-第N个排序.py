# 给定参数
# n ，从
# 1
# 到
# n
# 会有
# n
# 个整数
# 1，2，3，...，n。
#
# 这
# n
# 个数字共有n!种排列，按大小顺序升序列出所有排列情况，并一一标记。
#
# 当
# n = 3
# 时，所有排列如下："123", "132", "213", "231", "312", "321"。
#
# 给定
# n
# 和
# k
# 返回第
# k个排列。
#
# 输入
#
# 第一行为
# n
# 第二行为
# k
#
# n
# 的范围是
# 1
# ~ 9
#
# k
# 的范围是
# 1
# ~ n!
#
#
# 输出
# 输出排列第
# k
# 位置的数字
# 样例输入
# 复制
# 3
# 3
# 样例输出
# 复制
# 213
# 213
m = int(input())
k = int(input())
nums = [i for i in range(1, m + 1)]
n = len(nums)
ans = []
path = []
visited = [False for i in range(n)]


def dfs(i):
    if i == n:
        ans.append(path[:])
        return
    for j in range(n):
        if not visited[j]:
            visited[j] = True
            path.append(nums[j])
            dfs(i + 1)
            path.pop()
            visited[j] = False


dfs(0)
ans.sort()
print("".join(str(i) for i in ans[k - 1]))
