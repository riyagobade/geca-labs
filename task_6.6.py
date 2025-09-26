def kruskal_mst_adjlist(edges, V):
    edges_sorted = sorted(edges, key=lambda x: x[2])
    parent = [i for i in range(V)]

    def find(x):
        if parent[x] == x:
            return x
        return find(parent[x])

    def union(x, y):
        xroot = find(x)
        yroot = find(y)
        if xroot != yroot:
            parent[yroot] = xroot

    mst_edges = []
    for u, v, w in edges_sorted:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, w))

    adjlist = {i: [] for i in range(V)}
    for u, v, w in mst_edges:
        adjlist[u].append(v)
        adjlist[v].append(u)

    return mst_edges, adjlist

edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
V = 4
mst_edges, adjlist = kruskal_mst_adjlist(edges, V)
print("MST edges:", mst_edges)
print("Adjacency list:")
for k, v in adjlist.items():
    print(f"{k}: {v}")
