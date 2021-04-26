# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12931

# IDEA
# 각 자릿수별로 숫자를 쪼개고 summation

def solution(n):
    n = list(str(n))
    n = map(int, n)
    return sum(n)