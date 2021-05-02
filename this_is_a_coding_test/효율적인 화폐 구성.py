# 화폐 개수 n, 만들려는 숫자 m
n,m = map(int, input().split())

# 화폐 개수 n만큼 각 화폐의 가치를 array에 입력
array = []
for _ in range(n):
    array.append(int(input()))

# DP 테이블 생성, 최소한의 화폐 개수를 구하기 위해
# 각 요소에는 0이 아닌 m보다 큰 숫자 10001을 입력
# m == 0인 경우, 최소한의 화폐 개수는 0이므로 d[0] = 0
d = [10001] * (m+1)
d[0] = 0

# array 속 화폐 가치를 하나하나 넣어가며 forloop
# k라는 화폐단위로 금액 i를 만들 수 있는 최소한의 화폐 개수를 a_i라고 할 때
# a_i-k를 만드는 방법이 존재하는 경우, -> a_i-k != 10001
# 점화식은 a_i = min(a_i, a_i-k + 1)
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] != 10001:
    print(d[m])
else :
    print(-1)