arr = input()

def result(arr):
    correct = 0
    for i in range(len(arr)):
        fault = int(arr[i])
        if fault > 4:
            fault -= 1
        for j in range(len(arr) - i - 1, 0, -1):
            fault *= 9
        correct += fault
    return correct
print(result(arr))