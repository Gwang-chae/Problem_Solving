# 문제 설명
# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0
    waiting_list = [(value, idx) for idx, value in enumerate(priorities)]

    while True:
        j = waiting_list.pop(0)
        if waiting_list and max(waiting_list)[0] > j[0]:
            waiting_list.append(j)
        else:
            answer += 1
            if j[1] == location:break

    return answer