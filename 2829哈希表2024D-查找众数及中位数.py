# 1. 众数是指一组数据中出现次数最多的那个数，众数可以是多个
#
# 2. 中位数是指把一组数据从小到大排列，最中间的那个数，如果这组数据的个数是奇数，那最中间那个就是中位数，如果这组数据的个数为偶数，那就是中间的两个数之和除以2，所以得的结果就是中位数
#
# 3. 查找整型数组中元素的众数并组成一个新的数组，求新数组的中位数
#
# 输入
# 输入一个一维整型数组，数组大小取值范围0 < N < 1000，数组中每个元素取值范围 0 < E < 1000
# 输出
# 输出众数组成的新数组的中位数

from collections import Counter

lst = list(map(int, input().split()))
cot = Counter(lst)
max_num = max(cot.values())
arr = []
for key, value in dict(cot).items():
    if value == max_num:
        arr.append(key)
n = len(arr)
arr.sort()
ans = 0
if n % 2 == 0:
    ans = (arr[n // 2] + arr[n // 2 - 1]) / 2
else:
    ans = arr[(n-1)//2]
print(ans)
