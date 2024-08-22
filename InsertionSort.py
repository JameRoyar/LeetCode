# 插入排序
# 插入排序空间复杂度

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr


if __name__ == '__main__':
    arr = [11, 24, 33, 4, 52, 6, 27, 8, 94, 102]
    print(insertionSort(arr))
