# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12915

# IDEA
# 문제에서 주어진대로 n번째 값을 기준으로 정렬
# n이 값다면 사전순 정렬

def solution(strings, n):
    return sorted(strings, key=lambda x:(x[n], x))