# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12951

# IDEA
# python 내장함수 capitalize() 함수 사용
# capitalize는 첫 문자열을 대문자로, 나머지를 소문자로 만드는 함수로
# JadenCase 생성 조건과 일치하는 함수라 할 수 있음

def solution(s):
    s = s.split(' ')
    answer = []
    
    for i in s:
        answer.append(i.capitalize())
    
    return ' '.join(answer)