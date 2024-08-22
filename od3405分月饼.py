# 题目：【DP】2023C-分月饼
# 分值：200
# 作者：许老师-闭着眼睛学数理化
# 算法：DP
# 代码看不懂的地方，请直接在群上提问


# 输入员工人数m，月饼总数n
m, n = map(int, input().split())

# dp数组是一个大小为(m+1)*(n-m+2)*(n+1)的三维数组
# dp[i][j][k]表示，第i个数取值为j时，前i个数的总和为k的方法数
dp = [[[0] * (n+1) for j in range(n-m+2)] for i in range(m+1)]
# 第1个数字选了j，此时总和为j
# j的取值范围是[1, n//m]
# 因为m个数的和需要为n，那么最小那个数的最大值是n//m
for j in range(1, n//m+1):
    dp[1][j][j] = 1

# i的最大取值为m-1
for i in range(1, m):
    # j的最小取值为1，最大取值为n-m+1
    for j in range(1, n-m+2):
        # k的最小取值为i（前i个数都选了1，和为i），最大取值为n
        for k in range(i, n+1):
            # 增量d的取值范围为0，1，2，3
            for d in range(4):
                # 条件为j+d和k+j+d都没有超过对应的最大范围
                if j+d < n-m+2 and k+j+d < n+1:
                    dp[i+1][j+d][k+j+d] += dp[i][j][k]

ans = 0
# dp[m][j][n]表示第m个数（最后一个数）选了j后，总和为n的方法数
# 将所有的dp[m][j][n]加在一起即为答案
for j in range(n-m+2):
    ans += dp[m][j][n]

print(ans)
