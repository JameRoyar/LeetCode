# 2537: 【模拟】2024D-绘图机器
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：103
# 解决：52
# 题目描述
# 绘图机器的绘图笔初始位置在原点(0,0)，机器启动后其绘图笔按下面规则绘制直线：
#
# 1) 尝试沿着横向坐标轴正向绘制直线，直到给定的终点值E。
#
# 2) 期间可通过指令在纵坐标轴方向进行偏移，并同时绘制直线，偏移后按规则1绘制直线。
#
# 指令的格式为X offsetY，表示在横坐标X沿纵坐标方向偏移，offsetY为正数表示正向偏移，为负数表示负向偏移。
#
# 给定了横坐标终点值E、以及若干条绘制指令，请计算绘制的直线和横坐标轴、以及 X=E 的直线组成图形的面积。
#
# 输入
# 首行为两个整数 N E，表示有N条指令，机器运行的横坐标终点值E。
#
# 接下来N行，每行两个整数表示一条绘制指令X offsetY，用例保证横坐标X以递增排序方式出现，且不会出现相同横坐标X。
#
# 取值范围:0 < N <= 10000, 0 <= X <= E <= 20000, -10000 <= offsetY <= 10000。
#
# 输出
# 一个整数，表示计算得到的面积，用例保证，结果范围在0~4294967295内
# 样例输入 复制
# 4 10
# 1 1
# 2 1
# 3 1
# 4 -2
# 样例输出 复制
# 12
#输入处理
N, E = map(int, input().split())
instructions = [map(int, input().split()) for _ in range(N)]
def solve(N, E, instructions):
    pre_x = 0
    pre_y = 0
    area = 0
    for x, offsetY in instructions:
        area += (x - pre_x)*abs(pre_y)
        pre_x = x
        pre_y += offsetY
    area += (E - pre_x)*abs(pre_y)
    return area
print(solve(N, E, instructions))