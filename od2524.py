# 2524: 【模拟】2023C-API 集群负载统计
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：181
# 解决：123
# 题目描述
# 某个产品的 RESTful API 集合部署在服务器集群的多个节点上，近期对客户端访问日志进行了采集，需要统计各个 API 的访问频次，根据热点信息在服务器节点之间做负载均衡，现在需要实现热点信息统计查询功能。
#
# RESTful API 的由多个层级构成，层级之间使用/连接，如/A/B/C/D这个地址，A 属于第一级，B 属于第二级，C 属于第三级，D 属于第四级。
#
# 现在负载均衡模块需要知道给定层级上某个名字出现的频次，未出现过用 0 次表示，实现这个功能。
#
# 输入
# 第一行为 N，表示访问历史日志的条数，0<N<=100。
# 接下来 N 行，每一行为一个 RESTful API 的 URL 地址，约束地址中仅包含英文字母和连接符/，最大层级为 10，每层级字符串最大长度为 10。
# 最后一行为层级 L 和要查询的关键字。
# 输出
# 输出给定层级上，关键字出现的频次，使用完全匹配方式（大小写敏感）。
# 样例输入 复制
# 5
# /huawei/computing/no/one
# /huawei/computing
# /huawei
# /huawei/cloud/no/one
# /huawei/wireless/no/one
# 2 computing
# 样例输出 复制
# 2
# 提示
# 在第二层级上，computing 出现了 2 次，因此输出 2.

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(input().split("/")))
tmp = list(input().split())
m = int(tmp[0])
aim = tmp[1]

#solution
ans = 0
for i in range(n):
    if len(lst[i]) < m+1:
        continue
    elif lst[i][m] == aim:
        ans += 1
print(ans)
