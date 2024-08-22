# 2580: 【系统设计】2023C-文件缓存系统
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：183
# 解决：62
# 题目描述
# 请设计一个文件缓存系统，该文件缓存系统可以指定缓存的最大值(单位为字节)。
#
# 文件缓存系统有两种操作：存储文件(put)和读取文件(get) 操作命令为put fileName fileSize或者get fileName
#
# 存储文件是把文件放入文件缓存系统中；读取文件是从文件缓存系统中访问已存在的文件，如果文件不存在，则不作任何操作。
#
# 当缓存空间不足以存放新的文件时，根据规则删除文件，直到剩余空间满足新的文件大小为止，再存放新文件。
#
# 具体的删除规则为：文件访问过后，会更新文件的最近访问时间和总的访问次数，当缓存不够时，按照第一优先顺序为访问次数从少到多，第二顺序为时间从老到新的方式来删除文件。
#
# 输入
# 第一行为缓存最大值m(整数，取值范围为0 < m <= 52428800)
#
# 第二行为文件操作序列个数n(0 <= n <= 300000）
#
# 从第三行起为文件操作序列，每个序列单独一行
#
# 文件操作定义为"op fileName fileSize" fileName是文件名，fileSize是文件大小
#
# 输出
# 输出当前文件缓存中的文件名列表，文件名用英文逗号分隔，按字典顺序排序
#
# 如：a,c
#
# 如果文件缓存中没有文件，则输出NONE
#
# 样例输入 复制
# 50
# 6
# put a 10
# put b 20
# get a
# get a
# get b
# put c 30
# 样例输出 复制
# a,c
# 提示
# 1. 如果新文件的文件名和文件缓存中已有的文件名相同，则不会放在缓存中
#
# 2. 新的文件第一次存入到文件缓存中时，文件的总访问次数不会变化，文件的最近访问时间会更新到最新时间
#
# 3. 每次文件访问后，总访问次数加1，最近访问时间更新到最新时间
#
# 4. 任何两个文件的最近访问时间不会重复
#
# 5. 文件名不会为空，均为小写字母，最大长度为10
#
# 6. 缓存空间不足时，不能存放新文件
#
# 7. 每个文件大小都是大于0的整数

capacity = int(input())
n = int(input())
cache = {}
curSize = 0
for i in range(n):
    ops = input().split()
    if ops[0] == "put":
        name, size = ops[1], int(ops[2])
        if name in cache:
            continue
        if size > capacity:
            continue
        while curSize + size > capacity:
            delName = min(cache.keys(), key=lambda k: (cache[k][0], cache[k][1]))
            delSize = cache[delName][2]
            del cache[delName]
            curSize -= delSize
        cache[name] = [0, i, size]
        curSize += size
    elif ops[0] == "get":
        name = ops[1]
        if name not in cache:
            continue
        cache[name][0] += 1

ans = sorted(cache.keys())
print(",".join(ans)) if ans else print("NONE")

# # 输入文件缓存系统的容量
# maxSize = int(input())
# # 输入操作个数
# N = int(input())
# # 构建表示文件缓存系统的哈希表
# # 其中key为
# dic = dict()
# # 当前系统的大小
# curSize = 0

# # 遍历N次，其中每一次操作都对应时间time
# for time in range(N):
#     ops = input().split()
#     # 插入操作
#     if ops[0] == "put":
#         fileName, fileSize = ops[1], int(ops[2])
#         # 如果文件名已经存在，则直接跳过
#         if fileName in dic:
#             continue
#         # 如果文件本身的大小已经超过了最大容量，则直接跳过
#         if fileSize > maxSize:
#             continue
#         # 如果剩余空间不足，则持续删除文件
#         while maxSize - curSize < fileSize:
#             # 优先删除访问次数最少的，其次删除最近一次访问的时间最早的
#             delFileName = min(dic.keys(), key=lambda k: (dic[k][0], dic[k][1]))
#             delFileSize = dic[delFileName][2]
#             del dic[delFileName]
#             curSize -= delFileSize
#
#         # 将新文件加入哈希表中，key为文件名，value为[访问次数，最近访问时间，文件大小]所构成的三元组
#         dic[fileName] = [0, time, fileSize]
#         curSize += fileSize
#
#     # 访问操作
#     elif ops[0] == "get":
#         fileName = ops[1]
#         # 如果文件不位于哈希表中，不做任何操作
#         if fileName not in dic:
#             continue
#         # 该文件的访问次数+1
#         dic[fileName][0] += 1
#
#
# # 操作了N次之后，查看哈希表中剩余哪些文件，排序后输出
# ans = sorted(dic.keys())
# print(",".join(ans)) if ans else print("NONE")
