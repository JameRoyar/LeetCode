s = "ferga13fdsf3(100,200)f2r3rfasf(300,400)"


def maxTrack(s):
    maxDis = 0
    left = 0
    coord = "(0,0)"
    for i in range(len(s)):
        if s[i] == "(":
            left = i + 1
            continue
        if s[i] == ")":
            m, n = s[left:i].split(",")
            x, y = int(m), int(n)
            if not ((0 < x < 1000) and (0 < y < 1000)):
                continue
            if m[0] == "0" or n[0] == "0":
                continue
            distance = x * x + y * y
            if distance > maxDis:
                maxDis = distance
                coord = "(" + m + "," + n + ")"
    return coord


print(maxTrack(s))
