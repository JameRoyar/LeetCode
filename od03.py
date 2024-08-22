#lst = list(map(int,input().split(",")))
#k = int(input())

def maxBoxNum(lst, k):
    ans = 0
    left,right=0,0
    sum = 0
    while right<len(lst):
        sum += lst[right]
        right +=1
        if right - left < k:continue
        ans = max(ans,sum)
        sum -= lst[left]
        left += 1
    return ans


lst = [2, 10, -3, -8, 40, 5]
k = 4
print(int(maxBoxNum(lst, k)))

'''
========[test_1.out]=========
Expected						      |	Yours
591019
							      |	756152

==============================
========[test_10.out]=========
Expected						      |	Yours
1371214
							      |	1375301

==============================
========[test_11.out]=========
Expected						      |	Yours
2434111
							      |	2436062

==============================
========[test_12.out]=========
Expected						      |	Yours
686207
							      |	681074

==============================
========[test_13.out]=========
Expected						      |	Yours
-16360
							      |	1493884

==============================
========[test_14.out]=========
Expected						      |	Yours
1741685
							      |	1752789

==============================
========[test_15.out]=========
Expected						      |	Yours
1456480
							      |	1454671

==============================
========[test_16.out]=========
Expected						      |	Yours
1769560
							      |	1774302

==============================
========[test_17.out]=========
Expected						      |	Yours
1777235
							      |	1783948

==============================
========[test_18.out]=========
Expected						      |	Yours
354128
							      |	865476

==============================
========[test_19.out]=========
Expected						      |	Yours
992198
							      |	1004313

==============================
========[test_2.out]=========
Expected						      |	Yours
975253
							      |	972475

==============================
========[test_3.out]=========
Expected						      |	Yours
985127
							      |	966911

==============================
========[test_4.out]=========
Expected						      |	Yours
788592
							      |	780709

==============================
========[test_5.out]=========
Expected						      |	Yours
335863
							      |	375247

==============================
========[test_6.out]=========
Expected						      |	Yours
664297
							      |	1585487

==============================
========[test_7.out]=========
Expected						      |	Yours
853170
							      |	851819

==============================
========[test_8.out]=========
Expected						      |	Yours
927834
							      |	925327

==============================
========[test_9.out]=========
Expected						      |	Yours
862475
							      |	847903

==============================
time_space_table:
/3250/sample.in:AC mem=16340k time=33ms
/3250/test_1.in:WA mem=22624k time=64ms
/3250/test_10.in:WA mem=22624k time=64ms
/3250/test_11.in:WA mem=22624k time=63ms
/3250/test_12.in:WA mem=22624k time=66ms
/3250/test_13.in:WA mem=22624k time=63ms
/3250/test_14.in:WA mem=22624k time=65ms
/3250/test_15.in:WA mem=22624k time=65ms
/3250/test_16.in:WA mem=22624k time=62ms
/3250/test_17.in:WA mem=22624k time=62ms
/3250/test_18.in:WA mem=22624k time=64ms
/3250/test_19.in:WA mem=22624k time=66ms
/3250/test_2.in:WA mem=22624k time=66ms
/3250/test_3.in:WA mem=22624k time=66ms
/3250/test_4.in:WA mem=22624k time=66ms
/3250/test_5.in:WA mem=22624k time=64ms
/3250/test_6.in:WA mem=22624k time=63ms
/3250/test_7.in:WA mem=22624k time=65ms
/3250/test_8.in:WA mem=22624k time=66ms
/3250/test_9.in:WA mem=22624k time=65ms


'''