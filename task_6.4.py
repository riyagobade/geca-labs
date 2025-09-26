def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if xroot != yroot:
        parent[yroot] = xroot

parent = [0, 1, 2, 3]
union(parent, 0, 1)
union(parent, 1, 2)

print("Find 2:", find(parent, 2))
print("Parent array:", parent)
