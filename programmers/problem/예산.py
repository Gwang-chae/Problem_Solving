# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12982

# IDEA
# 전형적인 greedy 문제
# 예산이 적게 들어가는 순으로 정렬 후 예산 분배
# 예산이 초과될 시 바로 break

def solution(d, budget):
    d.sort()
    answer = 0
    for x in d:
        budget -= x
        if budget >= 0:
            answer +=1
        else:
            break
    return answer