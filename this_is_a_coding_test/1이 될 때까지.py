# 내 풀이
n,k = map(int, input().split())
answer = 0
while n != 1 :
    if n % k == 0 :
        n = n // k
    else :
        n -= 1
    answer += 1

print(answer)

### Short Coding in textbook
# n,k = map(int, input().split())
# answer = 0
#
# while True :
#     # (n == k로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
#     target = (n // k) * k
#     answer += (n - target)
#     n = target
#     if n < k :
#         break
#     answer += 1
#     n //= k
#
# # 마지막으로 남은 수에 대하여 1씩 빼기
# answer += (n-1)
# print(answer)