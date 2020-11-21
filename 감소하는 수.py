# 시간초과

x, y = map(int,input().split())
z = y/x * 100
z_initial = int(z)
count = 0

while int(z) == z_initial:
    count += 1
    x += 1
    y += 1
    z = y/x * 100

print(count)