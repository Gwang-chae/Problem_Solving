from collections import deque
import copy
import sys

input = sys.stdin.readline

# 노드의 개수 n
n = int(input())
# 진입차수 테이블 생성 및 0으로 초기화
indegree = [0] * (n+1)
# 노드에 연결된 간선 정보를 담을 연결 리스트 생성
graph = [[] for i in range(n+1)]
# 각 강의 시간 테이블 생성 및 0으로 초기화
time = [0] * (n+1)

for i in range(1, n+1):
    # 입력은 강의 시간, 선수강 강의, ... , -1로 종료
    lecture = list(map(int, input().split()))
    time[i] = lecture[0]
    # 진입 차수 정보 업데이트
    # 선수강 강의 정보 업데이트
    for j in lecture[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

def topology_sort():
    # 리스트 값 복제시에는 deepcopy 사용
    result = copy.deepcopy(time)
    q = deque()

    # 진입 차수가 0인 노드들을 q에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        # q에서 값을 꺼내면서
        # 해당 노드와 연결된 노드들의 진입 차수 -1
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새로 진입 차수가 0이 된 노드들을 q에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()