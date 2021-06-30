# 문제
# https://www.acmicpc.net/problem/11404

# IDEA
# 문제 이름대로 플로이드 워셜 알고리즘으로 구현
# 한 가지 주의할 점은 두 노드를 연결하는 간선이 여러개일 수 있다는점
# 따라서, 간선 정보를 입력하며 테이블을 갱신할 때 기존값과 비교하는 작업 필요

import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
INF = 1e9

# 모든 노드에서 모든 노드로까지의 최단경로를 구하기 위해
# 2차원 리스트로 구현, INF 값으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 경우는 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: 
            graph[i][j] = 0

# 간선 정보를 입력받으며 테이블 갱신
# 이 때, 기존값과 비교해 작은 값으로 입력
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])
    
# 플로이드 워셜 알고리즘 구현
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 수행된 결과 출력
for i in range(1, n+1):
    for j in range(1, n+1):
            # 도달할 수 없는 경우, 0으로 출력
            if graph[i][j] == INF:
                print(0, end=" ")
            else:
                print(graph[i][j], end=" ") 
    print()