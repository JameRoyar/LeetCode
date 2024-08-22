# 3512: 【DFS/BFS】2024D-二叉树的广度优先遍历
# 内存限制：128 MB
# 时间限制：2.000 S
# 评测方式：文本比较
# 命题人：外部导入
# 提交：78
# 解决：58
# 题目描述
# 有一棵二叉树，每个节点由一个大写字母标识（最多26个节点），现有两组字母，分别表示后序遍历 (左孩子->右孩子->父节点) 和中序遍历 (左孩子->父节点->右孩子) 的结果，请输出层次遍历的结果。
# 输入
# 输入为两个字符串，分别是二叉树的后序遍历和中序遍历结果
# 输出
# 输出二叉树的层次遍历结果
# 样例输入 复制
# CBEFDA CBAEDF
# 样例输出 复制
# ABDCEF
# 提示
# 二叉树为
#     A
#    / \
#   B   D
#  /   / \
# C   E   F
# 来源/分类
# 树 DFS BFS 2024D 华为OD真题-200分
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

# input
# back, mid = input().split()
back = 'CBEFDA'
mid = 'CBAEDF'

# 构建二叉树
def buildTree(back, mid):
    if len(back) == 0:
        return None
    if len(back) != len(mid):
        return None
    root = TreeNode(back[-1])
    if len(back) == 1:
        return root
    mider = mid.index(back[-1])
    root.right = buildTree(back[mider:-1], mid[mider+1:])
    root.left = buildTree(back[:mider], mid[:mider])
    return root

def bfs(root):
    if root is None:
        return []
    queue = [root]
    res = []
    while len(queue) > 0:
        node = queue.pop(0)
        res.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return res


root = buildTree(back, mid)
print(''.join(bfs(root)))