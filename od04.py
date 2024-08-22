#lst = list(map(int, input().split(" ")))
#t = int(input())
import collections
from collections import defaultdict


# print(lst)
# print(t)
def maxColorCar(lst, t):
    ans = 0
    left, right = 0, 0
    cot = collections.defaultdict(int)
    for i in range(min(t, len(lst))):
        cot[lst[i]] += 1
        ans = max(ans, cot[lst[i]])
    for i in range(t, len(lst)):
        add = lst[i]
        rem = lst[i - t]
        cot[add] += 1
        cot[rem] -= 1
        ans = max(ans, cot[add])
    return ans

lst=[0,1,2,1]
t=3
print(int(maxColorCar(lst, t)))
