#lst = list(map(int, input().split(",")))
#s = int(input())

def TheLongestAimSequene(lst, s):
    ans = -1
    left, right = 0, 0
    sum = 0

    while left < right and right < len(lst):
        if sum < s:
            sum += lst[right]
            right += 1
        else:
            if sum == s: ans = max(ans, right - left)
            sum -= lst[left]
            left += 1
    return ans


lst = [1, 2, 3, 4, 2]
s = 6
ans = TheLongestAimSequene(lst, s)
print(int(ans))
