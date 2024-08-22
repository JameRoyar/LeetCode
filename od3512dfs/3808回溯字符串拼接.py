# 给定M (0<M<=30)个字符(a-z)，从中取出任意字符(每个字符只能用一次)拼接成长度为N (0<N<=5)的字符串，要求相同的字符不能相邻，计算出给定的字符列表能拼接出多少种满足条件的字符串，输入非法或者无法拼接出满足条件的字符串则返回0。
# 输入
# 给定的字符列表和结果字符串长度，中间使用空格(" ")拼接
# 输出
# 满足条件的字符串个数
# 样例输入 复制
# aabc 3
# 样例输出 复制
# 8
# 提示
# 给定的字符为aabc，结果字符串长度为3，可以拼接成abc,acb,bac,bca,cba,cab,aba,aca，共8种
'''
# input
strs, n = input().split()
n = int(n)
visited = [False] * len(strs)
ans = 0
res = []


def dfs(strs, n, visited, idx, path, res):
    global ans
    if len(path) == n:
        res.append(path)
        ans += 1
        return
    for i in range(len(strs)):
        if visited[i] or (path and strs[i] == path[-1]):
            continue
        if i > 0 and strs[i] == strs[i - 1] and not visited[i - 1]:
            continue
        visited[i] = True
        path += strs[i]
        dfs(strs, n, visited, i + 1, path, res)
        # new_string = original_string.replace(char_to_remove, "")
        path = path[:-1]
        visited[i] = False


try:
    if not all("a" <= c <= "z" for c in strs) or n > len(strs):
        print(0)
    else:
        dfs(strs, n, visited, 0, "", res)
        print(ans)
        print(res)
        res = set(res)
        res = list(res)
        print(res)
        print(len(res))
except:
    print(0)
'''
strs, n = input().split()
strs = sorted(list(strs))
n = int(n)
visited = [False] * len(strs)
ans = 0
path = []
res = []


def dfs(strs, n, visited, idx, path, res):
    if len(path) == n:
        global ans
        res.append(path[:])
        ans += 1
        return
    for i in range(len(strs)):
        if visited[i] or (path and strs[i] == path[-1]):
            continue
        if i > 0 and strs[i] == strs[i - 1] and not visited[i - 1]:
            continue
        visited[i] = True
        path.append(strs[i])
        dfs(strs, n, visited, i + 1, path, res)
        # new_string = original_string.replace(char_to_remove, "")
        path.pop()
        visited[i] = False


try:
    if not all("a" <= c <= "z" for c in strs) or n > len(strs):
        print(0)
    else:
        dfs(strs, n, visited, 0, path, res)
        print(res)
        print(ans)
except:
    print(0)

# # 从输入中读取字符串 s 和整数 k
# s, k = input().split()
# s = list(s)
# s.sort()  # 将字符串按照字典序排序，方便后续去重操作
# k = int(k)
# ans = 0
# n = len(s)
# vis = [False] * n  # 用于标记当前字符是否被选取
# v = []  # 存储对应的字符串序列
#
# # 定义深度优先搜索函数
# def dfs(u):
#     if u == k:
#         global ans
#         ans += 1
#         return
#     for i in range(n):
#         # 如果当前字符已经被使用过，或者与上一个字符一样（但上一个字符未被使用），则跳过
#         if vis[i] or (i > 0 and s[i] == s[i - 1] and not vis[i - 1]):
#             continue
#         # 如果相邻字符相同，则跳过
#         if len(v) and v[-1] == s[i]:
#             continue
#         # 将当前字符添加到序列中，更新标记，并进行递归
#         v.append(s[i])
#         vis[i] = True
#         dfs(u + 1)
#         # 回溯操作，将当前字符弹出序列，还原标记
#         v.pop()
#         vis[i] = False
#
# # 从起始状态开始深度优先搜索
# dfs(0)
# print(ans)
