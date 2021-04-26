# 문제
# https://programmers.co.kr/learn/courses/30/lessons/70128

# IDEA
# 문제에서 알려준 내적 공식대로(a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1]) 구현
# zip 함수로 길이가 같은 a,b의 각 원소의 곱을 더해 주면 된다

def solution(a, b):
    answer = 0
    for x,y in zip(a,b):
        answer += x*y
    return answer