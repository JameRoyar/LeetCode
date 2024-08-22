# 527: 【模拟】2024D-结队编程
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：216
# 解决：99
# 题目描述
# 某部门计划通过结队编程来进行项目开发，已知该部门有 N 名员工，每个员工有独一无二的职级，每三个员工形成一个小组进行结队编程。
#
# 结队分组规则如下： 从部门中选出序号分别为i、j、k 的 3 名员工，他们的职级分别为 level[i], level[j], level[k]
#
# 结队小组需满足 level[i] < level[j] < level[k] 或者 level[i] > level[j] > level[k] ，其中 0 ⩽ i < j < k < n 请你按上述条件计算可能组合的小组数量。
#
# 同一员工可以参加多个小组。
#
# 输入
# 第一行输入：员工总数 n
#
# 第二行输入：按序号依次排列的员工的职级 level，中间用空格隔开
#
# 限制：
#
# 1 ⩽ n ⩽ 6000
#
# 1 ⩽ level[i] ⩽ 10^5
#
# 输出
# 可能组合的小组数量
# 样例输入 复制
# 4
# 1 2 3 4
# 样例输出 复制
# 4

n = int(input())
level = list(map(int, input().split()))

ans = 0

left_bigger = [0]*n
left_smaller = [0]*n
right_bigger = [0]*n
right_smaller = [0]*n

for j in range(1,n-1):
    for i in range(0,j):
        if level[i] < level[j]:
            left_bigger[j] += 1
        else:
            left_smaller[j] += 1
    for k in range(j+1,n):
        if level[k] < level[j]:
            right_bigger[j] += 1
        else:
            right_smaller[j] += 1

for j in range(1,n-1):
    ans += left_smaller[j]*right_bigger[j] + left_bigger[j]*right_smaller[j]

print(ans)