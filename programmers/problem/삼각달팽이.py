# 문제
# https://programmers.co.kr/learn/courses/30/lessons/68645

from itertools import chain

def solution(n):
    graph = [[0] * (i+1) for i in range(n)]
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            if i % 3 == 1:
                y += 1
            if i % 3 == 2:
                x -= 1
                y -= 1
            graph[x][y] = num
            num += 1
            
    answer = list(chain(*graph))
    return answer