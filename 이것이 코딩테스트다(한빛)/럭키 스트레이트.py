n = input()
# n은 항상 자릿수가 짝수 형태이므로
# mid를 둬서 나눠서 변수에 넣어주면 됨
mid = len(n) // 2

left = 0
right = 0

for i in range(len(n)):
    if i < mid:
        left += int(n[i])
    else:
        right += int(n[i])

if left == right:
    print('LUCKY')
else:
    print('READY')