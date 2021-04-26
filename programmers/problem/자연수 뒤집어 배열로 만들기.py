# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12932

# IDEA
# 문자열 변환 후 [::-1] 형태로 reverse

def solution(n):
    n = list(str(n)[::-1])
    n = list(map(int, n))
    return n