# 문제
# https://programmers.co.kr/learn/courses/30/lessons/76501

# IDEA
# zip() 함수로 absolutes와 signs를 엮으면서 합을 구한다.

def solution(absolutes, signs):
    answer = 0
    for number, sign in zip(absolutes, signs):
        if sign: answer += number
        else: answer -= number
    return answer