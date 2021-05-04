# 문제
# https://programmers.co.kr/learn/courses/30/lessons/17687

# IDEA
# n진법 변환 함수 생성
# 필요한 만큼의 숫자까지만 변환하여 하나의 문자열에 저장
# 인덱싱을 통해 필요한 문자열 추출

import string

T = string.digits + string.ascii_uppercase
def convert(n, base):
    q,r = divmod(n, base)
    if q == 0: return T[r]
    else: return convert(q, base) + T[r]

def solution(n, t, m, p):
    converted_num = ''
    num = 0
    while len(converted_num) < t * m:
        converted_num += convert(num, n)
        num += 1
    
    answer = ''
    for i in range(t):
        answer += converted_num[i*m + p-1]
    return answer