# 문제
# https://www.acmicpc.net/problem/1966

# IDEA
# index 정보까지 tuple로 묶어서 큐 구현

from collections import deque

# 테스트 케이스 t
t = int(input())
for _ in range(t):
    # 문서의 개수 n, 알고자 하는 문서 번호 m
    n, m = map(int, input().split())
    l = list(map(int, input().split()))

    q = deque([])
    for idx, value in enumerate(l):
        # 큐에 문서 순서(idx)와 중요도를 쌍으로 묶어 삽입
        q.append((idx, value))

    # 문서들을 정렬
    l.sort()

    count = 0
    while True:
        # 큐에서 pop
        idx, value = q.popleft()
        # idx가 찾고자하는 m이면서 중요도도 가장 높으면
        # count를 하나 올리고 break
        if idx == m and value == l[-1]:
            count += 1
            break
        # idx가 m은 아니지만 중요도가 가장 높은 문서라면
        # count 후 l에서도 마찬가지로 pop
        elif value == l[-1]:
            count += 1
            l.pop()
        # 나머지 케이스들은 대기 후순위로 배치
        else: q.append((idx,value))
        
    print(count)