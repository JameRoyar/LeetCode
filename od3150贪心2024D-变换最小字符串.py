# 3150: 【贪心】2024D-变换最小字符串
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：353
# 解决：158
# 题目描述
# 给定一个字符串s，最多只能进行一次变换，返回变换后能得到的最小字符串（按照字典序进行比较）
#
# 变换规则： 交换字符串中任意两个不同位置的字符。
#
# 输入
# 一串小写字母组成的字符串s
# 输出
# 按照要求进行变换得到的最小字符串
# 样例输入 复制
# edcba
# 样例输出 复制
# adcbe
# 提示
# s是都是小写字符组成
#
# 1 <= s.length <= 1000
#
# 来源/分类
# 栈 贪心 2024D 华为OD真题-100分

# lst = list(input())
# ans = "".join(lst)
# n = len(lst)
# stack = list()
# for i in range(n - 1, -1, -1):
#     if not stack or lst[i] < lst[stack[-1]]:
#         stack.append(i)
# for i in range(n):
#     if not stack:
#         break
#     if i < stack[-1]:
#         if lst[i] > lst[stack[-1]]:
#             lst[i], lst[stack[-1]] = lst[stack[-1]], lst[i]
#             ans = "".join(lst)
#             break
#     else:
#         stack.pop()
# print(ans)
# class Solution:
#     def maximumSwap(self, num: int) -> int:
#         s = str(num)
#         ans = num
#         lst = list(map(int,s.split()))
#         n = len(lst)
#         stack = list()
#         for i in range(n-1,-1,-1):
#             if not stack or lst[i] > lst[stack[-1]]:
#                 stack.append(i)
#         for i in range(n):
#             if not stack:
#                 break
#             if i < stack[-1]:
#                 if lst[i] < lst[stack[-1]]:
#                     lst[i],lst[stack[-1]] = lst[stack[-1]],lst[i]
#                     ans = int("".join(str(lst)))
#                     break
#             else:
#                 stack.pop()
#         return ans

# import unittest
#
# class TestMaximumSwap(unittest.TestCase):
#     def test_empty_stack(self):
#         num = 123
#         ans = 123
#         self.assertEqual(ans, Solution().maximumSwap(num))
#
#     def test_single_element_stack(self):
#         num = 9
#         ans = 99
#         self.assertEqual(ans, Solution().maximumSwap(num))
#
#     def test_all_elements_larger_or_equal_to_top(self):
#         num = 12345678
#         ans = 98765432
#         self.assertEqual(ans, Solution().maximumSwap(num))

class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        ans = num
        lst = list()
        for i in s:
            lst.append(int(i))
        n = len(lst)
        stack = list()
        for i in range(n - 1, -1, -1):
            if not stack or lst[i] > lst[stack[-1]]:
                stack.append(i)
        for i in range(n):
            if not stack:
                break
            if i < stack[-1]:
                if lst[i] < lst[stack[-1]]:
                    lst[i], lst[stack[-1]] = lst[stack[-1]], lst[i]
                    ans = int("".join(str(ch) for ch in lst))
                    break
            else:
                stack.pop()
        return ans


a = Solution()
num = 2736
print(a.maximumSwap(num))
