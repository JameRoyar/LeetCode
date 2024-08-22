# 在一款虚拟游戏中生活，你必须进行投资以增强在虚拟游戏中的资产以免被淘汰出局。现有一家 Bank，它提供有若干理财产品 m，风险及投资回报不同，你有 N（元）进行投资，能接受的总风险值为 X。
#
# 你要在可接受范围内选择最优的投资方式获得最大回报。
#
# 说明：
#
# 1、在虚拟游戏中，每项投资风险值相加为总风险值；
#
# 2、在虚拟游戏中，最多只能投资 2 个理财产品；
#
# 3、在虚拟游戏中，最小单位为整数，不能拆分为小数； 投资额*回报率=投资回报
#
# 输入
# 第一行：产品数(取值范围[1, 20])，总投资额(整数，取值范围[1, 10000])，可接受的总风险(整数，取值范围[1, 200])
#
# 第二行：产品投资回报率序列，输入为整数，取值范围[1,60]
#
# 第三行：产品风险值序列，输入为整数，取值范围[1,100]
#
# 第四行：最大投资额度序列，输入为整数，取值范围[1,10000]
#
# 每个产品的投资额序列
# 样例输入 复制
# 5 100 10
# 10 20 30 40 50
# 3 4 5 6 10
# 20 30 20 40 30
# 样例输出 复制
# 0 30 0 40 0

n, total_invest, total_risk = map(int, input().split())
feedback = list(map(int, input().split()))
risk = list(map(int, input().split()))
max_invest = list(map(int, input().split()))

max_profit = 0
cur_profit = 0
invest = [[0, 0], [0, 0]]

for i in range(n):
    for j in range(i + 1, n):
        if risk[i] + risk[j] > total_risk:
            continue
        if max_invest[i] + max_invest[j] <= total_invest:
            i_amount = max_invest[i]
            j_amount = max_invest[j]
        else:
            if feedback[i] >= feedback[j]:
                i_amount = min(total_invest, max_invest[i])
                j_amount = total_invest - i_amount
            else:
                j_amount = min(total_invest, max_invest[j])
                i_amount = total_invest - j_amount
        cur_profit = i_amount * feedback[i] + j_amount * feedback[j]
        if cur_profit > max_profit:
            max_profit = cur_profit
            invest = [[i, i_amount], [j, j_amount]]

ans = [0] * n
ans[invest[0][0]] = invest[0][1]
ans[invest[1][0]] = invest[1][1]
print(" ".join(str(num) for num in ans))
