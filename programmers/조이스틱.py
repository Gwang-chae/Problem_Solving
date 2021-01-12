def solution(name):
    name = list(name)

    # 위아래 이동
    up_down = 0
    for letter in name:
        count = min(ord(letter) - ord('A'), ord('Z') - ord(letter) + 1)
        up_down += count

    # 좌우 이동
    left_right = 0

    A = ['A'] * len(name)
    A_checker = [False] * len(name)

    # name중 A가 아닌 부분을 check
    for i in range(len(name)):
        if A[i] != name[i]:
            A_checker[i] = False
        else:
            A_checker[i] = True

    idx = 0
    while True:
        # A_check에 False가 없으면 종료
        if((False in A_checker) is False):
            break

        # 오른쪽, 왼쪽 중에서 'A'가 아닌 가장 가까운 곳 찾기
        # 찾을 때까지 거리(dist)를 늘려가며 탐색
        dist = 0
        while True:
            if A_checker[idx] == False:
                break

            # 없을 경우 dist 증가
            dist += 1

            # 오른쪽 이동
            if ( A_checker[(idx + dist) % len(name)] == False) :
                idx = (idx + dist) % len(name)

            # 왼쪽 이동
            elif ( A_checker[(idx - dist) % len(name)] == False) :
                idx =  (idx - dist) % len(name)

        # 'A'가 아닌 바꿔야 할 부분을 찾았으면
        # 'A'로 바꿨다고 표시
        A_checker[idx] = True
        # 움직인 거리만큼 left_right를 업데이트
        left_right += dist

    answer = up_down + left_right

    return answer