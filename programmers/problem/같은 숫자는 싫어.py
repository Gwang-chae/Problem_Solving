# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12906

# IDEA
# 바로 앞 숫자와 현재 숫자가 같으면 건너뜀.
# 맨 첫 인덱스 처리만 잘 해주면 됨.
def solution(arr):
    prior = arr[0]
    answer = [arr[0]]
    for i in arr:
        if i == prior:
            continue
        else:
            prior = i
            answer.append(i)
    return answer
