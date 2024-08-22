class Solution:
    Mapping = ["", "", 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', "wxyz"]

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits: return []
        ans = []
        path = []

        def backtrack(i):
            if len(path) == len(digits):
                ans.append("".join(path.copy()))
                return
            for c in self.Mapping[int(digits[i])]:
                path.append(c)
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return ans
