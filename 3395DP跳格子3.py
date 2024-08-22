from collections import deque
n = int(input())
a = list(map(int,input().split()))
k = int(input())
inf = 10**8
f = [-inf for i in range(n)]
q = deque([0])
f[0] = a[0]
for i in range(1,n):
    while len(q)>0 and i-q[0]>k:
        q.popleft()
    f[i]=f[q[0]]+a[i]
    while len(q)>0 and f[i]>=f[q[-1]]:
        q.pop()
    q.append(i)
print(f[-1])