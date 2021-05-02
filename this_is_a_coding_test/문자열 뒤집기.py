s = input()

zero = 0
one = 0

if s[0] == '0':
    zero += 1
else:
    one += 1

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        # 그 다음 수가 0이 되면
        # 연속된 1이 끝났으므로 one에 1 추가
        if s[i] == '0':
            one += 1
        else:
            zero += 1

print(min(zero, one))