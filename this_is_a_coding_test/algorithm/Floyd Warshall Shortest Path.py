import sys

input = sys.stdin.readline
INF = int(1e9)

# n은 노드의 개수, m은 간선의 개수
n,m = map(int, input().split())

# 모든 노드에서 다른 모든 노드까지의 최단 경로를 구하기 위해
# 2차원 리스트로 표현, 모든 값을 큰 수(무한)으로 초기화
graph = [[INF] * (n+1) for i in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 간선에 대한 정보를 입력받아, 그 값으로 테이블 초기화
for _ in range(m):
    # a번 노드에서 b번 노드까지의 비용이 c
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘
# a노드에서 b노드까지의 최단 거리를 D_ab, 거쳐가는 노드를 k라고 하면,
# D_ab = min(D_ab, D_ak + D_kb)
# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
            # 도달할 수 없는 경우, -1로 출력
            if graph[a][b] == INF:
                print(-1, end=" ")
            else:
                print(graph[a][b], end=" ") 
    print()