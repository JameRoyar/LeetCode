# 给定长度为n的无序的数字数组，每个数字代表二叉树的叶子节点的权值，数字数组的值均大于等于1。
#
# 请完成一个函数，根据输入的数字数组,生成哈夫曼树，并将哈夫曼树按照中序遍历输出。
#
# 为了保证输出的二又树中序遍历结果统一，增加以下限制：二叉树节点中，左节点权值小于等于右节点权值，根节点权值为左右节点权值之和。当左右节点权值相同时，左子树高度高度小于等于右子树
#
# 注意：所有用例保证有效，并能生成哈夫曼树。
#
# 提醒：哈夫曼树又称最优二叉树，是一种带权路径长度最短的二又树。所谓树的带权路径长度，就是树中所有的叶结点的权值乘上其到根结点的路径长度（若根结点为0层，叶结点到根结点的路径长度为叶结点的层数）。
"""
第一行输入为数组长度，记为N，1<=N<=1000

第二行输入无序数值数组，以空格分割，数值均大于等于1，小于100000

输出
输出一个哈夫曼树的中序遍历的数组，数值间以空格分割
样例输入 复制
5
5 15 40 30 10
样例输出 复制
40 100 30 60 15 30 5 15 10
"""
# how to build a  huffman tree is get the most min two number in arr and sum them and put the sum in the new arr and delete the two number in the old arr
# input
n = int(input())
arr = list(map(int, input().split()))


# define huffman tree
class node:
    def __init__(self, val=0, left=None, right=None, lev=0):
        self.val = val
        self.left = left
        self.right = right
        self.lev = lev


# mid  order
def mid_order(root):
    if not root:
        return None
    mid_order(root.left)
    print(root.val, end=' ')
    mid_order(root.right)


# convey arr to node arr
for i in range(n):
    arr[i] = node(arr[i], None, None, 0)


# build huffman tree
def build_huffman_tree(arr):
    while len(arr) > 1:
        arr.sort(key=lambda x: (x.val, x.lev))
        father_val = arr[0].val + arr[1].val
        father_lev = max(arr[0].lev, arr[1].lev)
        father = node(father_val, arr[0], arr[1], father_lev)
        arr.pop(0)
        arr.pop(0)
        arr.append(father)

build_huffman_tree(arr)
mid_order(arr[0])
