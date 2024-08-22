map = [1, 2, 3, 4]
ans = []
path = []

def dfs(ans, path, map, idx):
    if len(path) == 2:
        ans.append(path[:])
        return
    for i in range(len(map)):
        path.append(map[i])
        dfs(ans, path, map, i + 1)
        path.pop()


for i in range(2):
    dfs(ans, path, map, 0)

print(ans)
