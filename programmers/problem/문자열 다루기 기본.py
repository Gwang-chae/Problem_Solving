# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12918

# IDEA
# 정규식으로 숫자가 아닌 값을 없애고 원래 문자와 비교
import re

def solution(s):
    num_s = re.sub(r'[^0-9]', '', s)
    return (len(s) == 4 or len(s) == 6) and len(s) == len(num_s)

# 보완점
# match() 함수를 통해서 처음부터 문자열과 정규식이 매치되는지 조사
# ^(\d{4}|\d{6})$ -> 숫자 4개 또는 6개

# def improved_solution(s):
    # return bool(re.match("^(\d{4}|\d{6})$", s))

# 효율성 코드
# isdigit() 함수로 숫자인지 아닌지 여부를 확인할 수 있음
def best_solution(s):
    return s.isdigit() and len(s) in (4, 6)