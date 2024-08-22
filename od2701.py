# k = input()
# boxs = list(input().split())

key = "abc"
boxs = ["s,sdf134", "A2c4b"]


def findKey(key, boxs):
    key = sorted(key)
    for i in range(len(boxs)):
        box = boxs[i]
        k = 0
        box = sorted(box.lower())
        for j in range(len(box)):
            if box[j] == key[k]:
                k += 1
            if k == len(key):
                return i + 1
    return -1


print(findKey(key, boxs))

# ========[test_1.out]=========
# Expected						      |	Yours
# 243							      \	20
#
# ==============================
# ========[test_10.out]=========
# Expected						      |	Yours
# -1
# 							      |	1
#
# ==============================
# ========[test_12.out]=========
# Expected						      |	Yours
# 512							      \	16
#
# ==============================
# ========[test_13.out]=========
# Expected						      |	Yours
# 204							      \	16
#
# ==============================
# ========[test_15.out]=========
# Expected						      |	Yours
# 138							      \	2
#
# ==============================
# time_space_table:
# /2701/sample.in:AC mem=16340k time=30ms
# /2701/test_1.in:WA mem=16340k time=30ms
# /2701/test_10.in:WA mem=16496k time=30ms
# /2701/test_11.in:AC mem=16496k time=36ms
# /2701/test_12.in:WA mem=16496k time=30ms
# /2701/test_13.in:WA mem=16496k time=31ms
# /2701/test_14.in:AC mem=16496k time=33ms
# /2701/test_15.in:WA mem=16496k time=32ms
# /2701/test_16.in:AC mem=16496k time=32ms
# /2701/test_17.in:AC mem=16496k time=38ms
# /2701/test_18.in:AC mem=16496k time=36ms
# /2701/test_19.in:AC mem=16496k time=37ms
# /2701/test_2.in:AC mem=16496k time=33ms
# /2701/test_3.in:AC mem=16496k time=37ms
# /2701/test_4.in:AC mem=16496k time=37ms
# /2701/test_5.in:AC mem=16496k time=37ms
# /2701/test_6.in:AC mem=16496k time=33ms
# /2701/test_7.in:AC mem=16496k time=33ms
# /2701/test_8.in:AC mem=16496k time=33ms
# /2701/test_9.in:AC mem=16496k time=36ms

