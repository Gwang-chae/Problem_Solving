# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12943

# IDEA
# 조건에 맞게 차례대로 구현하면 됨
# num의 입력값이 1로 들어오는 경우만 예외 처리

def solution(num):
    if num == 1:
        return 0
    answer = 0
    while True:
        answer += 1
        if answer > 500:
            return -1
        if num%2 == 0:
            num /= 2
        else:
            num = num*3 +1
        if num == 1:
            return answer