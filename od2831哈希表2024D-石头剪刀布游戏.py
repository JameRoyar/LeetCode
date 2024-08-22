# 2831: 【哈希表】2024D-石头剪刀布游戏
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：349
# 解决：154
# 题目描述
# 石头剪刀布游戏有 3 种出拳形状：石头、剪刀、布。分别用字母 A , B , C 表示。 游戏规则:
#
# 1. 出拳形状之间的胜负规则如下： A > B；B > C；C > A；">"左边一个字母，表示相对优势形状。右边一个字母，表示相对劣势形状。
#
#  2. 当本场次中有且仅有一种出拳形状优于其它出拳形状，则该形状的玩家是胜利者。否则认为是平局。
#
# 3. 当发生平局，没有赢家。有多个胜利者时，同为赢家。
#
# 例如 1： 三个玩家出拳分别是A, B, C ，由于出现三方优势循环(即没有任何一方优于其它出拳者)，判断为平局。
#
# 例如 2： 三个玩家，出拳分别是 A, B ，出拳 A 的获胜。
#
# 例如 3： 三个玩家，出拳全部是 A ，判为平局。
#
# 输入
# 在一场游戏中，每个玩家的信息为一行。玩家数量不超过 1000 。
#
# 每个玩家信息有 2 个字段，用空格隔开：
#
#  1. 玩家 ID：一个仅由英文字母和数字组成的字符串
#
# 2. 出拳形状：以英文大写字母表示, A 、B 、C 形状。
#
# 例：
#
# abc1 A
#
# xyz B
#
# 解释：
#
# 玩家 abc1 出拳为石头( A )。玩家 xyz 出拳为剪刀( B )
#
# 输出
# 输出为赢家的玩家 ID 列表(一个或多个)，每个 ID 一行，按字符串升序排列。如果没有赢家，输出为"NULL"字符串。
#
# 例如：
#
# abc1
#
# 样例输入 复制
# abc1 A
# def A
# alic A
# xyz B
# 样例输出 复制
# abc1
# alic
# def

from collections import defaultdict
dic = defaultdict(list)
while True:
    try:
        name,k = input().split()
        dic[k].append(name)

    except:
        break

if len(dic) != 2:
    print("NULL")
else:
    if "A" in dic and "B" in dic:
        ans = dic["A"]
    if "B" in dic and "C" in dic:
        ans = dic["B"]
    if "C" in dic and "A" in dic:
        ans = dic["C"]

    for name in sorted(ans):
        print(name)

