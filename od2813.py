# 某个产品当前迭代周期内有 N 个特性（F1, F2, ..., FN）需要进行覆盖测试，每个特性都被评估了对应的优先级，特性使用其 ID 作为下标进行标识。
#
# 设计了 M 个测试用例（T1, T2, ..., TN ），每个用例对应了一个覆盖特性的集合，测试用例使用其 ID 作为下标进行标识，测试用例的优先级定义为其覆盖的特性的优先级之和。
#
# 在开展测试之前，需要制定测试用例的执行顺序，规则为：优先级大的用例先执行，如果存在优先级相同的用例，用例 ID 小的先执行。
#
# 输入
# 第一行输入为 N 和 M ，N 表示特性的数量，M 表示测试用例的数量，0＜N<=100 ，0＜M<=100
#
# 之后 N 行表示特性 ID=1 到特性 ID=N 的优先级。
#
# 再接下来 M 行表示测试用例 ID=1 到测试用例 ID=M 关联的特性的 ID 的列表。
#
# 输出
# 按照执行顺序（优先级从大到小）输出测试用例的 ID，每行一个 ID。
#
# 测试用例覆盖的 ID 不重复。

#输入处理
m,n = map(int,input().split())
dic = {}
for i in range(1,m+1):
    dic[i] = int(input())

dic_ans = {}
for i in range(1,n+1):
    nums = list(map(int,input().split()))
    dic_ans[i] = sum(dic[num] for num in nums)

for dex in sorted(list(dic_ans.keys()),key = lambda x:(dic_ans[x]*-1,x)):
    print(dex)