
def LongestSqu(s):
    ans = -1
    left, right = 0, 0
    numCot, alpCont = 0, 0

    while right < len(s) and left <= right:

        if s[right].isdigit():
            numCot += 1
        else:
            alpCont += 1

        if numCot >= 1 and alpCont == 1:
            ans = max(ans, right - left)

        while alpCont > 1:
            if s[left].isdigit():
                numCot -= 1
            else:
                alpCont -= 1
            left += 1

        right += 1

    return ans

s = "abC124ACb"
print(int(LongestSqu(s)))