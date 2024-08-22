# 有一个字符串数组 words 和一个字符串 chars 。
#
# 假如可以用 chars 中的字母拼写出 words 中的某个“单词”（字符串），那么我们就认为你掌握了这个单词。
#
# words 的字符仅由 a-z 英文小写字母组成，例如 “abc” chars 由 a-z 英文小写字母和 “?” 组成。其中英文问号 “?” 表示万能字符，能够在拼写时当做任意一个英文字母。
#
# 例如：“?” 可以当做 “a” 等字母。
#
# 注意：每次拼写时，chars 中的每个字母和万能字符都只能使用一次。
#
# 输出词汇表 words 中你掌握的所有单词的个数。没有掌握任何单词，则输出 0。
#
# 输入
# 第 1 行输入数组 words 的个数，记为 N。
#
# 从第 2 行开始到第 N+1 行一次输入数组 words 的每个字符串元素。
#
# 第 N+2 行输入字符串 chars。
#
# 输出
# 输出一个整数，表示词汇表 words 中你掌握的单词个数。
# 样例输入 复制
# 4
# cat
# bt
# hat
# tree
# at?ch
# 样例输出 复制
# 3
# 提示
# at?ch可以拼写出单词cat、hat和bt，因此掌握的单词是3个。

from collections import defaultdict

#处理输入
n = int(input())
words = []
for i in range(n):
    words.append(input())
chars = input()


def spell(word, chars):
    dic = defaultdict(int)
    ans = 0
    for i in chars:
        dic[i] += 1
    for i in word:
        cnt = len(i)
        tmp = dic.copy()
        for n in i:
            if n in tmp and tmp[n] > 0:
                cnt -= 1
                tmp[n] -= 1
        if cnt - tmp["?"] <= 0:
            ans += 1
    return ans


print(spell(words, chars))
