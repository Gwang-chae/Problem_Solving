# 문제
# https://www.acmicpc.net/problem/15686

# IDEA
# 치킨집이 13개 이하로 제한되어 있으므로 combinations()를 활용해 모든 조합 도출
# 집과의 거리들을 구하며 가장 최저 거리가 나올 때를 출력

# 내 풀이
from itertools import combinations

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

house, chicken = [], []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i,j))
        if graph[i][j] == 2:
            chicken.append((i,j))
            
def close_chicken(house, chicken):
    min_dist = 1e9
    for c in chicken:
        distance = abs(house[0]-c[0]) + abs(house[1]-c[1])
        if distance < min_dist:
            min_dist = distance
    return min_dist

comb = combinations(chicken, m)
min_total = 1e9
for c_comb in comb:
    total = 0
    for h in house:
        total += close_chicken(h, c_comb)
    if total < min_total:
        min_total = total
print(min_total)

# 책 풀이
# 내 풀이와의 차이
# 데이터를 받으면서 바로 집과 치킨집의 값을 튜플 형태로 받음
# 내 풀이에서는 graph로 따로 모든 정보를 받았지만 그럴 필요x
# get_sum 함수에서 바로 이중 forloop형태로 가독성이 높음

from itertools import combinations

n,m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))

candidates = list(combinations(chicken, m))

def get_sum(candidates):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidates:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
print(result)