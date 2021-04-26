# 문제
# https://programmers.co.kr/learn/courses/30/lessons/72410

# IDEA
# 문제에 나온 조건대로 차례대로 만들어주면 된다.
# 정규표현식을 사용할 수 있으면 쉽게 구현가능한 문제
# 3단계에서 .이 1회 이상 반복된 부분을 .으로 대체
# 4단계에서 new_id가 빈 문자열인지를 고려하지 않으면
# 인덱싱에서 오류가 발생하기 때문에 빈 문자열 여부를 확인한다.

# 4단계 자체를 new_id = re.sub(r'^[.]|[.]$', '', new_id)로 대체 가능

import re

def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    new_id = re.sub(r'[^a-z0-9\-\_\.]', '', new_id)
    # 3단계
    new_id = re.sub(r'[\.]+', '.', new_id)
    # 4단계
    if new_id:
        if new_id[0] == '.': new_id = new_id[1:]
    if new_id:
        if new_id[-1] == '.': new_id = new_id[:-1]
    # 5단계
    if not new_id: new_id = 'a'
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.': new_id = new_id[:-1]
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
    return new_id

