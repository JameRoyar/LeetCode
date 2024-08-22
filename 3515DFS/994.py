class Solution:
    @staticmethod
    def orangesRotting(grid: list[list[int]]) -> int:
        ans = -1
        q = []
        fresh = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: fresh += 1
                if grid[i][j] == 2: q.append((i, j))
        while q:
            ans += 1
            i, j = q.pop(0)
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                fresh -= 1
                grid[i][j] = 2
                q += [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        return -1 if fresh else max(ans, 0)


grids = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
s = Solution()
print(s.orangesRotting(grids))
