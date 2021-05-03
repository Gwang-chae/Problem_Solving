# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12973

# IDEA
# 스택에 원소 하나씩 넣으면서 짝이 되면 제거
# 마지막에 빈 스택이 반환되면 해당 문자열은 짝지어 제거가능

def solution(s):
    stack = []
    for i in s:
        if not stack or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
    return int(not stack)