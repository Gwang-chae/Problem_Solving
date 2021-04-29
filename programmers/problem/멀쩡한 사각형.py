# 문제
# https://programmers.co.kr/learn/courses/30/lessons/62048

def gcd(a,b):
    r = a%b
    if r == 0:
        return b
    else:
        return gcd(b, r)

print(gcd(12,9))