# 문제
# https://www.acmicpc.net/problem/1697

# IDEA
# BFS로 각각의 수식 갈래에 따라 값을 계산

from collections import deque

n, k = map(int, input().split())
# 최소로 도달할 경우를 저장할 visitied 변수 선언
visited = [0] * 100001

def bfs(n, k):
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        if x == k:
            print(visited[x])
            break
        else:
            # 각 수식을 루프를 돌면서
            for dx in (x-1, x+1, x * 2):
                # 범위 안에서
                # not visited[dx] -> 최소로 도달할 경우만 저장
                if 0 <= dx < 100001 and not visited[dx]:
                    visited[dx] = visited[x] + 1
                    queue.append(dx)
bfs(n, k)