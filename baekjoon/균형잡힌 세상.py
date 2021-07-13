# 문제
# https://www.acmicpc.net/problem/4949

# IDEA
# 문제 정의에 맞춰 짝이 안 맞는 소괄호, 대괄호 존재 시 'no' 출력
# 짝이 안 맞을 경우 아무 문자('#')나 입력하여 stack에 도로 넣어주고 break
# forloop가 종료되고도 stack에 원소가 남은 경우 'no'

while True:
    s = input()
    stack = []
    if s == '.': break

    for i in s:
        if i == '(':
            stack.append(i)
        if i == ')':
            if stack:
                last = stack.pop()
                if last == '(': continue
                else:
                    stack.append('#')
                    break
            else:
                stack.append('#')
                break
        if i == '[':
            stack.append(i)
        if i == ']':
            if stack:
                last = stack.pop()
                if last == '[': continue
                else:
                    stack.append('#')
                    break
            else:
                stack.append('#')
                break
    print('yes' if not stack else 'no')