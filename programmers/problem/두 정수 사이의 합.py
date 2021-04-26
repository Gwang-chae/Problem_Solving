# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12912

# IDEA
# a,b의 대소관계를 명확히 한 후 그 사이의 값들을 summation
def solution(a, b):
    start, end = min(a,b), max(a,b)
    return sum(range(start, end + 1))


# 효율성 코드
# 등차수열의 합공식으로 계산
# S = n(a+l)/2. a = 시작값, l = 끝값, n = 숫자 개수

def best_solution(a, b):
    return (abs(a-b)+1)*(a+b)//2