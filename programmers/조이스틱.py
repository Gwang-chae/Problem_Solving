name = 'ASDBXOASDBAABSDASA'
name = list(name)

# 위아래 이동
up_down = 0
for letter in name:
    count = min(ord(letter) - ord('A'), ord('Z') - ord(letter) + 1)
    up_down += count

# 좌우 이동
# 'A'로만 이름이 구성될 경우 좌우 이동은 0
if name == ['A'] * len(name):
    left_right = 0

# 이름에 'A'가 없는 경우 좌우 이동은 len(name) - 1
if not [x for x in name if x in ['A']]:
    left_right = len(name) - 1

# 이름에 'A'가 존재하는 경우
else:
    # index 0값을 A로 바꿔주고 시작
    idx = 0
    name[0] = "A"
    left_right = 0
    while True:
        # 모든 글자가 'A'가 될 때 while문 종료
        if name == ['A'] * len(name):
            break
        
        # 오른쪽으로 이동하며 이동값 count
        # 'A'가 아닌(바꿔야 하는) 지점에서 종료
        right = 0
        for i in range(1, len(name[idx:])):
            right += 1
            if name[idx+i] != 'A':
                break
        
        # 왼쪽으로 이동하며 이동값 count
        # 'A'가 아닌(바꿔야 하는) 지점에서 종료
        left = 0
        for j in range(1, len(name[idx:])):
            left += 1
            if name[idx-j] != 'A':
                break
        
        # 오른쪽 값이 작을 경우 오른쪽 방향을 선택
        if right <= left:
            # 오른쪽 방향에서 가장 가까운 'A'가 아닌 지점을 'A'로 변경
            name[idx+right] = 'A'
            # 인덱스를 해당 지점으로 변경 다시 loop 시작
            idx += right
            left_right += right
        # 반대의 경우
        else:
            # 왼쪽 방향에서 가장 가까운 'A'가 아닌 지점을 'A'로 변경
            name[idx-left] = 'A'
            # 인덱스를 해당 지점으로 변경 다시 loop 시작
            idx = len(name) + 1 - left
            left_right += left

print(up_down + left_right)