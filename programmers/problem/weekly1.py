# 문제
# https://programmers.co.kr/learn/courses/30/lessons/82612

# IDEA
# 주어진 문제대로 구현만 하면 되는 문제

def solution(price, money, count):
    answer = 0
    for i in range(count):
        answer += price * (i+1)
    if money >= answer: return 0
    else: return answer - money