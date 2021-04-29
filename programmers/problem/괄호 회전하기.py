# 문제
# https://programmers.co.kr/learn/courses/30/lessons/76502

# IDEA
# 오른쪽 괄호가 먼저 나오거나,
# 저장한 괄호 중 마지막 괄호의 짝이 나오지 않으면 해당 문자는 올바르지 않음
# 짝이 맞다면 저장한 괄호들을 지워나가고 함수 결과로 빈 값이 나오면 해당 문자는 올바른 괄호 문자

left = ['[', '(', '{']
right = [']', ')', '}']

def move_left(s):
    return s[1:] + s[0]

def is_correct(s):
    bracket = []
    for i in s:
        if i in left:
            bracket.append(i)
        else:
            if not bracket or bracket[-1] != left[right.index(i)]:
                return False
            else: bracket.pop()
    return not bracket

def solution(s):
    answer = 0
    for _ in range(len(s)-1):
        if is_correct(s):
            answer += 1
        s = move_left(s)
    return answer