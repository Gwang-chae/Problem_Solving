# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12930#

# IDEA
# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야 함
# 따라서, 공백이 나올 경우 idx를 초기화하면서 인덱스를 판단

def solution(s):
    answer = ''
    idx = 0
    for i in s:
        if i.isalpha():
            if idx%2 == 0:
                answer += i.upper()
                idx += 1
            else:
                answer += i.lower()
                idx += 1
        else:
            answer += ' '
            idx = 0
    return answer