# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12921

# IDEA
# 에라토스테네스의 체에 따라 find_prime 함수 생성

def find_prime(n):
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if n%i == 0:
            return 0
    return 1

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if find_prime(i) == 1:
            answer += 1
    return answer