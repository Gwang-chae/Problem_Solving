# 문제
# https://www.acmicpc.net/problem/18870

# IDEA
# set()으로 중복없는 값들을 추출 후 정렬
# dictionary로 작은 값부터 0으로 시작하는 value 부여
# search가 쉽도록 key와 value를 map()으로 변경

n = int(input())
arr = list(map(int, input().split()))
set_arr = sorted(set(arr))

# dictionary = {set_arr[i] : i for i in range(len(set_arr))}로 아래 작업 가능
dictionary = dict()
for i in range(len(set_arr)):
    dictionary[i] = set_arr[i]

dictionary = dict(map(reversed, dictionary.items()))

for i in arr:
    print(dictionary[i], end=' ')