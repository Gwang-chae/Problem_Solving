# 문제
# https://www.acmicpc.net/problem/11657

# IDEA
# 벨만-포드 알고리즘 구현

# 벨만-포드 알고리즘이란
# 매번 모든 간선을 확인하면서 특정 노드로부터 다른 노드로까지의
# 최단 거리를 구할 수 있는 알고리즘으로, 다익스트라보다는 오래 걸리지만
# 음수 간선 순환이 내부에 존재해도 이를 탐지해 낼 수 있다는 장점을 가짐

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
INF = 1e9

# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n+1)

graph = []
for _ in range(m):
    # a에서 b까지의 비용 c
    a,b,c = map(int, input().split())
    graph.append((a,b,c))

def bf(start):
    # 출발 지점의 최단거리를 0으로 갱신
    distance[start] = 0

    # 노드의 수만큼 과정 반복
    for i in range(n):
        # 모든 간선을 하나씩 확인
        for j in range(m):
            now = graph[j][0]
            next = graph[j][1]
            cost = graph[j][2]

            # 만약 현재 노드의 최단 거리가 INF가 아니고
            # 현재 노드를 지나 다음 노드로의 비용이 다음 노드에서의 최단 거리값보다 작다면 값을 갱신
            if distance[now] != INF and distance[next] > distance[now] + cost:
                distance[next] = distance[now] + cost

                # 음수 간선 순환 유무 확인
                # n라운드에도 값이 갱신된다면 음수 간선 순환이 존재
                if i == n -1:
                    return True
    return False

cycle = bf(1)

if cycle: print(-1)
else:
    for i in range(2, n+1):
        if distance[i] != INF: print(distance[i])
        else: print(-1)