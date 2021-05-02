# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12939

# IDEA
# 문자열 처리 후 mapping하여 int 변환

def solution(s):
    s = s.split(' ')
    s = list(map(int, s))
    return '{} {}'.format(min(s),max(s))