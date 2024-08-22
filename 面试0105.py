# 字符串有三种编辑操作:插入一个英文字符、删除一个英文字符或者替换一个英文字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。
#
#
#
#  示例 1:
#
#
# 输入:
# first = "pale"
# second = "ple"
# 输出: True
#
#
#
#  示例 2:
#
#
# 输入:
# first = "pales"
# second = "pal"
# 输出: False
#
#
#  Related Topics 双指针 字符串 👍 261 👎 0


class Solution(object):
    def oneEditAway(self, first, second):
        """
        :type first: str
        :type second: str
        :rtype: bool
        """
        if abs(len(first) - len(second)) > 1: return False

        if len(first) == len(second):
            odd = 0
            for i in range(len(first)):
                if first[i] != second[i]:
                    odd += 1
                    if odd > 1: return False
            return True

        if len(first) > len(second):
            first, second = second, first
        if len(first) or len(second) == 0: return True
        i, j, odd = 0, 0, 0
        while i < len(first) and j < len(second):
            if first[i] != second[j]:
                j += 1
                odd += 1
                if odd > 1: return False
                break
            i += 1
            j += 1

        return True


first = "mart"
second = "karma"
print(Solution().oneEditAway(first, second))
