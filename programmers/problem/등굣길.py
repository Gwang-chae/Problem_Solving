# 문제 설명
# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):

    # 인덱스와 좌표값을 맞추기 위해 (m+1) * (n+1) 형태의 그래프 생성
    # 문제에서는 m이 가로
    graph = [[0] * (m + 1) for _ in range(n + 1)]
    # 시작지점인 (1,1)로 갈 수 있는 경로는 자기 자신이므로 1로 초기화
    graph[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 시작지점은 이미 고려해서 입력했으므로 continue
            if i == 1 and j == 1:
                continue
            # puddle 좌표값은 (m, n) 형태로 주어지지만
            # graph를 생성하면서 graph는 [n][m]의 순서로 읽게 됨
            # 따라서 puddle은 [i, j]가 아닌 [j, i] 형태로 읽어야 함
            if [j, i] in puddles:
                graph[i][j] = 0
            # 진행방향은 오른쪽, 아래쪽밖에 없으므로
            # 해당값의 왼쪽, 위쪽 경우의 수를 더해 나가면 graph 테이블 완성
            else:
                graph[i][j] = graph[i - 1][j] + graph[i][j - 1]
    return graph[n][m] % 1000000007