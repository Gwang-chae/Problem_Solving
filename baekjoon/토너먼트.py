# 문제
# https://www.acmicpc.net/problem/1057

import sys

n, jimin, hansu = map(int, input().split())
count = 0
while True:
    count += 1
    if jimin%2 == 1 and jimin + 1 == hansu:
        break
    if hansu%2 == 1 and hansu + 1 == jimin:
        break
    if jimin%2 == 1: jimin = (jimin + 1) // 2
    else: jimin //= 2
    if hansu%2 == 1: hansu = (hansu + 1) // 2
    else: hansu //= 2

print(count)