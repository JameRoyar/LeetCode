# 输入输出处理
# n = int(input())
# lst = [input().split() for i in range(n)]


def isAward(list):
    absent, present = 0, 0
    pre = ""
    for i in range(len(list)):
        cur = list[i]
        if cur == "absent":
            absent += 1
            if absent > 1:
                return False
        if cur in ["late", "leave early"]:
            if pre in ["late", "leave early"]:
                return False
        elif cur == "present":
            present += 1

        if i > 6:
            if present < 4:
                return False
            if list[i - 6] == "present":
                present -= 1

    return True


lst = [['present'], ['present', 'absent', 'present', 'present', 'leaveearly', 'present', 'absent']]


def result(list):
    for lst in list:
        if isAward(lst):
            print("true", end=" ")
        else:
            print("false", end=" ")


result(lst)

'''
========[test_1.out]=========
Expected						      |	Yours
true false true false false true false false false false fals
							      /	true false true false false true false false true false false

==============================
========[test_2.out]=========
Expected						      |	Yours
false true true false false false false true false false true
							      /	true true true false false false false true false false true 

==============================
========[test_5.out]=========
Expected						      |	Yours
false false false true false true false true true true false 
							      /	false false false true false true true true true true false f

==============================
========[test_6.out]=========
Expected						      |	Yours
true false true false true false true false false false false
							      /	true false true false true false true false false false false

==============================
========[test_7.out]=========
Expected						      |	Yours
false false true false true false false true false true false
							      /	false true true false true false false true false true false 

==============================
========[test_8.out]=========
Expected						      |	Yours
true true true false false true true true false false false t
							      /	true true true false true true true true false false false tr

==============================
========[test_9.out]=========
Expected						      |	Yours
false false false false true false true false true true true 
							      /	true false true false true false true true true true true tru

==============================
time_space_table:
/3255/sample.in:AC mem=16472k time=33ms
/3255/test_1.in:WA mem=16472k time=34ms
/3255/test_2.in:WA mem=16472k time=33ms
/3255/test_3.in:AC mem=16472k time=33ms
/3255/test_4.in:AC mem=16472k time=33ms
/3255/test_5.in:WA mem=16472k time=31ms
/3255/test_6.in:WA mem=16472k time=32ms
/3255/test_7.in:WA mem=16472k time=33ms
/3255/test_8.in:WA mem=16472k time=33ms
/3255/test_9.in:WA mem=16472k time=31ms
'''
