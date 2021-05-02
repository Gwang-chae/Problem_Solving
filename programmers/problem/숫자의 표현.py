# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12924

# IDEA
# 완전 탐색 구현
# 이중 for문으로 i를 늘려가며 연속된 수의 합이 n이 되는지 확인

def solution(n):
    answer = 1
    for i in range(1, n//2 + 1):
        count = 0
        for j in range(i, n+1):
            count += j
            if count == n:
                answer += 1
                break
            if count > n: break
    return answer