# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    sum_x = sum((map(int, list(str(x)))))
    return x%sum_x == 0