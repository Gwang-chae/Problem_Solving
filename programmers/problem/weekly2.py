# 문제
# https://programmers.co.kr/learn/courses/30/lessons/83201

# IDEA
# 점수를 열 기준으로 담는 부분만 유의하면
# 나머지는 조건대로 구현해주면 된다.

def solution(scores):
    mean_list = []
    for i in range(len(scores)):
        score_list = []
        for j in range(len(scores)):
            score_list.append(scores[j][i])
            if i == j: my_score = scores[i][j]
        
        if len([x for x in score_list if x == my_score]) == 1 and (my_score == max(score_list) or my_score == min(score_list)):
            mean = (sum(score_list) - my_score) / (len(score_list) - 1)
        else:
            mean = sum(score_list) / len(score_list)
        mean_list.append(mean)
    
    answer = []
    for i in mean_list:
        if i >= 90: answer.append('A')
        elif 80 <= i < 90: answer.append('B')
        elif 70 <= i < 80: answer.append('C')
        elif 50 <= i < 70: answer.append('D')
        else: answer.append('F')
    
    return ''.join(answer)