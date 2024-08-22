# for i in range(1, 10):
#     for j in range(i,10):
#         print(f'{i}x{j}={i*j}\t', end=' ')
#     print()
# from collections import Counter
#
# counters = Counter()
# i = int(input())
# ans = list()
# for n in range(100,i+1):
#     if  n == (n%10)**3 + (n//10%10)**3 + (n//100)**3
#         ans.append(n)
# for s in ans:
#     print(s)
# lst = list(map(int, input().split()))
# k = int(input())
# n = k % (len(lst))
# ans = lst[-n:] + lst[:-n]
# print(" ".join(str(i) for i in ans))
# from cmath import inf
#
# n = list(map(int,input().split()))
# min = inf
# max = -inf
# sum = 0
# for i in range(len(n)):
#     if n[i] > max:
#          max = n[i]
#     if n[i] < min:
#          min = n[i]
#     sum += n[i]
# print(f'{min} {max} {sum}')
input = "1,1,0,0,1,1,1,0,1"
cars = input.strip().replace(",", "")
cars = [i for i in cars.split("0") if i]
ans = 0
for j in cars:
    n = len(j)
    count = 1
    while n > 3:
        count += 1
        n -= 3
    ans += count
print(ans)
