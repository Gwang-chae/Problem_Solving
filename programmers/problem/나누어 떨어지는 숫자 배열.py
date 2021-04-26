# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12910

# IDEA
# 문제 조건에 맞게 list comprehension

def solution(arr, divisor):
    answer = [x for x in arr if x%divisor == 0]
    if not answer:
        return [-1]
    answer.sort()
    return answer