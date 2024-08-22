class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        i , j = 0 , k
        res = []
        m = 0
        if k >= len(nums):
            res.append(max(nums))
            return res
        while j <= len(nums):
            m = max(m,max(nums[i:j]))
            res.append(m)
            i += 1
            j = i + k
        return res

a = Solution()
print(a.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))