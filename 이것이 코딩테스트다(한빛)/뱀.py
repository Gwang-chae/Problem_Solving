n = int(input())
k = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
turn_info = []

# 맵 정보 업데이트(사과 위치 기록)
# 사과가 있는 위치는 1로 표시
for _ in range(k):
    a,b = map(int, input().split())
    graph[a][b] = 1

# 방향 전환 정보 업데이트
l = int(input())
for _ in range(l):
    x,c = input().split()
    turn_info.append((int(x), c))

# x,y별 변화값 설정
# 문제에서 처음 시작 방향은 동쪽.
# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulation():
    # 뱀의 머리 위치
    x,y = 1,1
    # 뱀이 존재하는 위치는 2로 표시
    # 사과가 1, 뱀이 2
    # 시작 위치는 이미 뱀이 존재하므로 2
    graph[x][y] = 2
    # 방향은 동쪽부터 시작
    direction = 0
    time = 0
    # turn_info의 인덱스
    index = 0
    # 뱀의 전체 정보
    q = [(x,y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 맵 범위 안에 있고, 뱀 몸통이 없는 부분이라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and graph[nx][ny] != 2:
            # 사과가 없으면 이동 후에 꼬리를 제거
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx,ny))
                px, py = q.pop(0)
                graph[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                q.append((nx,ny))
        # 벽이나 몸에 부딪히면
        # 1초 후 break
        else:
            time += 1
            break

        x,y = nx,ny # 다음 위치로 머리 이동
        time += 1
        if index < l and time == turn_info[index][0]:
            direction = turn(direction, turn_info[index][1])
            index += 1
    
    return time

print(simulation())