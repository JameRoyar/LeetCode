class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        path = []
        n = len(s)
        def dfs(i: int) -> None:
            if i == n:
                ans.append(path.copy())  # 复制 path
                return
            for j in range(i, n):  # 枚举子串的结束位置
                t = s[i: j + 1]
                if t == t[::-1]:  # 判断是否回文
                    path.append(t)
                    dfs(j + 1)
                    path.pop()  # 恢复现场
        dfs(0)
        return ans

s = "aab"
solution = Solution()
print(solution.partition(s))