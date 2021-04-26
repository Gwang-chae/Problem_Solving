# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12901

# IDEA
# datetime 패키지 활용 -> datetime 형식으로 변환
# weekday() 함수를 통해 요일 반환 0 - 월요일, ~ 6 - 일요일

import datetime

def solution(a, b):
    date = datetime.datetime(2016, a, b)
    weekday = date.weekday()
    if weekday == 0: return 'MON'
    elif weekday == 1: return 'TUE'
    elif weekday == 2: return 'WED'
    elif weekday == 3: return 'THU'
    elif weekday == 4: return 'FRI'
    elif weekday == 5: return 'SAT'
    else: return 'SUN'
