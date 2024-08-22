class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, len(numbers) - 1
        while i != j:
            sum = numbers[i] + numbers[j]
            if sum == target: return [i, j]
            if sum > target:
                j -= 1
            else:
                i += 1
        return [i, j]

a = Solution()
print(a.twoSum([1, 2, 3, 4, 5, 7, 11, 15], 9))