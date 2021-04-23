from collections import Counter

def solution(clothes):
    type_list = []
    for cloth_name, cloth_type in clothes:
        type_list.append(cloth_type)

    type_count = Counter(type_list)

    answer = 1
    for key, value in type_count.items():
        answer *= value + 1

    if answer == 1:
        return answer
    else:
        return answer -1


