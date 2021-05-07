# 문제
# https://www.acmicpc.net/problem/14888

# IDEA
# 연산자 숫자와 일치하는 중복순열들을 product()를 사용하여 구한 뒤
# 각각의 연산 수행 후 최댓값, 최솟값을 찾음

# product() 함수는 중복순열, 카티션 곱(곱집합)을 만들어 줌

from itertools import product

n = int(input())
num_list = list(map(int, input().split()))
sign = list(map(int, input().split()))

p = list(product(['+','-','*','/'], repeat=(n-1)))
possible = []
for i in p:
    if i.count('+') == sign[0] and i.count('-') == sign[1] and i.count('*') == sign[2] and i.count('/') == sign[3]:
        possible.append(i)

max_total, min_total = -1e9, 1e9
for i in possible:
    total = num_list[0]
    for num, sign in zip(num_list[1:], i):
        if sign == '+': total += num
        if sign == '-': total -= num
        if sign == '*': total *= num
        if sign == '/': total = int(total/num)
    if total > max_total:
        max_total = total
    if total < min_total:
        min_total = total

print(max_total)
print(min_total)

# 책 풀이
# DFS 풀이

n = int(input())
num_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value, max_value = 1e9, -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + num_list[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now - num_list[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now * num_list[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / num_list[i]))
            div += 1

dfs(1, num_list[0])

print(max_value)
print(min_value)