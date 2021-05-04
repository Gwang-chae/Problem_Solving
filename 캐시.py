# 문제
# https://programmers.co.kr/learn/courses/30/lessons/17680

# IDEA
# LRU(Least Recently Use) 알고리즘을 아는지 물어보는 문제
# LRU는 가장 오랫동안 참조되지 않은 페이지를 교체하는 알고리즘
# ex) cachesize = 2일 때, 'Jeju'가 입력으로 들어오면
# cache에는 'Jeju'가 없으므로 cache miss. cache에는 이제 'Jeju'가 들어옴
# 다음으로 'Pangyo'가 들어올 때, 현재 cache에는 'Jeju'만 있으므로, 일치하는 값이 없고
# 따라서 cache miss. chach에는 이제 ['Jeju', 'Pangyo']가 저장
# 다음으로 'Seoul'이 들어오면, cache에 매치되는 값이 없으므로 cache miss.
# cachesize는 2로 제한되어 있기 때문에 가장 오랫동안 참조되지 않은 'Jeju'를 삭제하고 'Seoul'을 cache에 입력
# 만약 cache에 이미 존재하는 값이 들어오면, cache hit. 그리고 해당 값을 최신 값으로 변경
# 위와 같은 개념을 토대로 queue로 구현

from collections import deque

def solution(cacheSize, cities):
    cache = deque([])
    answer = 0
    if cacheSize == 0: return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        if city not in cache:
            answer += 5
            cache.append(city)
            if len(cache) > cacheSize:
                cache.popleft()
        else:
            answer += 1
            cache.remove(city)
            cache.append(city)
        
    return answer