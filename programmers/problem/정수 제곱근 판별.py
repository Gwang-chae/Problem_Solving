# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12934

# IDEA
# 1부터 int(n**0.5) 값까지 돌며 제곱근 여부 판별

def solution(n):
    for i in range(1, int(n**0.5)+1):
        if n//i == i and n%i == 0:
            return (i+1) ** 2
    return -1

# 효율성 코드
# n의 제곱근을 1로 나눈 나머지가 0이면 정수이므로
# n의 제곱근은 어떤 양의 정수 x의 제곱임.

def best_solution(n):
    sqrt = n ** 0.5    
    if sqrt%1 == 0:
        return (sqrt+1) ** 2
    return -1