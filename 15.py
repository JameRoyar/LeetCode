class Solution:
    def threeSum(self, nums):
        k = 0
        nums.sort()
        res = []
        while k < len(nums)-2 :
            if nums[k] > 0: return res
            if k > 0 and nums[k] == nums[k-1]:
                k += 1
                continue
            i,j= k+1,len(nums)-1
            while i < j :
                if nums[k] + nums[j] + nums[i] == 0 :
                    res.append([k,i,j])
                    j -= 1
                    i += 1
                    while i < j and nums[i] == nums[i+1]:i+=1
                    while i < j and nums[j] == nums[j-1]:j-=1
                if nums[k] + nums[j] + nums[i] < 0:
                    i += 1
                    while i < j and nums[i] == nums[i+1]:i+=1
                if nums[k] + nums[j] + nums[i] > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j-1]:j-=1
            k += 1
        return res

a = Solution()
print(a.threeSum([-1,0,1,-1]))