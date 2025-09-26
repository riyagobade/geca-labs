def kruskal_mst(edges, V):
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
    total_weight = 0

    for u, v, w in edges_sorted:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, w))
            total_weight += w

    return mst_edges, total_weight

edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
V = 4
mst_edges, mst_weight = kruskal_mst(edges, V)
print("MST edges:", mst_edges)
print("MST total weight:", mst_weight)
