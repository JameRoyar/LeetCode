# 2528: 【模拟】2023C-素数之积
# 内存限制：128 MB
# 时间限制：10.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：223
# 解决：106
# 题目描述
# RSA加密算法在网络安全世界中无处不在，它利用了极大些数因数分解的闲难度，数据越大，安全系数越高，给定一个32位整数，请对其进行因数分解，找出是哪两个素数的乘积。
# 输入
# 1个正整数num
#
# 0 < num <= 2147483647
#
# 输出
# 如果成功找到，以单个空格分割，从小到大输出两个素数。分解失败，请输出-1 -1
# 样例输入 复制
# 15
# 样例输出 复制
# 3 5
# 提示
# 因数分解后，找到两个素数3和5，使得3*5=15，按从小到大排列后，输出3 5

from math import floor, sqrt


# 使用埃氏筛计算数组
def sieve_of_eratosthenes(n):
    # 构建埃氏筛，长度为n+1，初始化均为True，表示默认为质数
    sieve = [True] * (n + 1)
    # 0和1不是质数
    sieve[0], sieve[1] = False, False
    # 枚举从2到floor(sqrt(x))的每一个数x
    for x in range(2, floor(sqrt(n)) + 1):
        # 如果x是一个质数，则说明其m倍（m >= 2）的所有正整数是合数
        if sieve[x] == True:
            # 将mx标记为False
            for i in range(2 * x, n + 1, x):
                sieve[i] = False

    # 退出循环后，sieve中所有为True的元素下标为质数
    primes = [i for i in range(n + 1) if sieve[i]]
    return primes


num = int(input())
# 计算所有小于num的素数
primes = sieve_of_eratosthenes(num)
primes_set = set(primes)

# 初始化一个标记，表示是否找到一组素数
isFind = False
# 遍历所有小于num的素数a
for a in primes:
    # 如果num可以整除a
    if num % a == 0:
        # 则计算b是否也是素数
        b = num // a
        # 如果是，则输出(a, b)
        # 同时标记isFind为True，表示计算得到一组答案
        # 同时退出循环
        if b in primes_set:
            print(a, b)
            isFind = True
            break

# 如果退出循环后，isFind仍为False，则输出(-1, -1)
if isFind == False:
    print(-1, -1)