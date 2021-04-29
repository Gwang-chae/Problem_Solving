# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12911

# IDEA
# 조건에 맞게 구현. bin() 함수를 사용해서 쉽게 이진수로 변환

def solution(n):
    n_one = list(bin(n)).count('1')
    m = n + 1
    while True:
        m_one = list(bin(m)).count('1')
        if n_one == m_one:
            break
        m += 1
    return m

print(int('20',4))