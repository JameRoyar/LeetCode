# class Solution:
#     @staticmethod
#     def nextPermutation(nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # 从后往前寻找第一组升序的排列
#         # 找到并且标记第一个数字的位置
#         # 再在[first,end]区间从后往前寻找第一个大于这个数字的下标
#         # 交换两个元素位置
#         # reserve[first,end]区间
#
#         # 定义reserve函数
#         n = len(nums)
#
#         def reserve(num):
#             l, r = 0, len(num) - 1
#             while l < r:
#                 num[l], num[r] = num[r], num[l]
#                 l += 1
#                 r -= 1
#
#         first = -1
#         # 倒序寻找第一组升序排列
#         for i in range(n - 2, -1, -1):
#             if nums[i] < nums[i + 1]:
#                 first = i
#                 break
#
#         # 说明都是降序排列 按照题意返回下一个排列 即全倒序
#         if first == -1:
#             reserve(nums)
#             return
#
#         second = -1
#         for i in range(n - 1, first, -1):
#             if nums[i] > nums[first]:
#                 second = i
#                 break
#         nums[second], nums[first] = nums[first], nums[second]
#         reserve(nums[first + 1:n])
#
# nums = [1,3,2]
# Solution.nextPermutation(nums)
# print(nums)
from heapq import heapify

lists = [[1,4,5],[1,3,4],[2,6]]
h = [head for head in lists if head]  # 初始把所有链表的头节点入堆
print(h)
heapify(h)
print(h)