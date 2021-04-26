# 문제
# https://programmers.co.kr/learn/courses/30/lessons/68644

# IDEA
# numbers의 길이는 2 이상 100 이하
# 따라서 combinations로 조합을 구해도 최대 100C2 가지밖에 나오지 않음

from itertools import combinations

def solution(numbers):
    numbers.sort
    comb = list(combinations(numbers, 2))
    answer = []

    for i in comb:
        if sum(i) not in answer:
            answer.append(sum(i))

    answer.sort()
    return answer