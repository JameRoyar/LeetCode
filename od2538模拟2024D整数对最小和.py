# 2538: 【模拟】2024D-整数对最小和
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：109
# 解决：30
# 题目描述
# 给定两个整数数组array1、array2，数组元素按升序排列。假设从array1、array2中分别取出一个元素可构成一对元素，现在需要取出k对元素，并对取出的所有元素求和计算和的最小值。
#
# 注意：两对元素如果对应于array1、array2中的两个下标均相同，则视为同一对元素。
#
# 输入
# 输入两行数组array1、array2，每行首个数字为数组大小size(0 < size <= 100)
#
# 0 < array1[i] <= 1000
#
# 0 < array2[i] <= 1000
#
# 接下来一行为正整数k 0 < k <= array1.size()*array2.size()
#
# 输出
# 满足要求的最小和
# 样例输入 复制
# 3 1 1 2
# 3 1 2 3
# 2
# 样例输出 复制
# 4
# 来源/分类
# 优先队列 数组 模拟 华为OD真题-100分

#input
tmp1 = list(map(int,input().split()))
tmp2 = list(map(int,input().split()))
k = int(input())
a1 = tmp1[1:]
a2 = tmp2[1:]

#solution
lst = []
for i in range(len(a1)):
    for j in range(len(a2)):
        lst.append(a1[i]+a2[j])
lst.sort()
print(sum(lst[:k]))