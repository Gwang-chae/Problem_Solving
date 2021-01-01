n = int(input())
array = list(map(int, input().split()))

d = [0] * 101
d[1] = array[0]
d[2] = max(array[0], array[1])

for i in range(3,n+1):
    d[i] = max(d[i-1], d[i-2]+array[i-1])

print(d)
print(d[n])