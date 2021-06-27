# 문제
# https://www.acmicpc.net/problem/7569

# IDEA
# BFS 구현
# x,y축 외에도 z축까지 고려 -> 상하좌우 외에도 앞뒤까지 고려
# 출발지점이 여러개이기 때문에 출발지점들을 먼저 queue에 넣어준 후 BFS 시행

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
m, n, h = map(int, input().split())

graph = [[] * x for x in range(h)]
for i in range(h):
    for _ in range(n):
        graph[i].append(list(map(int, input().split())))

# 상하좌우앞뒤 변화량
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque([])

# 익은 토마토(1)가 있는 자리를 queue에 삽입
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))

# bfs 구현
def bfs(queue):
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz, nx, ny))

bfs(queue)
box = [element for sub1 in graph for sub2 in sub1 for element in sub2]
if 0 in box: print(-1)
else: print(max(box) - 1)