from collections import defaultdict

n = list(input().split(","))
dic = dict()
for i in range(len(n)):
    for j, k in enumerate(n[i]):
        if k == "1":
            if j not in dic:
                dic[j] = 1
            else:
                dic[j] += 1
print(min(dic.values()))
