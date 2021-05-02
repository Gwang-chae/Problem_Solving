# 내 풀이
n, m, k = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort(reverse=True)

first = n_list[0]
second = n_list[1]
answer = 0
count = 0
for i in range(m):
    if count < k :
        answer += first
    else :
        count = 0
        answer += second
    count += 1
print(answer)

### Short Coding in textbook
# 반복 수열의 개수를 구해 forloop 없이 해결
# count = int(m / (k+1)) * k
# count += m % (k+1)          # first가 더해지는 총 횟수
#
# answer = 0
# answer += count * first
# answer += (m - count) * second
# print(answer)