# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12926

# IDEA
# ord() 함수로 ascii 변환 후 구간 조건에 따라
# 시저 암호 적용

def solution(s, n):
    answer = ''
    for i in s:
        if ord(i) == 32:
            answer += ' '
        if 65 <= ord(i) <= 90:
            if ord(i) + n > 90:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)
        if 97 <= ord(i) <= 122:
            if ord(i) + n > 122:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)
    return answer

# simple code
# issupper(), islower() 함수들을 통해 대소문자 여부 판별
# 리스트 인덱싱으로 직접 접근하여 값을 바꿔주는 방식 적용
# % 연산과 ord('A'), ord('a')를 더해줌으로써 간략화
def simple_solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))
    return ''.join(s)