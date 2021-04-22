# 문제
# https://programmers.co.kr/learn/courses/30/lessons/43105

# IDEA
# 거쳐간 숫자의 최댓값을 구하는 문제로 아랫줄은 윗줄의 영향을 받음
# 아랫줄 맨 왼쪽 인덱스와 맨 오른쪽 인덱스는 각각 경우의 수가 1개로 윗줄 계산값에 해당 인덱스를 더하면 됨
# 나머지 가운데 인덱스들의 경우는 윗줄의 왼쪽값, 윗줄의 오른쪽값 중 큰 값을 가져오면 됨

def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            # 맨 왼쪽 인덱스일 경우
            if j == 0:
                triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            # 맨 오른쪽 인덱스일 경우
            elif j == i:
                triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
            # 가운데 인덱스일 경우
            else :
                triangle[i][j] = max(triangle[i-1][j-1] + triangle[i][j], triangle[i-1][j] + triangle[i][j])
    
    # 삼각형 마지막 줄의 최댓값이 답
    return max(triangle[-1])