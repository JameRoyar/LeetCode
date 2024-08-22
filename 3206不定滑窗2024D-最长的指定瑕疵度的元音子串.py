# 头和结尾都是元音字母（aeiouAEIOU）的字符串为元音字符串，其中混杂的非元音字母数量为其瑕疵度。比如:
#
# - "a"，"aa"是元音字符串，其瑕疵度都为 0
#
# - "aiur"不是元音字符串（结尾不是元音字符）
#
# - "abira"是元音字符串，其瑕疵度为 2
#
# 给定一个字符串，请找出指定瑕疵度的最长元音字符子串，并输出其长度，如果找不到满足条件的元音字符子串，输出 0。
#
# 子串：字符串中任意个连续的字符组成的子序列称为该字符串的子串。
#
# 输入
# 首行输入是一个整数，表示预期的瑕疵度flaw，取值范围[0, 65535]。
#
# 接下来一行是一个仅由字符a-z和A-Z组成的字符串，字符串长度(0, 65535]。
#
# 输出
# 输出为一个整数，代表满足条件的元音字符子串的长度。
# 样例输入 复制
# 2
# aeueo
# 样例输出 复制
# 0
# 0
# asdbuiodevauufgh

k = int(input())
s = input()
n = len(s)


def is_vowel(c):
    return c in 'aeiouAEIOU'


left = 0
ans  = 0
not_vowel_count = 0

# find first vowel
for i in range(n):
    if is_vowel(s[i]):
        left = i
        break

if left == n:
    print(0)
else:
    for right,c in enumerate(s[left:],left):
        if is_vowel(c):
            if not_vowel_count == k:
                ans = max(ans, right - left + 1)
        else:
            not_vowel_count += 1
            while left < n and (not_vowel_count>k or not is_vowel(s[left])):
                if not is_vowel(s[left]):
                    not_vowel_count -= 1
                left += 1

print(ans)