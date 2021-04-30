# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12978

# IDEA
# 1번 마을에서 출발하여 k 이내로 갈 수 있는 모든 마을의 수를 구하는 문제
# 1번 마을에서 출발해 각 마을까지의 최단거리들을 구한 후 조건에 맞는 마을 수 도출 -> 다익스트라
# 중요한 점은 각 마을의 노드 정보를 입력해줘야 한다는 점. a -> b, b-> c 정보를 모두 graph에 입력

import heapq

def solution(N, road, K):
    INF = 1e9
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)
    
    for i in road:
        a,b,c = i[0], i[1], i[2]
        graph[a].append((b,c))
        graph[b].append((a,c))
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    answer = [x for x in distance if x <= K]
    return len(answer)