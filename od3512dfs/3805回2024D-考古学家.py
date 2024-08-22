# 有一个考古学家发现一个石碑，但是很可惜 发现时其已经断成多段，原地发现 N 个断口整齐的石碑碎片，为了破解石碑内容
#
# 考古学家希望有程序能帮忙计算复原后的石碑文字，你能帮忙吗
#
#
# 备注 如果存在石碑碎片内容完全相同，则由于碎片间的顺序不影响复原后的碑文内容。仅相同碎片间的位置变化不影响组合
#
# 输入
# 第一行输入 N，N 表示石碑碎片的个数
#
# 第二行依次输入石碑碎片上的文字内容 S 共有 N 组
#
# 输出
# 输出石碑文字的组合(按照升序排列)，行尾无多余空格
# 样例输入 复制
# 3
# a b ab
# 样例输出 复制
# aabb
# abab
# abba
# baab
# baba
# 来源/分类
# input
n = int(input())
s = input().split()
s.sort()
visited = [False] * n
path = []
ans_set = set()
ans = []


def dfs(s,  ans, visited, ans_set, path):
    if len(path) == len(s):
        ans_str = ''.join(path)
        if ans_str not in ans_set:
            ans.append(ans_str)
            ans_set.add(ans_str)
        return
    for i in range(len(s)):
        if visited[i] or (i > 0 and s[i] == s[i - 1] and not visited[i - 1]):
            continue
        visited[i] = True
        path.append(s[i])
        dfs(s,ans,visited,ans_set, path)
        path.pop()
        visited[i] = False


dfs(s, ans, visited, ans_set, path)
for res in ans:
    print(res)