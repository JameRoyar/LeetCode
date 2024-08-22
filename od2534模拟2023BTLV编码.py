# 2534: 【模拟】2023B-TLV编码
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：13
# 解决：7
# 题目描述
# TLV 编码是按 TagLengthValue 格式进行编码的。
# 一段码流中的信元用 tag 标识，tag 在码流中唯一不重复，length 表示信元 value 的长度，value 表示信元的值，码流以某信元的 tag 开头，tag固定占一个字节，length固定占两个字节，字节序为小端序。
# 现给定 TLV 格式编码的码流以及需要解码的信元 tag，请输出该信元的value。
# 输入码流的 16 进制字符中，不包括小写字母；且要求输出的 16 进制字符串中也不要包含小写字母；码流字符串的最大长度不超过 50000 个字节。
# 输入
# 第一行为第一个字符串 ，表示待解码信元的 tag；输入第二行为一个字符串， 表示待解码的 16 进制码流；字节之间用 空格 分割。
# 输出
# 输出一个字符串，表示待解码信元以 16 进制表示的 value。
# 样例输入 复制
# 31
# 32 01 00 AE 90 02 00 01 02 30 03 00 AB 32 31 31 02 00 32 33 33 01 00 CC
# 样例输出 复制
# 32 33

import sys
import sys

def process_ltv_solution(tag, tlv_stream):
    i = 0
    while i < len(tlv_stream):
        # 获取当前的Tag
        tag_tmp = tlv_stream[i]

        # 获取长度信息
        length_str = tlv_stream[i + 2] + tlv_stream[i + 1]
        length = int(length_str, 16)

        # 如果找到匹配的Tag
        if tag_tmp == tag:
            output_list = []
            for j in range(length):
                output_list.append(tlv_stream[i + j + 3])
            print(" ".join(output_list))
            return

        # 没有找到匹配的Tag，跳过当前Tag
        i += 3 + length

if __name__ == "__main__":
    # 读取输入
    input = sys.stdin.read()
    lines = input.split('\n')

    tag = lines[0].strip()
    tlv_stream = lines[1].strip().split()

    process_ltv_solution(tag, tlv_stream)
