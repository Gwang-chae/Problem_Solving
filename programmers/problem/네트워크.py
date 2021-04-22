# 문제
# https://programmers.co.kr/learn/courses/30/lessons/43162

# IDEA
# 노드끼리 연결만 되어 있으면 그 자체로 하나의 네트워크
# 따라서 시작 노드와 연결된 모든 노드를 탐색하고
# 연결된 각 노드들을 하나씩 돌며 그 노드와 또 연결된 모든 노드 정보를 하나로 엮으면 됨 -> DFS 

def dfs(graph, start, visited):
    # 시작 노드를 방문 처리
    visited[start] = 1
    # 시작 노드와 연결된 모든 노드 탐색
    for idx, i in enumerate(graph[start]):
        # 만약 시작 노드와 연결되어 있고 방문하지 않았으면
        if visited[idx] == 0 and i == 1:
            # 해당 노드와 연결된 모든 노드를 탐색하며 방문 처리
            start = idx
            dfs(graph, start, visited)

def solution(n, computers):
    start = 0
    # 처리한 노드를 표시할 테이블 생성
    visited = [0] * n
    answer = 0
    while True:
        answer += 1
        dfs(computers, start, visited)
        # 만약 모두 방문 처리했으면 break
        if sum(visited) == n:
            break
        # 시작 노드는 방문하지 않은 노드부터 시작
        start = visited.index(0)
    return answer