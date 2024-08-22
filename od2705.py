'''
给定一个数组，编写一个函数来计算它的最大N个数与最小N个数的和。

你需要对数组进行去重。

数组中数字范围[0，1000] 最大N个数与最小N个数不能有重叠，如有重叠返回-1

输入
第一行输入M， M标识数组大小

第二行输入M个数，标识数组内容

第三行输入N，N表达需要计算的最大、最小N个数
'''
# size = int(input())
# arr = list(map(int(), input()))
# n = int(input())

'''
去重直接放到set里面
1.去重
2.找到最大最小的n个数字
3.存储他们
4.比较重复
5.求和返回
'''


def sumOfMaxNNumbers(size, arr, n):
    sum = 0
    arr = list(set(arr))
    if len(arr) < 2 * n:
        return -1
    else:
        arr.sort()
        if arr[0] < 0 or arr[-1] > 1000:
            return -1
        for i in range(n):
            sum += arr[i] + arr[-1 - i]
        return sum

    return -1


size = 5
arr = [95, 88, 83, 64, 100]
n = 2
print(sumOfMaxNNumbers(size, arr, n))
