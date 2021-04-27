# 문제
# https://programmers.co.kr/learn/courses/30/lessons/72411

# IDEA
# 메뉴들의 조합을 구하고, 그 조합의 등장 횟수를 구하는 문제이므로
# combinations()와 Counter() 활용
# 이 때,사전에 orders를 사전순으로 정렬하여 combinations()를 하며
# 원소간 조합 순서가 꼬이지 않도록 방지

# 추가적으로 Counter()는 most_common() 함수를 제공
# most_common(n)은 데이터 개수가 많은 순으로 n개 원소를 리스트 형태로 반환
from itertools import combinations
from collections import Counter

def solution(orders, course):
    # 메뉴 조합을 사전에 정렬
    orders = [list(sorted(x)) for x in orders]
    
    answer = []
    for k in course:
        order_comb = []
        for order in orders:
            if len(order) < k:
                continue
            order_comb.append(list(combinations(order, k)))
        
        # order_comb가 없는 경우도 있으므로 if문 설정
        if order_comb:
            order_comb_count = Counter(order_comb[0])
            for i in order_comb[1:]:
                order_comb_count.update(Counter(i))

            max_order = max(order_comb_count.values())

            for menu, count in order_comb_count.items():
                if count >= 2 and count == max_order:
                    answer.append(menu)

    # 튜플로 묶임 answer들 처리            
    answer_list = []
    for letter in answer:
        name = ''
        for i in letter:
            name += i
        answer_list.append(name)
    
    return sorted(answer_list, key=lambda x:x)