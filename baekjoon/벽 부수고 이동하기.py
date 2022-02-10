# 문제
# https://www.acmicpc.net/problem/2206

# IDEA

from collections import deque

def bfs():
    queue = deque()
    queue.append((0, 0, 1))
    
    if n == 1 and m == 1:
        return 1

    while queue:
        x, y, z= queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == '1' and z == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    queue.append((nx, ny, 0))
                elif graph[nx][ny] == '0' and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append((nx, ny, z))
    return -1

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][1] = 1
print(bfs())
