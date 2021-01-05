import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드 개수 n, 간선 개수 m, 시작 노드 start
n,m,start = map(int, input().split())
# 노드 연결 정보를 담는 2차원 리스트 생성
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 INF값으로 초기화
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    # a노드에서 b노드로 가는 값이 c
    # (도착 노드, 거리)쌍으로 a노드에 해당하는 graph 인덱스에 삽입
    graph[a].append((b,c))

print(graph)
def dijkstra(start):
    q = []
    # 시작 노드에서 시작 노드로 가는 값은 0이므로
    # 0으로 설정하여 q에 삽입, 최단 거리 또한 0으로 수정
    # q에는 (거리, 시작노드)쌍으로 삽입하여
    # 우선순위(거리 값이 작은 것 우선) q 생성
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 거리 값이 0으로 INF보다 작지만
# 문제에서는 제외해야 하므로 count -1
print(count-1, max_distance)