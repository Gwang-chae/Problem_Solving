# 문제
# https://www.acmicpc.net/problem/2606

# IDEA
# DFS 구현
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
start = 1
# 방문 처리를 기록할 visited 리스트 생성
visited = [False] * (n+1)

# 노드 간 연결을 표현하기 위한 graph 생성
# 인덱스 시작이 0부터이므로 편의를 위해 n+1로 구현
graph = [[0] * (n+1) for _ in range(n+1)]

# 각 간선 정보 입력
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1

# dfs 구현
def dfs(graph, start, visited):
    visited[start] = True
    for i in range(1, n+1):
        # 해당 노드와 연결되어 있고 방문한 적이 없으면
        if graph[start][i] == 1 and visited[i] == False:
            # 해당 노드에서 dfs 실행
            dfs(graph, i, visited)

dfs(graph, start, visited)
# 시작 노드인 1번은 이미 count에 들어가지 않으므로
# visited의 summation값에서 -1
print(sum(visited) - 1)