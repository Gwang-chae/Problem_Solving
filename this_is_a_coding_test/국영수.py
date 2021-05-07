# 문제
# https://www.acmicpc.net/problem/10825

# IDEA
# 정렬 문제
# sorted()로 처음에 해결했으나 시간초과
# sorted()는 새로 리스트를 생성하기 때문
# 따라서, sort()로 바로 정렬

n = int(input())
graph = []
for _ in range(n):
    name, korean, english, math = input().split()
    graph.append([int(korean), int(english), int(math), name])

graph.sort(key=lambda x:(-x[0], x[1], -x[2], x[3]))

for i in graph:
    print(i[3])