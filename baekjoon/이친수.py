# 문제
# https://www.acmicpc.net/problem/2193

# IDEA

n = int(input())
dp = [0 for _ in range(91)]
for i in range(1, n+1):
    if i == 1: dp[i] = 1
    elif i == 2: dp[i] = 1
    else: dp[i] = dp[i-1] + dp[i-2]

print(dp[n])