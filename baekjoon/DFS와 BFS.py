# 문제
# https://www.acmicpc.net/problem/1260

# IDEA
# DFS와 BFS를 각각 정의에 맞게 구현

import sys
from collections import deque

input = sys.stdin.readline
# 노드 수 n, 간선 수 m, 시작 노드 v
n, m, v = map(int, input().split())

# 노드 간 연결을 표현하기 위한 graph 생성
# 인덱스 시작이 0부터이므로 편의를 위해 n+1로 구현
graph = [[0] * (n+1) for _ in range(n+1)]
# 방문 처리를 기록할 visited 리스트 생성
visited = [False] * (n+1)

# 양방향에 맞춰 각 간선 정보 입력
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1

# dfs 구현
def dfs(graph, v, visited):
    print(v, end=' ')
    visited[v] = True
    for i in range(1, n+1):
        # 해당 노드와 연결되어 있고 방문한 적이 없으면
        if graph[v][i] == 1 and visited[i] == False:
            # 해당 노드에서 dfs 실행
            dfs(graph, i, visited)

# bfs 구현
def bfs(graph, v, visited):
    visited[v] = True
    queue = deque([v])

    # 큐가 빌 때까지
    while queue:
        # 첫 원소 pop
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            # 해당 노드와 연결되어 있고 방문한 적이 없으면
            if graph[v][i] == 1 and visited[i] == False:
                # 큐에 삽입 후 방문 처리
                queue.append(i)
                visited[i] = True

dfs(graph, v, visited)
# 방문 리스트를 초기화하여 bfs 진행
visited = [False] * (n+1)
print()
bfs(graph, v, visited)