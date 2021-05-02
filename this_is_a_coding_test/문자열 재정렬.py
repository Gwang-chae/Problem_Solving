s = list(input())

letter = []
number = []

for i in s:
    if i.isalpha():
        letter.append(i)
    else:
        number.append(int(i))

letter.sort()
letter = ''.join(letter)

# letter가 빈 리스트일지라도,
# number는 빈 리스트가 아니므로 고려할 필요 x

# number가 빈 리스트가 아닐 때
if number:
    print(letter + str(sum(number)))
# number가 빈 리스트일 때
else:
    print(letter)