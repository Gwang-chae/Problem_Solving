# initR = 3
# initC = 2
# finalR = 1
# finalC = 3

# costRows = [1,2,3]
# costCols = [7,8,9]

# if initR <= finalR:
#     print(sum(costRows[initR:finalR]))
# if initC <= finalC:
#     print(sum(costCols[initC:finalC]))
# if initR > finalR:
#     print(costRows[finalR:initR])


pickup = [0,2,9,10,11,12]
drop = [5,9,11,11,14,17]
tip = [1,2,3,2,2,1]
total = []
for i in range(len(pickup)):
    total.append(drop[i] - pickup[i] + tip[i])

d = [0] * len(pickup)
d[len(pickup) - 1] = drop[len(pickup) - 1] - pickup[len(pickup) - 1] + tip[len(pickup) - 1]
print(d)
# print(total)
for i in range(len(pickup)-1, -1, -1):
    print(drop[i-1])
    print(pickup[i])
    if drop[i-1] > pickup[i]:
        d[i-1] = max(d[i], total[i-1])
    # else:
    #     d[i-1] = max(d[i], d[i-1 ],d[i] + total[i-1])
    # else:
    #     d[i] = max(d[i-1], (drop[i] - pickup[i] + tip[i]))
print(d)

# print(d)
# answer = []
# dist = [1e9, 0, 1, 1, 2, 1]
# for value, idx in enumerate(dist):
#     answer.append((value,idx))

# answer = sorted(answer, key=lambda x:x[1])
# print(answer)

# a = []
# for i in answer:
#     if i[1] == 0 or i[1] == 1e9:
#         continue
#     else:
#         a.append(i[0])
# print(a)

# dp = [0,0,0,0,0,1,2]