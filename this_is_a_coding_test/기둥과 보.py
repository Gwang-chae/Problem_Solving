# 설치, 삭제 가능 여부 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 설치된 것이 기둥인 경우
            # 만약 '바닥 위' 또는 '보의 한쪽 끝'(보의 왼쪽/오른쪽) 또는 '다른 기둥 위'라면 가능
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False    # 가능하지 않다면 False
        else:   # 설치된 것이 보인 경우
            # 만약 '한쪽 끝이 기둥 위(보의 왼쪽/오른쪽이 기둥 위)' 또는 '양쪽 끝 부분이 보'이면 가능
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False    # 가능하지 않다면 False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:    # 삭제하는 경우
            answer.remove([x, y, stuff])    # 삭제를 해본 후
            if not possible(answer):    # 가능한 구조인지 확인
                answer.append([x, y, stuff])    # 불가능하다면 다시 생성
        else:   # 생성하는 경우
            answer.append([x, y, stuff])    # 생성을 해본 후
            if not possible(answer):    # 가능한 구조인지 확인
                answer.remove([x, y, stuff])    # 가능하다면 다시 제거
    return sorted(answer)