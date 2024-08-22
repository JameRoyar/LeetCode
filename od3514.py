# 3514: 【DFS/BFS】2024D-寻找最富裕的小家庭
# 在一棵树中，每个节点代表一个家庭成员，节点的数字表示其个人的财富值，一个节点及其直接相连的子节点被定义为一个小家庭。
#
# 现给你一棵树，请计算出最富裕的小家庭的财富和。
#
# 输入
# 第一行为一个数N，表示成员总数，成员编号1-N，1<=N<=1000
#
# 第二行为N个空格分隔的数，表示编号1-N的成员的财富值，0<=财富值<=1000000
#
# 接下来N-1行，每行两个空格分隔的整数(N1,N2)，表示N1是N2的父节点。
#
# 输出
# 最富裕的小家庭的财富和
# 样例输入 复制
# 4
# 100 200 300 500
# 1 2
# 1 3
# 2 4
# 样例输出 复制
# 700

# 导入所需模块
import sys
from collections import defaultdict


def main():
    input = sys.stdin.read  # 从标准输入读取所有输入
    data = input().split()  # 将输入按空格拆分成列表
    index = 0

    N = int(data[index])  # 读取成员总数
    index += 1

    # 用于存储每个成员的财富值，索引从1开始
    wealth = [0] * (N + 1)

    # 读取每个成员的财富值
    for i in range(1, N + 1):
        wealth[i] = int(data[index])
        index += 1

    # 构建树结构，使用邻接表存储每个节点的子节点
    children = defaultdict(list)

    # 读取父子关系，构建树
    for _ in range(1, N):
        parent = int(data[index])
        index += 1
        child = int(data[index])
        index += 1
        children[parent].append(child)

    # 寻找最富裕的小家庭
    maxWealth = 0
    for i in range(1, N + 1):
        familyWealth = wealth[i]  # 小家庭的财富总和起始为父节点的财富值
        # 加上所有直接子节点的财富值
        for child in children[i]:
            familyWealth += wealth[child]
        # 更新最大财富和
        if familyWealth > maxWealth:
            maxWealth = familyWealth

    # 输出最大财富和
    print(maxWealth)


if __name__ == "__main__":
    main()