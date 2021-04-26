# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12977

# IDEA
# 문제 조건 상 nums 안에 숫자는 중복이 없고, 모든 조합의 경우의 수를 구해야 함
# itertools의 combinations 패키지 활용
# 에라토스테네스의 체를 사용하여 소수 여부인지를 판별하는 함수 생성

from itertools import combinations

def prime(n):
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if n%i == 0:
            return 0
    return 1

def solution(nums):
    comb = list(combinations(nums, 3))
    comb_sum = []
    for i in comb:
        comb_sum.append(sum(i))

    answer = []
    for i in comb_sum:
        answer.append(prime(i))

    return sum(answer)