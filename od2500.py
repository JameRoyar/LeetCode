tmp1 = "b 3 a b c"
tmp = tmp1.split()
index = tmp[0]
cot = int(tmp[1])
words = tmp[2:2 + cot]


def searchDict(index, cot, words):
    find = False
    for i in range(len(words)):
        if words[i].startswith(index):
            find = True
            print(words[i])
    if not find:
        print(-1)


searchDict(index, cot, words)