# 문제
# https://programmers.co.kr/learn/courses/30/lessons/60063

# IDEA
# BFS를 이용하여 (n,n)까지의 최소거리를 구하는 문제
# 두 좌표를 동시에 고려해야 하는 문제로, 막혀서 책 풀이를 copy하여 품

# 알게된 점
# {}는 안에 값이 'key': 'value' 형식이 아니라면 set type...
# 한 번 방문한 좌표는 두 번 방문하지 않기 위해 두 좌표를 set() 안에 넣으면서 관리

# 경우의 수를 고려해서 풀이
# 이동할 수 있는 경우
# 1. 상하좌우 이동 -> 상하좌우 변화값을 반영한 두 좌표가 모두 0
# 2. 현재 가로방향일 때 90도 회전
    # 2-1) 시계방향 회전 -> 두 좌표 각각의 위의 값들이 0 0 이어야 함
    # 2-2) 반시계방향 회전 -> 두 좌표 각각의 아래 값들이 0 0 이어야 함
# 3. 현재 세로방향일 때 90도 회전
    # 3-1) 시계방향 회전 -> 두 좌표 각각의 왼쪽 값들이 0 0 이어야 함
    # 3-2) 반시계방향 회전 -> 두 좌표 각각의 오른쪽 값들이 0 0 이어야 함    

from collections import deque

# 다음 가능한 위치를 반환해주는 함수
def get_next_pos(pos, board):
    next_pos = []   # 반환 결과를 담을 리스트 생성
    pos = list(pos) # 현재 위치를 set -> list 형식 변환
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # 상하좌우 변화량
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    # 상하좌우 위치 이동이 가능한 경우 next_pos에 삽입 
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    # 현재 로봇이 가로 방향일 때
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 현재 로봇이 세로 방향일 때
    if pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    return next_pos

def solution(board):
    n = len(board)
    # 좌표값들을 바로 인덱싱할 수 있도록 벽(1)으로 padding
    # 좌표값들을 업데이트
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    q = deque()
    visited = []
    pos = {(1,1), (1,2)}    # 시작 위치 설정
    q.append((pos, 0))      # q에 시작 위치와, 거리값 설정
    visited.append(pos)     # 해당 지점 방문 처리

    while q:
        pos, cost = q.popleft()
        # (n,n) 위치에 로봇이 도달하면, 최단 거리이므로 반환
        if (n,n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 모든 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 만약 방문하지 않은 위치라면 쿠에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)

    return 0

# print(type({(1,1), (1,2)}))
# print(type({'key':1}))