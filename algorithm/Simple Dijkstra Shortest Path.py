import sys

input = sys.stdin.readline
INF = int(1e9) # 10^9

# n은 노드, m은 간선
n,m = map(int, input().split())
# 시작 노드 입력
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담은 리스트 생성
# 이 때, 인덱스와 노드 번호를 일치시키기 위해 n+1개의 리스트 생성
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 확인하기 위한 리스트 생성
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    # a번 노드에서 b번 노드까지의 비용이 c
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환하는 함수
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    # 시작 노드와 연결된 노드들의 거리를 최단 거리 테이블에 입력
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복 작업
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            # 거쳐간 값으로 최단 거리를 변경
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, -1로 출력
    if distance[i] == INF:
        print(-1)
    else:
        print(distance[i])