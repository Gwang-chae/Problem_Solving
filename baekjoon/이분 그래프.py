# 문제
# https://www.acmicpc.net/problem/1707

# IDEA
# 이분 그래프를 구현하는 문제
# 이분 그래프를 이해하지 못해 싸이클 판별 문제인 줄 알고 접근했었음
# 다른 사람의 코드를 참고로 bfs 구현

# 이분 그래프 정의대로 그래프를 분할할 수 있다면
# 특정 노드 a가 집합 A일 때 a와 직접 연결된 다른 노드들은 다른 집합 B에 속해야 함

import sys
from collections import deque

def bfs(graph, start, visited):
    # 시작 노드를 집합 1로 처리
    visited[start] = 1
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        # now 노드와 연결된 노드들을 탐색
        for i in graph[now]:
            # 처리된 적이 없다면
            if visited[i] == 0:
                # 현재 노드와 다른 집합으로 설정(두 집합은 1, -1로 부호가 다름)
                visited[i] = -visited[now]
                # 해당 노드를 큐에 삽입
                q.append(i)
            # 처리된 적이 있고
            else:
                # 현재 노드와 연결된 노드가 부호가 같다면
                # 이분 그래프 성립 불가
                if visited[i] == visited[now]:
                    return False
    return True

input = sys.stdin.readline
k = int(input())
for _ in range(k):
    v,e = map(int, input().split())
    flag = True
    graph = [[] for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]

    # 간선 정보 입력
    for _ in range(e):
        a,b = map(int, input().split())
        # a,b 양방향 처리
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v+1):
        # 처리 안된 노드일 경우
        if visited[i] == 0:
            # bfs 실행, 만약 False값을 받으면 이분 그래프 성립 불가
            if not bfs(graph, i, visited):
                flag = False
                break

    if flag: print('YES')
    else: print('NO')
