n = int(input())
money = list(map(int, input().split()))

money.sort()

# 먼저 1을 만들 수 있는지 확인하기 위해
# target을 1로 설정 
target = 1

for i in money:
    if target < i:
        break
    target += i

print(target)