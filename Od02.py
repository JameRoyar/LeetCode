
'''
n = int(input())
gems = list()
for i in range(n):
    gems.append(int(input()))
v = int(input())
'''

def MaxGemsNum(n, gems, v):
    ans = 0
    left, right = 0, 0
    curV = 0

    while right < n and left <= right:
        if curV < v:
            curV += gems[right]
            right += 1
            ans = max(ans, right - left)

        else:
            curV -= gems[left]
            left += 1

    return ans

n = 7
gems = [8,4,6,3,1,6,7]
v = 10
print(int(MaxGemsNum(n, gems, v)))

'''
========[test_1.out]=========
Expected						      |	Yours
2
							      |	3

==============================
========[test_2.out]=========
Expected						      |	Yours
2
							      |	3

==============================
========[test_3.out]=========
Expected						      |	Yours
1
							      |	2

==============================
========[test_4.out]=========
Expected						      |	Yours
0
							      |	1

==============================
========[test_5.out]=========
Expected						      |	Yours
2
							      |	3

==============================
========[test_6.out]=========
Expected						      |	Yours
2
							      |	3

==============================
========[test_7.out]=========
Expected						      |	Yours
1
							      |	2

==============================
========[test_8.out]=========
Expected						      |	Yours
2
							      |	3

==============================
========[test_9.out]=========
Expected						      |	Yours
2
							      |	3

==============================
time_space_table:
/3207/sample.in:AC mem=16340k time=30ms
/3207/test_1.in:WA mem=16340k time=43ms
/3207/test_2.in:WA mem=16476k time=145ms
/3207/test_3.in:WA mem=16484k time=51ms
/3207/test_4.in:WA mem=16484k time=29ms
/3207/test_5.in:WA mem=16484k time=90ms
/3207/test_6.in:WA mem=16484k time=249ms
/3207/test_7.in:WA mem=16484k time=206ms
/3207/test_8.in:WA mem=16484k time=292ms
/3207/test_9.in:WA mem=16484k time=216ms


'''