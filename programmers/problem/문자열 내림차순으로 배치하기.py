# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12917

# IDEA
# sort의 reverse 인자를 활용하여 내림차순 정렬
def solution(s):
    s = list(s)
    s.sort(reverse=True)
    return ''.join(s)