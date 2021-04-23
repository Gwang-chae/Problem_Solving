from collections import Counter

n = 9
edges = [[0,2],[2,1],[2,4],[3,5],[5,4],[5,7],[7,6],[6,8]]

max_edge_count = n//3 - 1
e = []
for edge in edges:
    e.append(edge[0])

counter = Counter(e)

answer = []
for key, value in counter.items():
    if value == max_edge_count:
        answer.append(key)

print(answer)