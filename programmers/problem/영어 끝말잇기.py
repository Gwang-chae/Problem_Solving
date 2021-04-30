# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12981

# IDEA
# 끝말잇기 조건을 요구하는대로 구현

def solution(n, words):
    used_word = [words[0]]
    last_word = words[0][-1]
    for idx, w in enumerate(words):
        turn = idx%n + 1
        if idx == 0:
            continue
        if w[0] == last_word and w not in used_word:
            used_word.append(w)
            last_word = w[-1]
        else:
            return [turn, idx//n + 1]
    return [0,0]