# 小明和朋友玩跳格子游戏，有
# n
# 个连续格子组成的圆圈，每个格子有不同的分数，小朋友可以选择从任意格子起跳，但是不能跳连续的格子，不能回头跳，也不能超过一圈；
#
#
# 给定一个代表每个格子得分的非负整数数组，计算能够得到的最高分数。
#
# 输入
#
# 给定一个数例，第一个格子和最后一个格子首尾相连，如： 2
# 3
# 2。
#
# 输出
# 输出能够得到的最高分，如： 3。
# 样例输入
# 复制
# 2
# 3
# 2
# 样例输出
# 复制
# 3
nums = list(map(int, input().split()))
n = len(nums)
dp = [0] * n
dp[0] = nums[0]
dp[1] = nums[0] + nums[1]


def rob(nums):
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[n - 1]


nums1 = nums[1:]
nums2 = nums[:-1]
print(max(rob(nums1), rob(nums2)))
