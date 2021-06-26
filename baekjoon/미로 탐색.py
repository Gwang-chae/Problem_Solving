# 문제
# https://www.acmicpc.net/problem/2178

# IDEA
# 시작점에서 끝점까지 최소 거리로 가는 경우 탐색
# BFS 구현, 상하좌우 중 가능한 경로 확인 후 거리값 기록

from collections import deque

n,m = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 그래프를 벗어나지 않는 범위에서 이동가능한 경우
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                # 이동가능하므로 현재 지점 값에 +1
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

# 문제의 출발 지점은 (1,1)이지만
# 인덱스 시작점은 (0,0)이므로 (0,0)에서 출발
bfs(0, 0)
# (n,m)까지의 거리 출력
print(graph[-1][-1])