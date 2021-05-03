# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12985

# IDEA
# 각 순위에 1 더한 값을 2로 나눈 나머지가 같아질 때
# ex) a,b = 1, 2 -> (a+1)//2 == (b+1)//2
# 그 때 a,b가 대진을 하게 됨

def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a = (a+1) // 2
        b = (b+1) // 2
    return answer