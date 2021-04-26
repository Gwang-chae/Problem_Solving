# 문제
# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    n = len(nums)//2
    nums = set(nums)
    if n <= len(nums):
        return n
    else:
        return len(nums)

# simple code

def solution(nums):
    return min(len(nums)/2, len(set(nums)))