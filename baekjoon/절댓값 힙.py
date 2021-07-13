# 문제
# https://www.acmicpc.net/problem/11286

# IDEA
# 힙의 우선순위를 절댓값으로 지정하여 문제 해결

import heapq
import sys

input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if x == 0 and q:
        print(heapq.heappop(q)[1])
    elif x == 0 and not q:
        print(0)
    else:
        heapq.heappush(q, (abs(x), x))