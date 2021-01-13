# 나의 풀이
# 통과는 했으나 numbers가 많아지면
# 효율이 떨어질 여지가 있음

def solution(numbers, target):
    lst = [numbers[0], -numbers[0]]
    idx = 1

    while idx != len(numbers):
        plus = []
        for i in lst:
            plus.append(i + numbers[idx])

        minus = []
        for i in lst:
            minus.append(i - numbers[idx])

        lst = plus + minus
        idx += 1

    answer_lst = [x for x in lst if x == target]
    answer = len(answer_lst)

    return answer

# DFS 풀이

answer = 0
def DFS(idx, numbers, target, value):
    # 함수 내에서 따로 return하지 않고
    # global 변수 answer에 값을 넣어 제출하는 식
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    # 재귀를 거치면서 조건에 맞는 경우 answer 계산
    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])

def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer