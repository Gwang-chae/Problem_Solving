# 문제
# https://programmers.co.kr/learn/courses/30/lessons/72412

# IDEA
# query에서 요하는 조건에 해당하는 info의 수를 반환

# 효율성 문제로 인해 찾은 블로그 copy code
# info가 가능한 조합들을 각각 하나의 문자로 생성하고 key로 지정
# 각 info의 score를 value로 설정.
# query를 하나씩 돌며 query에 해당하는 key를 찾고 해당 key의 score 조건을 만족하는 개수를 count
# 이 때, 이진 탐색을 통해서 원하는 값 이상의 값이 처음 나오는 인덱스를 탐색하여 시간 단축
from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    # score를 list형태로 append하며 업데이트하기 위해
    # defaultdict로 딕셔너리 생성
    info_dict = defaultdict(list)
    
    for i in info:
        i = i.split()
        key = i[:-1]
        score = int(i[-1])
        # info로 만들 수 있는 모든 조합을 구하기 위해 이중 forloop
        for j in range(5):
            for c in combinations(key, j):
                # 조합을 하나의 문자로 생성해서 key로 지정하고
                # 해당 key의 score를 append
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(score)

    # 이진 탐색을 사용하기 위해 각 key의 value들을 정렬            
    for key in info_dict.keys():
        info_dict[key].sort()
    
    for q in query:
        q = q.split(' ')
        q_score = int(q[-1])
        q = q[:-1]
        
        # query의 and와 '-' 제거
        for i in range(3):
            q.remove('and')
        while '-' in q:
            q.remove('-')
        # key검색을 위해 query의 조합을 하나의 문자로 생성
        tmp_q = ''.join(q)
        
        # tmp_q가 info_dict에 없는 경우도 있으므로
        # if문으로 조건 생성
        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if scores:
                # 이진 탐색
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end)//2
                    if scores[mid] >= q_score:
                        end = mid
                    else:
                        start = mid + 1
                # 이진 탐색 결과 start는 q_score 이상인 첫번째 값이 나오는 인덱스
                answer.append(len(scores) - start)
        else:
            answer.append(0)
    return answer