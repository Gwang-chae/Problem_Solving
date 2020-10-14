n = int(input())
lst = []
for _ in range(n):
    lst.append(input().split())

lst = sorted(lst, key=lambda x:x[1])

for name in lst:
    print(name[0], end=' ')