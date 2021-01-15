def solution(citations):
    # max(citations)부터 0까지 h를 줄여가며 탐색
    for h in range(max(citations), -1, -1):
        over_h = 0
        for citation in citations:
            if citation >= h:
                over_h += 1
            # 조건에 부합하는대로 over_h >= h 이상이면 해당 값 출력
            if over_h == h:
                return over_h
    # citations가 0으로만 이뤄진 케이스
    return 0