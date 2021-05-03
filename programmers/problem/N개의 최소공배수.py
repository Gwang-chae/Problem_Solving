# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12953

# IDEA
# 유클리드 호제법으로 gcd, lcm 함수 생성

def gcd(a,b):
    a,b = max(a,b), min(a,b)
    r = a%b
    if r == 0: return b
    else: return gcd(b,r)

def lcm(a,b):
    return (a*b)//gcd(a,b)

def solution(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        answer = arr[0]
        for i in arr[1:]:
            answer = lcm(answer, i)
        return answer

# simple code
# math 패키지의 gcd() 함수 사용

from math import gcd

def simple_solution(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        answer = arr[0]
        for i in arr[1:]:
            answer = answer*i // gcd(answer,i)
        return answer