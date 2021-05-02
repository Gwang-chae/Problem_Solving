# combinations를 쓰면 편하게 풀 수 있지만
# n이 큰 수가 들어올 경우, 메모리를 많이 차지할 수 있음
from itertools import combinations

n,m = map(int, input().split())
ball = list(map(int, input().split()))

combination = list(combinations(ball, 2))

no_count = 0
for comb in combination:
    if comb[0] == comb[1]:
        non_count += 1

print(len(combination) - no_count)

# Greedy
from itertools import combinations

n,m = map(int, input().split())
ball = list(map(int, input().split()))

# 조건에서 m은 10이하의 자연수
# 볼의 무게에 해당하는 볼링공의 개수를 
# 셀 수 있는 테이블 생성
array = [0] * 11

for i in ball:
    array[i] += 1

result = 0
for i in range(1, m+1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)