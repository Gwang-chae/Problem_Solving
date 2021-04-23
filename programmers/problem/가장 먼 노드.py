import heapq

def solution(n, edge):
    INF = 1e9
    # 시작 노드는 1번
    start = 1
    
    graph = [[] for i in range(n+1)]
    distance = [INF] * (n+1)
    
    # 양방향 그래프이므로 간선 정보를 모두 graph에 담아주고
    # 노드의 거리값은 정해져 있지 않지만 노드 몇개를 거쳐야 하는지
    # 구해야 하기 때문에 노드간 거리를 1로 설정하여 graph에 삽입
    for node1,node2 in edge:
        graph[node1].append((node2,1))
        graph[node2].append((node1,1))
    
    # 다익스트라 알고리즘 구현
    # q에는 (거리, 노드)쌍으로 입력하여 거리에 따른 최소 힙을 구현
    q = []
    # 시작 노드부터 시작 노드로 가기 위한 최단 경로는 0이므로 0 설정, q에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            # 거쳐간 값으로 최단 거리를 변경
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    answer_lst = [x for x in distance if x != INF]
    answer = answer_lst.count(max(answer_lst))
    
    return answer