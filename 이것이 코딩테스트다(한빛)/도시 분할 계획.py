import sys

input = sys.stdin.readline

n,m = map(int, input().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

edges = []
for _ in range(m):
    a,b,cost = map(int, input().split())
    edges.append((cost, a, b))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges.sort()
result = 0

for edge in edges:
    cost,a,b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        # 최소 비용으로 최소 신장 트리를 2개로 나누는 방법은
        # 최소 신장 트리에서 비용이 가장 큰 값을 제거하는 것
        # 따라서 최소 신장 트리에서 마지막으로 들어오는 cost를 빼주면 됨
        last = cost

print(result - last)