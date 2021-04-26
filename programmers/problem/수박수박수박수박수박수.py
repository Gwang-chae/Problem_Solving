# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12922

# IDEA
# 단순 forloop 활용

def solution(n):
    answer = ''
    for i in range(n):
        if i%2 == 0: answer += '수'
        else: answer += '박'
    return answer

# simple code
def simpe_solution(n):
    return '수박' * (n//2) + '수' * (n%2)