# 문제
# https://programmers.co.kr/learn/courses/30/lessons/17682

# IDEA
# 정규식으로 3번의 다트게임 결과를 분리
# 조건에 따라 결과값에 해당하는 점수를 업데이트

import re

def solution(dartResult):
    result_list = re.findall(r'\d{1,2}\D{1,2}', dartResult)
    answer = [0] * 3

    for idx, result in enumerate(result_list):
        digit_count = 0
        for i in result:
            if i.isdigit():
                digit_count += 1
                answer[idx] += int(i)
                if digit_count == 2:
                    answer[idx] = 10
            elif i.isalpha():
                if i == 'S': continue
                elif i == 'D': answer[idx] **= 2
                else: answer[idx] **= 3
            else:
                if i == '*':
                    if idx == 0:
                        answer[idx] *= 2
                    else:
                        answer[idx-1] *= 2
                        answer[idx] *= 2
                else:
                        answer[idx] *= -1
    return sum(answer)