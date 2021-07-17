# 문제
# https://www.acmicpc.net/problem/1706

# IDEA
# row, column별로 한줄씩 읽은 후, '#'을 기준으로 파싱
# 2글자 이상이면 낱말로 판단, 낱말 리스트에 삽입
# 사전순 정렬 후 첫째값 출력

r,c = map(int,input().split())
cross_word = [input() for _ in range(r)]

words = []

for row_word in cross_word:
    parsing = row_word.split('#')
    for p in parsing:
        if len(p) >= 2:
            words.append(p)

for i in range(c):
    column_word = ''
    for word in cross_word:
        column_word += word[i]
    parsing = column_word.split('#')
    for p in parsing:
        if len(p) >= 2:
            words.append(p)

words.sort()
print(words[0])