# 这是一个二叉树的最小深度的解法，该解法使用了深度优先搜索（DFS）和队列。下面是加上中文注释后的代码：
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def minDepth(self, root) -> int:
        # 空树，深度为 0
        if root is None:
            return 0
        # 初始化队列和层次
        queue = [root]
        depth = 1
        # 当队列不为空
        while queue:
            # 当前层的节点数
            n = len(queue)
            # 弹出当前层的所有节点，并将所有子节点入队列
            for i in range(n):
                node = queue.pop(0)
                # 最早出现左右节点都为空，证明为叶子节点，即为二叉树的最小高度
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1

        return depth


import unittest


class TestMinDepth(unittest.TestCase):
    def test_empty_tree(self):
        root = None
        depth = 0
        self.assertEqual(TreeNode.minDepth(root), depth)

    def test_single_node_tree(self):
        root = TreeNode(1)
        depth = 1
        self.assertEqual(TreeNode.minDepth(root), depth)

    def test_left_child_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        depth = 2
        self.assertEqual(TreeNode.minDepth(root), depth)

    def test_right_child_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        depth = 2
        self.assertEqual(TreeNode.minDepth(root), depth)

    def test_left_right_child_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        depth = 2
        self.assertEqual(TreeNode.minDepth(root), depth)

    def test_right_left_child_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.left = TreeNode(3)
        depth = 2
        self.assertEqual(TreeNode.minDepth(root), depth)

    def test_left_right_child_tree_2(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        depth = 2
        self.assertEqual(root.minDepth(root), depth)

    def test_right_left_child_tree_2(self):
        root = TreeNode(2)
        root.right = TreeNode(1)
        root.left = TreeNode(3)
        depth = 2
        self.assertEqual(TreeNode.minDepth(root), depth)
