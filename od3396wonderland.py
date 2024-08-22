# 3396: 【DP】2024D-Wonderland
# Wonderland是小王居住地一家很受欢迎的游乐园。 Wonderland目前有4种售票方式，分别为一日票（1天）、三日票（3天）、周票（7天）和月票（30天）。
# 每种售票方式的价格将由一个数组给出，每种票据在票面时限内可以无限制的进行游玩。
# 例如，小王在第10日买了一张三日票，小王可以在第10日、第11日和第12日进行无限制的游玩。 小王计划在接下来一年内多次游玩该游乐园。
# 小王计划的游玩日期将由一个数组给出。现在，请您根据给出的售票价格数组和小王计划游玩日期数组，返回完成游玩计划所需要的最低消费。
# 输入
# 输入为 2 个数组：
# 售票价格数组为 costs，costs.length = 4，默认顺序为一日票、三日票、周票和月票。
# 小王计划游玩日期数组为 days，1 ≤ days.length ≤ 365，1 ≤ days[i] ≤ 365，默认顺序为升序。
# 输出
# 完成游玩计划的最低消费。
# 样例输入 复制
# 1 2 7 25
# 1 4 6 7 8
# 样例输出 复制
# 4

# # 输入获取
# costs = list(map(int, input().split()))
# days = list(map(int, input().split()))
# # 算法入口
# def getResult():
#     # 最大游玩日
#     maxDay = days[-1]
#     # dp[i] 表示 前i天中完成其中所有游玩日需要的最少花费
#     dp = [0] * (maxDay + 1)  # dp[0] 默认为 0, 表示前0天花费0元
#     # index用于指向当前需要完成的游玩日days[index]
#     index = 0
#     # 遍历第1天~第maxDay天
#     for i in range(1, maxDay + 1):
#         if i == days[index]:
#             # 如果第i天是游玩日，那么此时有四种花费选择
#             #  选择买"一日票"，该花费仅用于第i天的游玩，那么此时前i天的花费就是 dp[i-1] + cost[0]
#             buy1 = dp[i - 1] + costs[0]
#             # 选择买"三日票"，该花费可用于第i天，第i-1天，第i-2天（相当于在第i-2天购买），那么此时前i天的花费就是 dp[i-3] + cost[1]
#             # 需要注意，如果 i < 3，那么dp[i-3]越界，此时前(i-3)天不存在,即花费为0
#             buy3 = (dp[i - 3] if i >= 3 else 0) + costs[1]
#             # 选择买“七日票”，该花费可用于第i天~第i-6天（相当于在第i-6天购买），那么此时前i天的花费就是 dp[i-7] + cost[2]
#             # 同上，注意i<7的处理
#             buy7 = (dp[i - 7] if i >= 7 else 0) + costs[2]
#             # 选择买“月票”，该花费可用于第i天~第i-29天（相当于在第i-29天购买），那么此时前i天的花费就是 dp[i-30] + cost[3]
#             # 同上，注意i<30的处理
#             buy30 = (dp[i - 30] if i >= 30 else 0) + costs[3]
#             # 最终dp[i]取上面四种花费的最小值
#             dp[i] = min(buy1, buy3, buy7, buy30)
#             # 匹配下一个游玩日（days是升序的，因此index 和 days[index] 正相关）
#             index += 1
#         else:
#             # 如果第i天不是游玩日，那么第i天不需要花费，即前i天的花费和前i-1天的花费一样
#             dp[i] = dp[i - 1]
#     return dp[maxDay]
#
#
# # 算法调用
# print(getResult())


costs = list(map(int, input().split()))
days = list(map(int, input().split()))

maxday = days[-1]
f = [0] * (maxday + 1)
idx = 0

for i in range(1, maxday + 1):
    if i == days[idx]:
        buy1 = (f[i - 1] if i >= 1 else 0) + costs[0]
        buy3 = (f[i - 3] if i >= 3 else 0) + costs[1]
        buy7 = (f[i - 7] if i >= 7 else 0) + costs[2]
        buy30 = (f[i - 30] if i >= 30 else 0) + costs[3]
        f[i] = min(buy1, buy3, buy7, buy30)
        idx += 1
    else:
        f[i] = f[i - 1]
print(f[-1])
