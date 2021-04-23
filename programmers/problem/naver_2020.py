n = 6
p = [5, 4, 7, 2, 0, 6]
c = [4, 6, 4, 9, 2, 3]

total = 0
price = 100
p_lst = []
rest = 0
count = 0
day = 0

for i in range(n):
    p[i] += rest
    day += 1
    rest = 0
    if p[i] >= c[i] :
        count = 0
        rest = p[i] - c[i]
        total += price * c[i]
        price = 100
    else :
        count += 1
        rest = p[i]
        price /= 2
    if count == 3 :
        break

answer = int(total/day)
answer = str('%.2f' % answer)
print(answer)