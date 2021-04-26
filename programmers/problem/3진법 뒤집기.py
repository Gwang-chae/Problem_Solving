# 문제
# https://programmers.co.kr/learn/courses/30/lessons/68935

# IDEA
# 3진법으로 바꾼 후, 바꾼 수를 역순으로 뒤집기, 이후 10진법 수로 변환
# 각각 변환 과정을 함수로 작성
# 마지막 10진법 수 변환은 int(n, base)함수 기능을 그대로 이용

def convert(n, base):
    T = '012'
    q,r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def reverse(n):
    reversed_n = ''
    for i in n[-1::-1]:
        reversed_n += i
    return reversed_n

def solution(n):
    return int(reverse(convert(n, 3)), 3)
