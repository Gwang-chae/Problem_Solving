# 문제
# https://www.acmicpc.net/problem/9370

# IDEA
# 목적지 후보 중 g,h 사이의 도로를 지나는 목적지 후보를 출력하는 문제
# 다익스트라 알고리즘으로 출발점에서 특정 노드를 가는 최단 거리를 구함
# 출발지에서 목적지 후보로 가는 최단 거리를 dist1,
# 출발지에서 g, h를 각각 최단 거리로 방문한 후 목적지 후보까지 최단 거리로 갔을 때를 dist2라 한다면
# dist1 == dist2라면 g, h를 경유한 것이라 볼 수 있음
# 여기서 고려해야 할 것은 dist2가 될 수 있는 경우는 2가지
# case) 출발 -> g -> h -> 목적지 후보, 출발 -> h -> g -> 목적지 후보

import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n,m,t = map(int, input().split())
    s,g,h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        # a에서 b로 가는 비용이 c
        a,b,c = map(int, input().split())
        # 양방향 처리
        graph[a].append((b,c))
        graph[b].append((a,c))

    INF = 1e9

    def dijkstra(s):
        # 최단 거리 테이블을 INF로 초기화
        distance = [INF] * (n+1)
        queue = []
        heapq.heappush(queue, (0, s))
        # 출발지에서 자기 자신으로 가는 거리는 0
        distance[s] = 0

        while queue:
            dist, now = heapq.heappop(queue)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(queue, (cost, i[0]))
        return distance

    # s,g,h에서 출발할때 각각의 최단 거리 테이블
    start_s = dijkstra(s)
    start_g = dijkstra(g)
    start_h = dijkstra(h)

    answer = []
    for _ in range(t):
        destination = int(input())
        # 출발지에서 목적지 후보로 가는 경우 direct
        direct = start_s[destination]
        # 출발지에서 g,h를 거쳐 목적지 후보로 가는 경우 2가지
        case1 = start_s[g] + start_g[h] + start_h[destination]
        case2 = start_s[h] + start_h[g] + start_g[destination]
        # direct와 하나라도 같은 경우가 존재한다면
        # g,h를 거치면서 목적지 후보로 가는 것임
        if direct == case1 or direct == case2:
            answer.append(destination)

    # 오름차순 정렬 후 공백 분리, 출력
    answer.sort()
    for i in answer:
        print(i, end=' ')