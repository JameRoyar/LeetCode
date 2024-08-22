# ### [#2手撕代码-coding：字符统计及重排](#2手撕代码-coding：字符统计及重排)2. 手撕代码 coding：字符统计及重排
#
# > 【字符统计及重排】给出一个仅包含字母的字符串，不包含空格，统计字符串中各个字母 (区分大小写) 出现的次数，并按照字母出现次数从大到小的顺序输出各个字母及
# 其出现次数。如果次数相同，按照自然顺序进行排序，且小写字母在大写字母之前。
#  输入描述:
#  输入一行，为一个仅包含字母的字符串。
#  输出描述:
#  按照字母出现次数从大到小的顺序输出各个字母和字母次数，用英文分号分隔，注意末尾的分号; 字母和次数间用英文冒号分隔。
#  示例 1:
#  输入
#  xyxyXX
#  输出
#  x:2;y:2;X:2;
#
# from collections import Counter
#
# s = input()
#
# # dic = Counter(s)
# dic = {}
# for i in s:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
#
# dic = sorted(dic.items(), key=lambda x: (x[1], x[0]), reverse=True)
#
# for i in dic:
#     print(i[0] + ":" + str(i[1]) + ";", end="")

def char_count_and_sort(text):
    """
    Counts the occurrences of each character in a string and sorts them by frequency and then alphabetically.

    Args:
        text: A string containing only letters (no spaces).

    Returns:
        A string representing the character counts and sorted order, separated by semicolons.
    """

    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Sort by count (descending) and then by character (ascending)
    sorted_counts = sorted(char_counts.items(),
                           key=lambda x: (-x[1], ord(x[0]) if ord(x[0]) > ord("a") else (ord(x[0]) + 64)))
    print("".join(f"{char},{num};" for char, num in sorted_counts))
    return sorted_counts

    # Build the output string
    # output = ""
    # for char, count in sorted_counts:
    #   output += f"{char}:{count};"
    #
    # return output  # Remove trailing semicolon


# Example usage (no need for input)
text = "xyxyXX"
result = char_count_and_sort(text)
print(result)  # Output: x:2;y:2;X:2;
