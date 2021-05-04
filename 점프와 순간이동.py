# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12980

# IDEA
# 처음 구상은 DP 테이블을 만들어서 해당 인덱스의 값을 구하는 것이었으나
# 문제 정의 상 n은 10억 이하의 자연수까지 가능하기 때문에 효율성에서 문제
# 그렇기 때문에, 반대로 n에서 0으로 가는 경우를 역산
# 2로 나누어 떨어지지 않는 경우에 값을 늘려주면 계산 가능

def solution(n):
    answer = 0
    while n != 0:
        q,r = divmod(n, 2)
        n = q
        if r == 1: answer += 1
    return answer

# simple code
# 이진수로 변환 후, 1의 개수를 구함

def simple_solution(n):
    return bin(n).count('1')