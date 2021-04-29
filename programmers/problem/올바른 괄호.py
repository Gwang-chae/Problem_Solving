# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12909

# IDEA
# 괄호를 담을 리스트를 만들고
# '('가 들어오면 append ')'가 들어오면 pop
# 리스트가 빈 상태에서 ')'가 들어오면 해당 문자는 올바른 괄호가 아님
# 모든 for문을 돌았을때 리스트가 비었다면 해당 문자는 올바른 괄호

def solution(s):
    bracket = []
    for i in s:
        if i == '(':
            bracket.append(i)
        else:
            if bracket: bracket.pop()
            else: return False
    return not bracket