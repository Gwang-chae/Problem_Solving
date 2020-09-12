import numpy as np

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

info_lst = []
for i in info:
    info_lst.append(i.split())
info_lst = np.asarray(info_lst)

query_lst = []
for ii in query:
    query_lst.append(ii.split(' and '))

for j in query_lst:
    tmp = j[-1].split(' ')
    j.pop()
    j.append(tmp[0])
    j.append(tmp[1])
query_lst = np.asarray(query_lst)

answer = []
for i in query_lst:
    answer_count = 0
    for j in info_lst:
        if (i[0] == j[0] or i[0] =='-') and (i[1] == j[1] or i[1] =='-') and (i[2] == j[2] or i[2] =='-') and (i[3] == j[3] or i[3] =='-') and (int(i[4]) <= int(j[4]) or i[4] =='-'):
            answer_count += 1
    answer.append(answer_count)

print(answer)