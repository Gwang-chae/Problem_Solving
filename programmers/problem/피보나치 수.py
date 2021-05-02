# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12945

# IDEA
# 점화식을 사용하여 피보나치 수열 풀이

def solution(n):
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n] % 1234567

# 효율성 코드
# 점화식을 위한 리스트 생성 및 인덱스 접근 없이
# 값만을 바꿔나가기 때문에 좀 더 빠른 코드

def best_solution(n):
    a,b = 0, 1
    for _ in range(n):
        a,b = b, a+b
    return a % 1234567