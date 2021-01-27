# 문제 설명
# https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    # 다리의 현재 상태를 확인할 수 있는 que 생성
    bridge_q = [0] * bridge_length
    time = 0

    while bridge_q:
        time += 1
        bridge_q.pop(0)
        if truck_weights:
            if sum(bridge_q) + truck_weights[0] <= weight:
                bridge_q.append(truck_weights.pop(0))
            else:
                bridge_q.append(0)
    return time