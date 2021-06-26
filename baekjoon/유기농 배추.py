# 문제
# https://www.acmicpc.net/problem/1012

# IDEA
# DFS 구현
# 백준 사이트에서는 런타임 에러가 떴었으나 파이썬 기본 재귀 깊이 제한을 늘린 결과 통과
# 파이썬의 기본 재귀 깊이 제한이 1000인 점을 항상 인식하고
# 재귀를 사용할 일이 있다면 sys.setrecursionlimit() 코드로 깊이를 늘려주자...!!!

import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
# 상하좌우 변화량
dx = [-1,1,0,0]
dy = [0,0,-1,1]

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())

    graph = [[0] * n for _ in range(m)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1


    def dfs(x, y):
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 그래프를 넘지 않는 범위에서 1인 값일 경우
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
                # 해당 좌표를 방문처리 후, 해당 좌표에서 탐색
                graph[nx][ny] = 0
                dfs(nx, ny)

    answer = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                answer += 1
                dfs(i, j)

    print(answer)