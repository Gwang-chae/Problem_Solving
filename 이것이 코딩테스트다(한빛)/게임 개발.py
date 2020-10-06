n, m = map(int, input().split())

# 방문 위치 저장용 리스트 d
d = [[0] * m for _ in range(n)]
x,y, direction = map(int, input().split())
d[x][y] = 1

game_map = []
for __ in range(n):
    game_map.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction   # 전역변수 선언을 해줘야 함수안에서 변수 조작 가능
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dx[direction]
    if d[nx][ny] == 0 and game_map[nx][ny] == 0:
        d[nx][ny] += 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else :
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if game_map[nx][ny] == 0:
            x = nx
            y = ny
        else :
            break
        turn_time = 0
print(count)