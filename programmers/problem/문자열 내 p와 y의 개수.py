# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12916

# IDEA
# 정규식을 사용하여 p의 개수, y의 개수 비교
import re

def solution(s):
    p_s = re.sub(r'[^pP]', '', s)
    y_s = re.sub(r'[^yY]', '', s)
    
    return (True if len(p_s) == len(y_s) else False)

# 효율성 코드
# 소문자로 통일한 뒤 count 함수를 통해 True/False 여부만 return
def best_solution(s):
    return s.lower().count('p') == s.lower().count('y')
