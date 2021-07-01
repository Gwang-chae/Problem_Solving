# 문제
# https://www.acmicpc.net/problem/1541

# IDEA
# '+','-'로 이뤄진 식에서 괄호로 최솟값을 만드려면
# '+'로 묶인 부분들을 먼저 계산해 준 후, '-' 연산을 수행하면 됨

# 입력을 받으면서 '-'를 구분자로 split
arr = input().split('-')
answer = 0

# 첫 번째 '+' 묶음은 answer에 '+' 연산
for i in arr[0].split('+'):
    answer += int(i)

# 첫 번째를 제외한 arr 원소들은 '-' 연산으로 나눠졌었기 때문에 answer에 '-' 연산
for i in arr[1:]:
    # '+'로 묶인 원소들은 결국 '-'로 부호 변경되기 때문에
    # 원소들 하나하나 answer에서 빼줌
    for j in i.split('+'):
        answer -= int(j)

print(answer)