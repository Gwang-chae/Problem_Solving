from collections import deque

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

# 상하좌우 x,y의 변화량 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간 밖을 탐색할 경우 스킵
            if nx < 0 or ny <0 or nx >= n or ny >= m:
                continue
            # 문제의 벽에 해당하는 부분일 경우 스킵
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))