'''
小华负责公司知识图谱产品，现在要通过新词挖掘完善知识图谱。
新词挖掘：给出一个待挖掘文本内容字符串content和一个词的字符串word，找到content中所有word的新词。
新词：使用词word的字符排列形成的字符串。
请帮小华实现新词挖掘，返回发现的新词的数量。

输入

第一行输入为待挖掘的文本内容content；
第二行输入为词word；

输出

在中找到的所有word的新词的数量。

样例输入 复制
qweebaewqd
qwe
样例输出 复制
2
'''


def newWordNums(lst, word):
    ans = 0
    total = len(word)
    left, right = 0, 0
    dic = {}

    for i in word:
        if dic.get(i) is None:
            dic[i] = 1
        else:
            dic[i] += 1

    for i in range(len(word)):
        w = lst[i]
        if dic.get(w) is not None:
            if dic[w] > 0:
                total -= 1
            dic[w] -= 1
    if total == 0:
        ans += 1
    for i in range(len(lst) - len(word)):
        remove = lst[i]
        add = lst[i + len(word)]
        if dic.get(remove) is not None:
            if dic[remove] >= 0:
                total += 1
            dic[remove] += 1
        if dic.get(add) is not None:
            if dic[add] > 0:
                total -= 1
            dic[add] -= 1
        if total == 0:
            ans += 1
    return ans

lst = "qweebaewqd"
s= "qwe"
print(int(newWordNums(lst,s)))