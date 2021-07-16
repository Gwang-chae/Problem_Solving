# 문제
# https://www.acmicpc.net/problem/1051

# IDEA
# 직사각형 안에서 만들 수 있는 가장 큰 정사각형을 찾는 구현 문제
# 4 모퉁이가 모두 같으면 정사각형

def find_square(k):
    for i in range(n-k+1):
        for j in range(m-k+1):
            if graph[i][j] == graph[i][j+k-1] == graph[i+k-1][j] == graph[i+k-1][j+k-1]:
                return True
    return False

n,m = map(int, input().split())
k = min(n,m)
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

while True:
    if find_square(k):
        print(k**2)
        break
    k -= 1
