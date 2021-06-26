# 문제
# https://www.acmicpc.net/problem/7576

# IDEA
# BFS로 구현
# 출발지점이 여러개이기 때문에 출발지점들을 먼저 queue에 넣어준 후 BFS 시행
# 출발지점(1)에 날짜를 더해가며 구했기 때문에
# 토마토가 모두 익을 때까지의 최소 날짜는 max값에서 시작일 1을 빼줘야 함
# 박스 안에 안 익은 토마토가 있는 경우(0)가 존재하면 -1 출력

from collections import deque

m, n = map(int, input().split())
# 상하좌우 변화값 지정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# graph를 돌며 익은 토마토가 들어 있는 경우(1)를
# queue에 삽입
queue = deque([])
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

def bfs(queue):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # graph를 벗어나지 않는 범위에서 토마토가 안 익은 경우를 만나면
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                # 이전까지의 거리 정보 + 1
                graph[nx][ny] += graph[x][y] + 1
                queue.append((nx, ny))
bfs(queue)

# graph를 flat하게 편 후, 조건에 따라 출력
box = [x for row in graph for x in row]
if 0 in box: print(-1)
else: print(max(box)-1)