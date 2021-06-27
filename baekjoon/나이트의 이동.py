# 문제
# https://www.acmicpc.net/problem/7562

# IDEA
# BFS 구현, 각 체스칸에 갈 수 있는 최소거리를 구하여 원하는 값을 출력

from collections import deque

# bfs 구현
def bfs(start_x, start_y, target_x, target_y):
    queue = deque([])
    queue.append((start_x, start_y))
    while queue:
        x, y = queue.popleft()
        if (x, y) == (target_x, target_y):
            print(visited[x][y])
            break
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            # 체스칸을 벗어나지 않는 범위에서 방문한 적이 한번이라도 없다면
            if 0 <= nx < k and 0 <= ny < k and not visited[nx][ny]:
                # 이전 값에 +1 처리
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

n = int(input())
for _ in range(n):
    k = int(input())
    start_x, start_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    
    # 나이트가 움직일 수 있는 경우의 수 8개
    # 각각의 변화량을 선언
    move = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    # 각 체스칸의 방문 정보를 받을 visited 변수 선언
    visited = [[0] * k for _ in range(k)]

    bfs(start_x, start_y, target_x, target_y)