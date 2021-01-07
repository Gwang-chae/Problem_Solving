from collections import deque

# 노드의 개수 v, 간선의 개수 e
v,e = map(int, input().split())
# 모든 노드에 대한 진입차수 테이블 생성, 0으로 초기화
indegree = [0] * (v+1)
# 노드에 연결된 간선들의 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보 입력받기
for _ in range(e):
    # a는 시작노드, b는 도착노드
    a,b = map(int, input().split())
    graph[a].append(b)
    # 진입차수 1 증가
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
    
        # now와 연결된 노드들의 진입차수 -1
        for i in graph[now]:
            indegree[i] -= 1
            # 새로 진입차수가 0이 된 노드들을 q에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    # 정렬값 출력
    for i in result:
        print(i, end=' ')

topology_sort()