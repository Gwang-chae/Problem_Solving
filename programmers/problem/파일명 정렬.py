# 문제
# https://programmers.co.kr/learn/courses/30/lessons/17686

# IDEA
# 정규식을 이용해서 문제에서 제시한 조건대로 HEAD, NUMBER, TAIL로 분리
# 분리 이후에는 HEAD의 경우, 대소문자 구분을 하지 않는다고 하였으므로
# HEAD를 대소문자 중 하나로 통일해서 정렬
# NUMBER 정렬

import re

def solution(files):
    files = [re.split(r'([\d]+)', x) for x in files]
    files = sorted(files, key=lambda x:(x[0].lower(), int(x[1])))
    return [''.join(x) for x in files]