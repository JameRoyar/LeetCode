# 现代计算机系统中通常存在多级的存储设备，针对海量workload的优化的一种思路是将热点内存页优先放到快速存储层级，这就需要对内存页进行冷热标记。
#
# 一种典型的方案是基于内存页的访问频次进行标记，如果统计窗口内访问次数大于等于设定阈值，则认为是热内存页，否则是冷内存页。
#
# 对于统计窗口内跟踪到的访存序列和阈值，现在需要实现基于频次的冷热标记。内存页使用页框号作为标识。
#
# 输入
# 第一行为输入为N，表示访存序列的记录条数，0 < N < 10000。
#
# 第二行为访存序列，空格间隔的N个内存页框号，页框号范围0-65535，同一页框号可能重复出现，出现的次数即为对应页框号的频次。
#
# 第三行为热内存页的频次阈值T，正整数，范围1< T < 10000
#
# 输出
# 第一行输出标记为热内存的内存页个数，如果没有被标记为热内存的，则输出0。
#
# 如果第一行>0，则接下来按照访问频次降序输出内存页框号，一行一个，频次一样的页框号，页框号小的排前面。
#
# 样例输入 复制
# 10
# 1 2 1 2 1 2 1 2 1 2
# 5
# 样例输出 复制
# 2
# 1
# 2
# 提示
# 内存页1和内存页2均被访问了5次，达到了阈值5，因此热内存页有2个。
# 内存页1和内存页2的访问频次相等，页框号小的排前面。

#输入处理
n = int(input())
lst = list(map(int, input().split()))
t = int(input())


#标记
def markhot(n, lst, t):
    if n == 0:
        return -1

    dic = dict()
    for i in lst:
        if i not in dic:
            dic[i] = 0
        else:
            dic[i] += 1
    ans = list()
    for key, value in dic.items():
        if value >= t-1:
            ans.append(key)
    if ans:
        print(len(ans))
        for i in ans:
            print(i)
    return


markhot(n, lst, t)
print(0)

from collections import Counter

# 输入数组长度
n = int(input())
# 输入内存页框号数组
nums = list(map(int, input().split()))
# 输入阈值t
t = int(input())

# 计算nums中每一个编号的出现次数
cnt = Counter(nums)
# 将cnt中所有v小于t的k过滤掉，cnt_filter中均为出现次数大于等于阈值t的k
cnt_filter = {k: v for k, v in cnt.items() if v >= t}
# cnt_filter的长度即为热内存页的个数
print(len(cnt_filter))

# 获得cnt_filter中的所有编号，构成一个数组
ans = list(k for k in cnt_filter.keys())
# 对ans进行排序，先按照出现频次逆序排序，再按照编号大小升序排序
ans.sort(key = lambda k: (-cnt_filter[k], k))
# 对ans排序完毕后，逐行输出num
for num in ans:
    print(num)
Python
Java