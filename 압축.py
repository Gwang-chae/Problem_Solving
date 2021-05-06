# 문제
# https://programmers.co.kr/learn/courses/30/lessons/17684

# IDEA
# string 패키지로 대문자 A~Z 까지의 딕셔너리 생성
# 끝 인덱스를 하나씩 늘려가며 딕셔너리에 들어가 있는지 여부 확인
# 없으면 해당 문자를 딕셔너리에 추가
# 인덱스들을 당겨가면서 모든 문자열 확인
# 끝 인덱스가 마지막 인덱스와 일치하면 break

import string
def solution(msg):
    word_dict = dict()
    num = 1
    for alpha in string.ascii_uppercase:
        word_dict[alpha] = num
        num += 1
        
    answer = []
    start, idx = 0, 0
    while True:
        idx += 1
        if idx == len(msg):
            answer.append(word_dict[msg[start:idx]])
            break
        if msg[start:idx+1] not in word_dict:
            word_dict[msg[start:idx+1]] = len(word_dict) + 1
            answer.append(word_dict[msg[start:idx]])
            start = idx
    return answer