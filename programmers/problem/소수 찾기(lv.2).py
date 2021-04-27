# 문제
# https://programmers.co.kr/learn/courses/30/lessons/42839

# IDEA
# 숫자를 이용해서 만들 수 있는 모든 경우의 수를 구함
# permutations() 함수를 사용하여 순열 이용
# permutations()를 쓰면서 tuple 형태가 만들어지면 추후 사용이 불편하므로
# 생성 과정에서 mapping 하며 join 수행. 중복 제거
# 모든 만들 수 있는 숫자를 돌아가며 소수 여부 판별.

from itertools import permutations

def prime_check(n):
    m = n ** 0.5
    if n < 2:
        return False
    for i in range(2, int(m)+1):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    maked_numbers = []
    for i in range(1, len(numbers)+1):
        maked_numbers.append(list(set(map(''.join, permutations(numbers, i)))))
    
    possible_number = []
    for num_list in maked_numbers:
        for i in num_list:
            if int(i) not in possible_number:
                possible_number.append(int(i))
                
    answer = 0
    for i in possible_number:
        if prime_check(i):
            answer += 1
    return answer