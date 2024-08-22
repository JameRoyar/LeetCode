# 滑动窗口算法框架
def slidingWindow(s: str):
    # 用合适的数据结构记录窗口中的数据，根据具体场景变通
    # 比如说，我想记录窗口中元素出现的次数，就用 map
    # 我想记录窗口中的元素和，就用 int
    window = dict()

    left = 0
    right = 0
    while right < len(s):
        # c 是将移入窗口的字符
        c = s[right]
        window[c] = window.get(c, 0) + 1
        # 增大窗口
        right += 1
        # 进行窗口内数据的一系列更新
        # ...

        # /*** debug 输出的位置 ***/
        # 注意在最终的解法代码中不要 print
        # 因为 IO 操作很耗时，可能导致超时
        # print(f"window: [{left}, {right})")
        # /********************/

        # 判断左侧窗口是否要收缩
        while left < right and "window needs shrink":
            # d 是将移出窗口的字符
            d = s[left]
            window[d] -= 1
            if window[d] == 0:
                del window[d]
            # 缩小窗口
            left += 1
            # 进行窗口内数据的一系列更新
            # ...
