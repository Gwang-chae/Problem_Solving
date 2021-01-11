def solution(s):
    answer = len(s)
    # 문자열을 압축할 수 있는 최대 단위는 len(s)//2이므로
    # 1부터 len(s)//2번 인덱스까지 단위를 늘려가면서 확인 
    for step in range(1, len(s)//2 + 1):
        compression = ''
        front_letter = s[0:step]
        count = 1
        # 단위만큼 증가시키며 이전 문자열과 비교
        for step_word in range(step, len(s), step):
            if front_letter == s[step_word:step_word + step]:
                count += 1
            # 이전 문자열과 같지 않은 문자열을 만나면
            else:
                # compression에 단위 count + 문자열 형식으로 입력
                # count가 1이라면 압축할게 없는 것이므로 front_letter 그대로 삽입
                compression += str(count) + front_letter if count >=2 else front_letter
                # front_letter를 그 다음 문자열로 초기화해서 뒤쪽도 탐색가능하게 만들어줌
                front_letter = s[step_word:step_word + step]
                # count 또한 초기화
                count = 1
        # forloop가 끝나고 남은 뒤의 문자열들을 위 조건과 같은 형태로 compression에 입력
        compression += str(count) + front_letter if count >=2 else front_letter
        # len(s)와 compression 비교하여 가장 짧은 값을 제출
        answer = min(answer, len(compression))
    return answer