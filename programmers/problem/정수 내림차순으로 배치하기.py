# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12933

# IDEA
# 문자열 변환 후 정렬, join
def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    n = ''.join(n)
    return int(n)