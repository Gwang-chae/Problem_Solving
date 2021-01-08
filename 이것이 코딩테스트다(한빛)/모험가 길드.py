import sys

input = sys.stdin.readline

n = int(input())
crew = list(map(int, input().split()))
crew.sort()

result = 0
count = 0
for i in crew:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)