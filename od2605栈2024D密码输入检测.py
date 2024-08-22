# 2605: 【栈】2024D-密码输入检测
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：664
# 解决：209
# 题目描述
# 给定用户密码输入流 input，输入流中字符'<'表示退格，可以清除前一个输入的字符，请你编写程序，输出最终得到的密码字符，并判断密码是否满足如下的密码安全要求。 密码安全要求如下：
#
# 1. 密码长度>=8;
#
# 2. 密码至少需要包含 1 个大写字母;
#
# 3. 密码至少需要包含 1 个小写字母;
#
# 4. 密码至少需要包含 1 个数字;
#
# 5. 密码至少需要包含 1 个字母和数字以外的非空白特殊字符
#
# 注意空串退格后仍然为空串，且用户输入的字符串不包含'<'字符和空白字符。
#
# 输入
# 用一行字符串表示输入的用户数据，输入的字符串中'<'字符标识退格，用户输入的字符串不包含空白字符，例如：ABC
# 输出
# 输出经过程序处理后，输出的实际密码字符串，并输出改密码字符串是否满足密码安全要求。两者间由','分隔， 例如：ABc89%00,true
# 样例输入 复制
# ABC<c89%000<
# 样例输出 复制
# ABc89%00,true
# 来源/分类
# 模拟 栈 华为OD真题-100分

s = input()
stack = list()
# 遍历字符串s中的每一个字符ch
for ch in s:
    # 如果不是退格，则直接入栈
    if ch != "<":
        stack.append(ch)
    # 如果遇到退格，且栈不为空栈，弹出栈顶元素表示退格
    elif ch == "<" and len(stack) > 0:
        stack.pop()

# 重新合并栈中的所有元素，得到处理后的字符串s_new
s_new = "".join(stack)

# 对字符串s_new进行每一个条件的判断
# 判断1：长度是否大于等于8
flag1 = len(s_new) >= 8
# 判断2：是否存在大写字符
flag2 = any(ch.isupper() for ch in s_new)
# 判断3：是否存在小写字符
flag3 = any(ch.islower() for ch in s_new)
# 判断4：是否存在数字
flag4 = any(ch.isdigit() for ch in s_new)
# 判断5：是否存在除了字符串、数字、空格之外的特殊字符
flag5 = any(not ch.isalnum() and not ch.isspace() for ch in s_new)

# 若上述五个条件均为True，则输出字符串和true
if flag1 and flag2 and flag3 and flag4 and flag5:
    print(f"{s_new},true")
# 否则输出字符串和false
else:
    print(f"{s_new},false")