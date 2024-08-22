import collections


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        A, B = collections.defaultdict(int), collections.defaultdict(int)
        for c in s:
            A[c] += 1
        for c in t:
            B[c] += 1
        list_A = [v for v in A.values()]
        list_B = [v for v in B.values()]
        if sorted(list_A) == sorted(list_B): return True
        return False


A = Solution()
print(A.isIsomorphic("egg", "add"))
