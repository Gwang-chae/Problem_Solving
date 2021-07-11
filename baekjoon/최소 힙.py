# 문제
# https://www.acmicpc.net/problem/1927

# IDEA
# 파이썬의 heapq는 이진 트리 기반의 최소힙 자료구조를 제공

import heapq
import sys

input = sys.stdin.readline
n = int(input())
q = []
for _ in range(n):
    num = int(input())
    # 입력이 0이고, 큐에 아무것도 없으면 0 출력
    if num == 0 and not q:
        print(0)
    # 입력이 0이라면 pop
    elif num == 0:
        print(heapq.heappop(q))
    # 나머지 경우는 큐에 push
    else:
        heapq.heappush(q, num)  
# heapq.heappush