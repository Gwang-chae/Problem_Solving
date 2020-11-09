n,m = list(map(int, input().split()))
rice_cake = list(map(int, input().split()))

start = 0
end = max(rice_cake)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for i in rice_cake:
        if i > mid:
            total += i - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)