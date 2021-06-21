# 문제
# https://programmers.co.kr/learn/courses/30/lessons/42888

# IDEA
# 이중 forloop로 구현
# user_id와 nickname을 매칭하는 딕셔너리를 생성하여
# 문제 정의에 맞게 출력

def solution(record):
    user_dict = {}
    for log in record:
        if len(log.split()) == 3:
            command, user_id, nickname = log.split()[0], log.split()[1], log.split()[2]
            user_dict[user_id] = nickname

    answer = []
    for log in record:
        command, user_id = log.split()[0], log.split()[1]
        if command == 'Enter':
            answer.append(user_dict[user_id] + '님이 들어왔습니다.')
        if command.split()[0] == 'Leave':
            answer.append(user_dict[user_id] + '님이 나갔습니다.')
    
    return answer