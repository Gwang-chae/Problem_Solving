# 문제
# https://programmers.co.kr/learn/courses/30/lessons/49993

# IDEA
# 선행순서를 고려해서 선행이 아닌 값이 나오면 for문을 break
# 파이썬의 for-else문을 이용

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        skill_list = list(skill)

        for i in tree:
            if i in skill and i != skill_list.pop(0):
                break
        else:
            answer += 1
    return answer