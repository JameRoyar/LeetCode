#
# 有这么一款单人卡牌游戏，牌面由颜色和数字组成，颜色为红、黄、蓝、绿中的一种，数字为0-9 中的一个。
#
# 游戏开始时玩家从手牌中选取一张卡牌打出，接下来如果玩家手中有和他上一次打出的手牌颜色或者数字相同的手牌，他可以继续将该手牌打出，直至手牌打光或者没有符合条件可以继续打出的手牌。
#
# 现给定一副手牌，请找到最优的出牌策略，使打出的手牌最多。
#
# 输入
# 输入为两行，第一行是每张手牌的数字，数字由空格分隔，第二张为对应的每张手牌的颜色， 用r y b g这4个字母分别代表4种颜色，字母也由空格分隔。手牌数量不超过10。
# 输出
# 输出一个数字，即最多能打出的手牌的数量。
# 样例输入 复制
# 1 4 3 4 5
# r y b b r
# 样例输出 复制
# 3
# 来源/分类

# input
number = list(map(int, input().split()))
color = list(input().split())
n = len(number)
# backtrack
ans = 0
visited = [False] * n


def backtrack(cur_number, cur_color, number, color, path, visited):
    global ans
    ans = max(ans, path)
    for i in range(n):
        if visited[i]:
            continue
        if color[i] == cur_color or number[i] == cur_number:
            visited[i] = True
            backtrack(number[i], color[i], number, color, path + 1, visited)
            visited[i] = False


for j in range(n):
    visited[j] = True
    backtrack(number[j], color[j], number, color, 1, visited)
    visited[j] = False

print(ans)
