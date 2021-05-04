# 문제
# https://programmers.co.kr/learn/courses/30/lessons/17677

# IDEA
# 문자를 2개씩 자르면서 해당 문자에 특수문자, 숫자, 공백 등이 없으면 다중 집합으로 생성
# 중복까지 고려해야 하기 때문에 collections의 Counter()함수를 통해 값들의 개수 count
# &연산, |연산으로 각각 교집합, 합집합을 만들고
# 교집합, 합집합의 값을 summation

import math
from collections import Counter

def multiple_set(s):
    s = s.lower()
    array = []
    for i in range(len(s)-1):
        if s[i:i+2].isalpha():
            array.append(s[i:i+2])
    return array

def solution(str1, str2):
    str1 = multiple_set(str1)
    str2 = multiple_set(str2)
    
    if not str1 and not str2: return 65536
    intersection = Counter(str1) & Counter(str2)
    intersection = sum(intersection.values())
    
    union = Counter(str1) | Counter(str2)
    union = sum(union.values())
    
    return math.floor(intersection/union * 65536)