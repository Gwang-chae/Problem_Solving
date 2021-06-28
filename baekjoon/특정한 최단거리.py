# 문제
# https://www.acmicpc.net/problem/1504

# IDEA
# 플로이드 워셜 알고리즘으로 노드간 최단 거리를 구한 후
# 조건에 맞는 경우 중 최소값을 출력 -> 시간초과로 실패
# 다익스트라 알고리즘으로 필요 정보만 출력

# 다익스트라 알고리즘 구현 이후에도 예외를 처리 못해 한번 실패...
# 변수의 조건을 꼼꼼히 읽어보자!

## 시간초과
import sys

input = sys.stdin.readline
n,e = map(int, input().split())
INF = 1e9

# 모든 노드에서 다른 노드까지의 최단 거리를 구하기 위해
# 2차원 리스트로 표현, 모든 값을 INF 값으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: 
            graph[i][j] == 0

# 간선에 대한 정보를 입력받아, 그 값으로 테이블 초기화
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

# a노드에서 b노드까지의 최단 거리를 D_ab, 거쳐가는 노드를 k라고 하면,
# D_ab = min(D_ab, D_ak + D_kb)
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 문제에서 거쳐가야 하는 서로 다른 두점 v1, v2
v1, v2 = map(int, input().split())

# v1, v2를 거쳐가는 경우는
# 1 -> v1 -> v2 -> n, 1-> v2 -> v1 -> n 이 2가지 경우뿐
# 플로이드 워셜 알고리즘으로 한 노드에서 다른 노드까지의 최단 거리를 모두 구했으므로
# 각 경우에 맞게 값을 구한 후, 최소값을 출력
case1 = graph[1][v1] + graph[v1][v2] + graph[v2][n]
case2 = graph[1][v2] + graph[v2][v1] + graph[v1][n]
distance = min(case1, case2)
if distance == INF: print(-1)
else: print(distance)


## 다익스트라 알고리즘 이용
import sys
import heapq

input = sys.stdin.readline
n,e = map(int, input().split())
INF = 1e9

# 각 노드에 연결되어 있는 노드에 대한 정보를 담을 리스트 생성
graph = [[] for _ in range(n+1)]

for _ in range(e):
    # a에서 b로 가는 비용이 c
    a,b,c, = map(int, input().split())
    # 양방향이라는 조건을 충족시키기 위해
    # graph[a], gragp[b]에 각각 (도착노드, 비용)순으로 삽입
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    # 최단 거리 테이블을 모두 INF로 초기화
    distance = [INF] * (n+1)
    queue = []
    # (비용, 출발노드)쌍으로 힙에 삽입
    # 힙은 비용에 따른 최소 힙으로 구현
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)
        # 해당 노드를 방문한 적이 있는 경우 continue
        if distance[now] < dist:
            continue
        # 해당 노드와 연결된 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 만약 현재 노드를 거쳐 다른 노드로 가는 거리가 짧은 경우
            # 거쳐간 값으로 최단 거리를 변경하고 거리값과 해당 노드를 큐에 삽입
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    return distance

# 1, v1, v2에서 출발할 경우의 distance값 추출
v1,v2 = map(int, input().split())
start_one = dijkstra(1)
start_v1 = dijkstra(v1)
start_v2 = dijkstra(v2)

# 예외 처리
# v1은 1이, v2는 n이 될 수 있음
if v1 == 1 and v2 == n:
    answer = start_one[n]
elif v1 == 1:
    answer = start_v1[v2] + start_v2[n]
elif v2 == n:
    answer = start_one[v1] + start_v1[n]
# 1에서 v1, v2를 거쳐 n으로 가는 경우는 2가지
# 2가지 경우 중 최소 값이 답
else:
    case1 = start_one[v1] + start_v1[v2] + start_v2[n]
    case2 = start_one[v2] + start_v2[v1] + start_v1[n]
    answer = min(case1, case2)

# 1에서 n까지 v1,v2를 거쳐 가는 경우가 없으면 -1 출력
if answer < INF: print(answer)
else: print(-1)

