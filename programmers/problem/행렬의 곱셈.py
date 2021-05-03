# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12949

# IDEA
# 행렬의 곱셈을 삼중 for문으로 구현

def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    
    for i in range(len(arr1)):
        for k in range(len(arr1[0])):
            a = arr1[i][k]
            for j in range(len(arr2[0])):
                b = arr2[k][j]
                answer[i][j] += a*b
    return answer

# simple code
# numpy 패키지 활용. numpy에서 행렬곱 연산은 np.dot()함수로 수행
import numpy as np

def simple_solution(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    answer = np.dot(arr1, arr2)
    return answer.tolist()