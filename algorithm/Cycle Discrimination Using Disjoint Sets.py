# 특정 원소(x)가 속한 집합 찾기(find)
def find_parent(parent, x):
    # 루트 노드가 아니라면, 찾을 때까지 재귀 호출    
    if parent[x] != x:
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

# cycle 여부 체크
cycle = False

for i in range(e):
    a,b = map(int, input().split())
    # cycle이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
   # cycle이 발생하지 않으면 union 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print('Cycle이 발생')
else:
    print('Cycle이 발생하지 않음')