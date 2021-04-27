# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12948

# IDEA
# str은 직접 슬라이싱으로 값 바꾸는게 안됨
# 따라서, 리스트 변환 후 슬라이싱 한 뒤 다시 join

def solution(phone_number):
    phone_number = list(phone_number)
    phone_number[:-4] = '*' * len(phone_number[:-4])
    return ''.join(phone_number)