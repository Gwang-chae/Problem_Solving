# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12928

# IDEA
# n == 0일 때를 고려하고, 나머지는 forloop로 해결

def solution(n):
    answer = 0
    if n == 0: return 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += i
    return answer