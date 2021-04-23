## 문제 1
from collections import deque

A = [1,4,2]
B = [5,4,4]
A.sort()
B.sort(reverse=True)
a_que = deque(A)
b_que = deque(B)

answer = 0
for i in range(len(a_que)):
    a = a_que.popleft()
    b = b_que.popleft()
    answer += a*b
print(answer)

## 문제 2
s = '1111111'
total_zero_count = 0
convert = 0

while True:
    convert += 1
    zero_count = 0
    for i in s:
        if i == '0':
            total_zero_count += 1
            zero_count += 1
    s = '1'*(len(s) - zero_count)
    s = str(bin(len(s)))[2:]
    if s == '1':
        break

print([convert, total_zero_count])