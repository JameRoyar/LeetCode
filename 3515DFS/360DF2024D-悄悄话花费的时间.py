# 题目描述
# 给定一个二叉树，每个节点上站着一个人，节点数字表示父节点到该节点传递悄悄话需要花费的时间。
#
# 初始时，根节点所在位置的人有一个悄悄话想要传递给其他人，求二叉树所有节点上的人都接收到悄悄话花费的时间。
#
# 输入
# 给定一个数组表示二叉树，-1 表示空节点
# 输出
# 返回所有节点都接收到悄悄话花费的时间
# 样例输入 复制
# 0 9 20 -1 -1 15 7 -1 -1 -1 -1 3 2
# 样例输出 复制
# 38
# DP 树 DFS 2024D 华为OD真题-200分
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minTimeToVisitAllNodes(self, nodes: list[int]) -> int:
        # 构建二叉树
        root = self.buildTree(nodes, 0)
        # 使用DFS计算时间
        return self.dfs(root)

    def buildTree(self, nodes, index: int) -> TreeNode:
        if index >= len(nodes) or nodes[index] == -1:
            return None
        node = TreeNode(nodes[index])
        node.left = self.buildTree(nodes, 2 * index + 1)
        node.right = self.buildTree(nodes, 2 * index + 2)
        return node

    def dfs(self, node: TreeNode) -> int:
        if not node:
            return 0
            # 更新当前节点的时间
        # 递归计算左右子树的最大时间
        left_time = self.dfs(node.left)
        right_time = self.dfs(node.right)
        # 取左右子树的最大时间作为当前子树的最大时间
        return max(left_time, right_time) + node.val

# 测试
solution = Solution()
nodes = list(map(int, input().split()))
print(solution.minTimeToVisitAllNodes(nodes))  # 输出应为38
