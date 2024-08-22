# 部门准备举办一场王者荣耀表演赛，有 10 名游戏爱好者参与，分为两队，每队 5 人。
#
# 每位参与者都有一个评分，代表着他的游戏水平。
#
# 为了表演赛尽可能精彩，我们需要把 10 名参赛者分为实力尽量相近的两队。
#
# 一队的实力可以表示为这一队 5 名队员的评分总和。
#
# 现在给你 10 名参与者的游戏水平评分，请你根据上述要求分队最后输出这两组的实力差绝对值。
#
# 例: 10 名参赛者的评分分别为 5 1 8 3 4 6 7 10 9 2，分组为 (1 3 5 8 10) (2 4 6 7 9)，两组实力差最小，差值为 1。
#
# 有多种分法，但实力差的绝对值最小为 1。
#
# 输入
# 10 个整数，表示 10 名参与者的游戏水平评分。范围在[1,10000]之间
# 输出
# 1 个整数，表示分组后两组实力差绝对值的最小值。
# 样例输入 复制
# 1 2 3 4 5 6 7 8 9 10
# 样例输出 复制
# 1
#input
numbers = list(map(int,input().split()))
numbers.sort()
total = sum(numbers)
target = total // 2
n = len(numbers)
ans = total
#dfs track the numbers until select five
def dfs(numbers,target,index,path,path_len):
    global ans
    if path > target:
        return
    if path_len == 5:
        ans = min(ans,abs(total-2*path))
        return
    for i in range(n):
        dfs(numbers,target,i+1,path+numbers[i],path_len+1)
dfs(numbers,target,0,0,0)
print(ans)