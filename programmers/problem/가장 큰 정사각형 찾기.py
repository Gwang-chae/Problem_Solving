# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12905

# IDEA
# 삼중 for문으로 구현했지만 효율성 문제로 실패
# 블로그 글들을 참조하여 DP 문제임을 확인
# (1,1)부터 왼쪽 대각선 위, 위, 왼쪽 인덱스가 0이 아니면
# 왼쪽 대각선 위, 위, 왼쪽 인덱스 중 min값 + 1로 값을 업데이트

def solution(board):
    zero_check = 0
    for row in board:
        zero_check += sum(row)
        if zero_check != 0:
            break
    if zero_check == 0:
        return 0

    max_point = 0
    for row in range(1, len(board)):
        for col in range(1, len(board[0])):
            if board[row][col] == 0:
                continue
            else:
                min_point = min(board[row-1][col-1], board[row-1][col], board[row][col-1])
                min_point += 1
                board[row][col] = min_point
                if max_point < board[row][col]:
                    max_point = board[row][col]
    if max_point == 0:
        return 1
    else:
        return max_point ** 2