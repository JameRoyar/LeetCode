from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n, m = len(matrix[0]), len(matrix)
        up = 0
        left = 0
        down = m - 1
        right = n - 1
        while len(ans) < m * n:
            if down >= up:
                for i in range(left, right + 1):
                    ans.append(matrix[up][i])
                    up += 1
            if right >= left:
                for j in range(up, down + 1):
                    ans.append(matrix[j][right])
                    right -= 1
            if down >= up:
                for k in range(right, left - 1, -1):
                    ans.append(matrix[down][k])
                    down -= 1
            if right >= left:
                for l in range(down, up - 1, -1):
                    ans.append(matrix[l][left])
                    left += 1
        return ans
