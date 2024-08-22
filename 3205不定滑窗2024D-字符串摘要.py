# 给定一个字符串的摘要算法，请输出给定字符串的摘要值
#
# 1、去除字符串中非字母的符号
#
# 2、对于去除非字母符号后的字符串：如果出现连续字符(不区分大小写) ，则输出: 该字符(小写) + 连续出现的次数
#
# 3、对于去除非字母符号后的字符串：如果是非连续的字符（不区分大小写) ，则输出: 该字符(小写)
# 该字母之后字符串中出现的该字符的次数
#
# 4、对按照以上方式表示后的字符串进行排序: 字母和紧随的数字作为一组进行排序，数字大的在前，数字相同的则按字母进行排序，字母小的在前。
#
# 输入
# 一行字符串，长度为[1, 200]
# 输出
# 转换后的摘要字符串
# 样例输入
# 复制
# bAaAcBb
# 样例输出
# 复制
# a3b2b2c0
# 提示
#
# 第一个b非连续字母，该字母之后字符串中还出现了2次(最后的两个Bb) ，所以输出b2；
#
#
# a连续出现3次，输出a3；
#
#
# c非连续，该字母之后字符串再没有出现过c，输出c0；
#
#
# Bb连续2次，输出b2。
#
#
# 对b2a3c0b2进行排序，最终输出a3b2b2c0。
from collections import defaultdict

# 输入处理
s = input()
# 去除非字母符号
s = ''.join(i for i in s if i.isalpha())
# 变成小写字符串
s = s.lower()
# 从右边到左边的滑动窗口遍历
n = len(s)
right = n - 1
dic = defaultdict(int)
ans = []
def updateAns(left, right, dic, s, ans):
    continueNum = right - left
    if continueNum == 1:
        ans.append([s[right], dic[s[right]]])
    else:
        ans.append([s[right], continueNum])
    dic[s[right]] += continueNum


for left in range(n - 1, -1, -1):
    if s[left] != s[right]:
        updateAns(left, right, dic, s, ans)
        right = left

# 更新最后一个字符
updateAns(-1, right, dic, s ,ans)
# 排序
ans.sort(key=lambda x:(-x[1], x[0]))

# 输出
print(''.join(i[0] + str(i[1]) for i in ans))
