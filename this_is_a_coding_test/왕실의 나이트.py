position = input()
row = int(position[1])
column = ord(position[0]) - ord('a') + 1
steps = [(-2,1),(-2,-1),(2,1),(2,-1),(-1,-2),(1,-2),(-1,2),(1,2)]

answer = 0
for step in steps :
    moved_row = row + step[0]
    moved_column = column + step[1]
    if moved_row >= 1 and moved_row <= 8 and moved_column >=1 and moved_column <= 8 :
        answer += 1

print(answer)