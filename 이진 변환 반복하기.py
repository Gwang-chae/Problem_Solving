# 문제
# https://programmers.co.kr/learn/courses/30/lessons/70129

# IDEA
# Python의 내장함수 bin()을 통해 쉽게 이진수 변환 가능

def solution(s):
    count = 0
    zero = 0
    while s != '1':
        count += 1
        zero += s.count('0')
        s = bin(s.count('1'))[2:]
    return [count, zero]