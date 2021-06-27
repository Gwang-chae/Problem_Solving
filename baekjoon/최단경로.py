# 문제
# https://www.acmicpc.net/problem/1753

# IDEA
# 다익스트라 알고리즘 구현
# sys는 maxsize 지원
import sys
import heapq

input = sys.stdin.readline
v,e = map(int, input().split())
k = int(input())
INF = sys.maxsize

# 각 노드에 연결되어 있는 노드에 대한 정보를 담은 리스트 생성
graph = [[] for _ in range(v+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (v+1)

for _ in range(e):
    # a번 노드에서 b번 노드까지의 비용이 c
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(k):
    # q에는 (거리, 노드)쌍으로 입력하여 거리에 따른 최소 힙을 구현
    queue = []
    heapq.heappush(queue, (0, k))
    # 시작 노드로 가기 위한 최단 경로는 0이므로 0 설정, q에 삽입
    distance[k] = 0

    while queue:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(queue)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            # 거쳐간 값으로 최단 거리를 변경
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else: print(distance[i])