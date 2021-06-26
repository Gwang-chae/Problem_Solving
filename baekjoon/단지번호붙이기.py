# 문제
# https://www.acmicpc.net/problem/2667

# IDEA
# 집(1)이 상하좌우로 연결된 단지들을 구하고 각 단지의 가구 수를 구하는 문제
# DFS 구현, 단지 내 가구 수를 구해야 하기 때문에 count 변수를 가져와서 집계

n = int(input())
# 상하좌우 변화값
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 입력값을 한줄씩 받아 graph에 저장
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# dfs 구현
# dfs가 호출될 시점은 집이 있는 경우(1)에 해당
def dfs(x, y):
    global count
    # 방문한 집은 '#'으로 표현
    graph[x][y] = '#'
    count += 1
    # 상하좌우를 돌면서
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 변화값이 그래프를 벗어나지 않고, 방문하지 않은 집(1)이 있으면
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            # 방문처리
            graph[nx][ny] = '#'
            dfs(nx, ny)
    return count

answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = 0
            answer.append(dfs(i, j))

answer.sort()
print(len(answer))
for i in answer:
    print(i)