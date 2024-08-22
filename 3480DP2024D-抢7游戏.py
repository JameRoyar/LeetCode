# 3480: 【DP】2024D-抢7游戏
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：237
# 解决：148
# 题目描述
# A、B两个人玩抢7游戏，游戏规则为A先报一个起始数字X (10<X<10000），B报下一个数字Y，(0<X-Y<3)，A再报一个数字Z(0<Y-Z<3)，以此类推，直到其中一个抢到7，抢到7即为胜者，在B赢得比赛的情况下，一共有多少种组合？
# 输入
# 起始数字M，如100
#
#  10<=M<=10000
#
# 输出
# B能赢得比赛的组合次数
# 样例输入 复制
# 10
# 样例输出 复制
# 1
# 提示
# 只有一种赢的组合，A起始选择10，B接着选择9，A接着选择8，B接着选择7赢得胜利。
import math
# 问题分析：
# 这个游戏本质上是从起始数字 m 到 7 的一个递减过程。
# 每次可以选择减1或减2，对应了两种操作。
# B 想要赢，必须在轮到自己时拿到 7。
# 问题转化：
# 我们可以将问题转化为排列组合问题。
# 从 m 到 7 的过程可以看作是排列若干个"减1"和"减2"操作。
# "减1"操作的次数 = m - 7
# 总操作次数必须为奇数，这样最后一步（到7）才会是 B 操作。
# 计算策略：
# 初始时，所有操作都是"减1"，即 oneCount = m - 7, twoCount = 0。
# 然后我们逐步将两个"减1"合并为一个"减2"，遍历所有可能的组合。
# 对于每种有效组合（总步数为奇数），计算其不重复排列数。
# 排列数计算：
# 使用组合数学公式：(oneCount + twoCount)! / (oneCount! * twoCount!)
# 这个公式计算了在总操作序列中，"减1"和"减2"的所有不重复排列方式。
# 大数处理：
# 由于数字可能很大，我们使用 BigInteger 来处理计算，避免溢出。
# 预先计算阶乘，存储在数组中，以提高效率。
# 结果累加：
# 对每种有效组合的排列数进行累加，得到最终 B 获胜的总情况数。

def count_combinations(m):
    """
    计算B获胜的总方案数
    Args:
        m: 初始数字
    Returns:
        B获胜的总方案数
    """
    # 初始化阶乘数组，Python中可以直接使用math.factorial()函数
    # 这里为了与Java代码保持一致，也使用数组存储阶乘
    factorial = [1]
    for i in range(1, m - 6):  # 只需要计算到m-7的阶乘
        factorial.append(factorial[-1] * i)

    one_count = m - 7  # 初始的1的数量
    two_count = 0  # 初始的2的数量
    total_count = 0

    # 遍历所有可能的1和2的组合
    while one_count >= 0:
        # 当总步数为奇数时，B才能赢
        if (one_count + two_count) % 2 != 0:
            # 计算当前组合的排列数，并加到总数中
            total_count += factorial[one_count + two_count] // (factorial[one_count] * factorial[two_count])
        # 将两个1合并为一个2
        one_count -= 2
        two_count += 1

    return total_count

if __name__ == "__main__":
    m = int(input())
    result = count_combinations(m)
    print(result)
