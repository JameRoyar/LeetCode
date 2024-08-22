class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i , j =  0 , 1
        m = 0
        while j < len(s):
            if s[j] not in s[i:j]:
                j+=1
                m = max(m,len(s[i:j]))
                continue
            i += 1
        return m

a = Solution()
print(a.lengthOfLongestSubstring("abcabcbb"))