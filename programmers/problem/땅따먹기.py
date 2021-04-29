# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12913

# IDEA
# land[i][j]값은 land[i-1][j]값을 제외한 land[i-1] 중에서 최댓값을 기존의 land[i][j]에 더해주면 됨
# 따라서, list comprehension으로 land[i-1][j] 값을 없애고 그 안에서 최댓값 탐색

def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max([x for idx,x in enumerate(land[i-1]) if not idx == j])
    return max(land[-1])