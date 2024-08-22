n = int(input())  # 输入披萨的数量
a = [int(input()) for i in range(n)]  # 输入每块披萨的美味值
dp = [[-1] * n for i in range(n)]  # 记忆化数组，用于存储已计算过的状态

def solve(L, R):
    # “馋嘴“选择一块披萨吃掉，对应端点移动
    if a[L] > a[R]:
        L = (L+1) % n
    else:
        R = (R+n-1) % n
    # 如果该状态已经计算过，则直接返回结果
    if dp[L][R] != -1:
        return dp[L][R]
    # 如果左右端点相同，则说明只剩下一块披萨，直接返回该披萨的美味值
    if L == R:
        dp[L][R] = a[L]
    else:
        # 分别计算选择左边披萨和选择右边披萨的情况下的最大美味值
        dp[L][R] = max(a[L] + solve((L+1)%n, R), a[R] + solve(L, (R+n-1)%n))
    return dp[L][R]

ans = 0
# 枚举吃货第一步取哪块披萨
for i in range(n):
    # 计算当前情况下吃货最多能吃到的披萨的美味值，并更新答案
    ans = max(ans, solve((i+1)%n, (i+n-1)%n) + a[i])

print(ans)  # 输出最多能吃到的披萨的美味值
