# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12941

# IDEA
# (A 배열의 작은 수) x (B 배열의 큰 수)의 형태로 만든 후 summation

def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    for a,b in zip(A,B):
        answer += a*b
    return answer