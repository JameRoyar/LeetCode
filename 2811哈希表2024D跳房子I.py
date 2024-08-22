arr = list(map(int,input()[1:-1].split(",")))
cot = int(input())
min_idx = 2*len(arr)
hash  = dict()
ans = [0,0]
for i in range(len(arr)):
    if arr[i] in hash:
        if min_idx > hash[arr[i]]+i:
            min_idx = hash[arr[i]]+i
            ans = [cot-arr[i],arr[i]]
    elif arr[i] not in hash:
        hash[cot-arr[i]] = i
print(f"[{ans[0]},{ans[1]}]")