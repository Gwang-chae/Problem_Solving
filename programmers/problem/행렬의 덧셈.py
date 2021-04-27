# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12950

# IDEA
# 이중 forloop로 2차원 리스트의 2개의 각 원소간의 합을 구함.

def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        sub = []
        for x, y in zip(i, j):
            sub.append(x+y)
        answer.append(sub)
    return answer

# 다른 풀이
# numpy 활용
import numpy as np

def solution(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    answer = arr1 + arr2
    return answer.tolist()