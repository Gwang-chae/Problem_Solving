# 문제
# https://programmers.co.kr/learn/courses/30/lessons/1844

# IDEA
# 대표적인 BFS 문제
# 조건에 따르면 목표지점까지 거리가 1인 경우는 정상적인 경우 발생할 수 없음
# 따라서, BFS를 수행했을 때 목표지점까지의 거리가 1이라면
# 해당 지점으로 갈 수 있는 경우가 없다는 의미이므로 -1 출력

from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((0,0))
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))     
    
    if maps[-1][-1] == 1:
        return -1
    else: return maps[-1][-1]