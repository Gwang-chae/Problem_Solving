# 문제
# https://www.acmicpc.net/problem/9012

# IDEA
# 스택을 활용하여 문제대로 구현

t = int(input())
for _ in range(t):
    ps = list(input())
    stack = []
    possible = True

    for element in ps:
        if element == '(':
            stack.append(element)
        else:
            if not stack:
                possible = False
                break
            else:
                stack.pop()

    if not stack and possible:
        print('YES')
    else: print('NO')