# 문제
# https://www.acmicpc.net/problem/1263

# IDEA
# Greedy하게 해결

import sys

input = sys.stdin.readline
n = int(input())
task = []
for _ in range(n):
    a,b = map(int, input().split())
    task.append((b,a))
# 끝내야 하는 시간 기준으로 정렬
task.sort()

# 가장 먼저 끝내야 하는 작업의 끝내야 하는 시간 - 걸리는 시간 init
init = task[0][0] - task[0][1]
gap = 0

# 먼저 끝내야하는 시간 - 걸리는 시간을 시작 시간으로 설정
while True:
    # 매 라운드마다 처음 현재 시간은 init - gap
    now = init - gap
    if now < 0: 
        print(-1)
        break
    else:
        # 모든 작업 확인
        for i in range(n):
            now += task[i][1]
            # 만약 현재 시간이 끝내야하는 시간보다 커지면 forloop break
            # 이 때 현재 시간과 끝내야하는 시간의 차를
            # 다음번 시작시간에서 빼 주면서 업데이트
            if now > task[i][0]:
                gap += now - task[i][0]
                break
        # 모든 작업이 가능하면 출력
        else:
            print(init - gap)
            break