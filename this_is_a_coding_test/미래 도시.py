import sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
# 플로이드 워셜 알고리즘을 위한 graph 테이블 생성
graph = [[INF] * (n+1) for i in range(n+1)]

# 자기 자신에게로 가는 경로는 0으로 설정
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 문제에서 모든 간선의 길이는 1이고 서로 연결되어 있으므로
# 노드 a -> b, b -> a로 들어오는 값을 1로 설정
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 먼저 방문해야 하는 k, 마지막 방문지 x입력
x,k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 1번 노드에서 k를 방문하고 x에 도착하는 경로
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else :
    print(distance)