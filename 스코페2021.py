n = int(input())
start_list = []
end_list = []

for i in range(n):
    time = input().split(' ~ ')
    start = int(time[0][0:2] + time[0][3:5])
    start_list.append(start)
    end = int(time[1][0:2] + time[1][3:5])
    end_list.append(end)

if max(start_list) <= min(end_list):
    start_time = str(max(start_list))
    if len(start_time) == 3:
        start_time = '0' + start_time
    answer_start = start_time[0:2] + ':' + start_time[2:4]
    end_time = str(min(end_list))
    if len(end_time) == 3:
        end_time = '0' + end_time
    answer_end = end_time[0:2] + ':' + end_time[2:4]
    print(answer_start + ' ~ ' + answer_end)

else:
    print('-1')

n = int(input())
route = input()
route = route.split('0')
route = [x for x in route if len(x) >= 3]

if not route:
    print(1)
else:
    count = 0
    for r in route:
        m = len(r)
        dp = [0] * (m + 2)
        dp[1], dp[2] = 1, 1
        for i in range(1, m//2 + 1):
            dp[2*i] = dp[2*i - 1] + (i - 1)
            dp[2*i + 1] = dp[2*i] + i
        count += dp[m]
    print(count)

favor = list(map(float, input().split()))
gname = ['A','B','C','D','E']
table = [[x,y] for x,y in zip(gname, favor)]
n,m = map(int, input().split())

read = []
for i in range(n):
	r = list(input())
	read.append(r)

genre = []
for j in range(n):
	g = list(input())
	genre.append(g)
		
dic = dict()
dic['A'], dic['B'], dic['C'], dic['D'], dic['E'] = False, False, False, False, False

# Y 찾기
for j in range(m):
  for i in range(n):
      if read[i][j] == 'Y':
           if dic[genre[i][j]] == False:
               dic[genre[i][j]] = [i, j]
for idx,v in enumerate(dic.values()):
  if v != False:
      table[idx].append(v[0])
      table[idx].append(v[1])

y_table = [x for x in table if len(x) > 3]
y_table = sorted(y_table, key=lambda x:-x[1])

# O 찾기
table = [[x,y] for x,y in zip(gname, favor)]
dic['A'], dic['B'], dic['C'], dic['D'], dic['E'] = False, False, False, False, False
for j in range(m):
    for i in range(n):
        if read[i][j] == 'O':
            if dic[genre[i][j]] == False:
                dic[genre[i][j]] = (i, j)

for idx,v in enumerate(dic.values()):
  if v != False:
      table[idx].append(v[0])
      table[idx].append(v[1])
			
o_table = [x for x in table if len(x) > 3]
o_table = sorted(o_table, key=lambda x:-x[1])

for y in y_table:
	print(y[0], y[1], y[2], y[3], sep=' ')

for o in o_table:
	print(o[0], o[1], o[2], o[3], sep=' ')

n,m = map(int,input().split())
graph = []
for k in range(m):
	graph.append(list(map(int,input().split())))
	
for j in range(n):
	for i in range(m):
			if i == 0 and j == 0:
					pass
			elif i == 0:
					graph[i][j] += graph[i][j-1]
			elif j == 0:
					graph[i][j] += graph[i-1][j]
			else:
					graph[i][j] += max(graph[i-1][j], graph[i][j-1])
print(graph[m-1][n-1])

import numpy as np

n = 4
graph = [[1,1,1,0],
         [1,1,1,0],
         [0,1,1,0],
         [0,0,0,0]]
graph = np.array(graph
k = 2

for i in range(k):
    for j in range(k):
        if sum(sum(graph[i:i+k,j:j+k])) == k*k:
            print('yes')

# print(sum(sum(graph[0:2,0:2])))