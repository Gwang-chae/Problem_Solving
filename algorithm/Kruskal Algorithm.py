# 특정 원소(x)가 속한 집합 찾기(find)
def find_parent(parent, x):
    # 루트 노드가 아니라면, 찾을 때까지 재귀 호출    
    if parent[x] !=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기(union)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수 v, union 연산을 위한 간선의 개수 e 입력
v,e = map(int, input().split())
# 부모 노드 테이블 생성
parent = [0] * (v+1)

# 부모 노드 테이블을 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 간선 정보를 담을 edges 리스트 생성
edges = []

for _ in range(e):
    # 노드 a,b와 a,b 사이의 거리값 cost
    a,b,cost = map(int, input().split())
    # 거리값(비용)순으로 정렬하기 위해 
    # cost를 앞에 둔 튜플로 edges에 정보 입력
    edges.append((cost, a, b))

# 거리값(비용)순으로 정렬
edges.sort()

# 최종 비용 산정을 위한 변수 result
result = 0

for edge in edges:
    cost, a, b = edge
    # cycle이 발생하지 않은 경우(부모 노드가 같지 않은 경우)
    # 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)