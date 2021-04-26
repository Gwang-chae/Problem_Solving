# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12935

# IDEA
# 배열 길이가 1이면 -1, 나머지 경우는 min값 제거

def solution(arr):
    if len(arr) == 1:
        return [-1]
    arr.remove(min(arr))
    return arr