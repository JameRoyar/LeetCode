# 94. 二叉树的中序遍历
# 已解答
# 简单
# 相关标签
# 相关企业
# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ans = []
#
#         def dfs(root, ans):
#             if not root:
#                 return root
#             dfs(root.left, ans)
#             ans.append(root.val)
#             dfs(root.right, ans)
#
#         dfs(root, ans)
#         return ans
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorderTraversal(self, root):
        # core method is move the root and its right tree to the left child s rightest s
        ans = []
        pre = None
        while root:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root
                # remove link of root
                tmp = root
                root = root.left
                tmp.left = None
            else:
                ans.append(root.val)
                root = root.right
        return ans


class Solution:
    def inorderTraversal(self, root):
        #core method is move the root and its right tree to the left child s rightest s
        ans = []
        pre = None
        while root:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root
                #remove link of root
                tmp = root
                root = root.left
                tmp.left = None
            else:
                ans.append(root.val)
                root = root.right
        return ans

    import unittest


class TestInorderTraversal(unittest.TestCase):
    def setUp(self):
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(4)
        self.root.left.right = TreeNode(5)
        self.root.right.right = TreeNode(6)

    def test_empty_tree(self):
        tree = TreeNode(None)
        self.assertEqual(tree.inorderTraversal(tree), [])

    def test_one_node_tree(self):
        tree = TreeNode(1)
        self.assertEqual(tree.inorderTraversal(tree), [1])

    def test_one_leaf_node_tree(self):
        tree = TreeNode(1)
        tree.left = TreeNode(2)
        tree.right = TreeNode(3)
        self.assertEqual(tree.inorderTraversal(tree), [2, 1, 3])

    def test_normal_tree(self):
        self.assertEqual(self.root.inorderTraversal(self.root), [4, 2, 5, 1, 3, 6])