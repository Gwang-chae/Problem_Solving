# 문제
# https://www.acmicpc.net/problem/1072

# IDEA
# math의 floor()로 소수 아랫점 제거 -> //으로도 표현 가능
# Binary Search로 처음으로 z가 달라지는 지점 탐색

from math import floor
x,y = map(int, input().split())
z = floor((y*100)/x)
start, end = 1, 1000000000

if z >= 99: print(-1)
else:
    # 아래의 Binary Search를 하게 되면
    # z가 변하지 않으면서 가질 수 있는 가장 최대의 값을 도출
    # 따라서 구한 answer에 +1 연산을 하면 처음으로 z가 달라지는 값이 됨
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        nx, ny = x + mid, y + mid
        if floor((ny *100)/nx) > z:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    print(answer+1)


# 실수의 연산
# (y*100)/x와 (y/x)*100은 전혀 다른 값 -> 무한 소수가 나오는 케이스
# 실수의 연산은 항상 사용에 주의!!