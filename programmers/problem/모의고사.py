from itertools import cycle

def solution(answers):
    score = [0, 0, 0]
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for cycle_a, cycle_b, cycle_c, ans in zip(cycle(a), cycle(b), cycle(c), answers):
        if cycle_a == ans:
            score[0] += 1
        if cycle_b == ans:
            score[1] += 1
        if cycle_c == ans:
            score[2] += 1

    max_score = max(score)
    answer = []
    for i in range(3):
        if score[i] == max_score:
            answer.append(i + 1)

    return answer