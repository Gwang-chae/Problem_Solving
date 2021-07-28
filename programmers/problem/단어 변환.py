# 문제
# https://programmers.co.kr/learn/courses/30/lessons/43163

# IDEA

def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = 0
    word_len = len(begin)
    word_list = [begin]
    diff_word = list()
    
    while True:
        for spelling in word_list:
            diff_word.clear()
            for word in words:
                diff = 0
                for idx in range (0, word_len):
                    if spelling[idx] != word[idx]: diff += 1
                    if diff > 1: break
                if diff==1: # 1글자 차이
                    diff_word.append(word)
                    words.remove(word)
        
        answer += 1            
        if target in diff_word: return answer
        else: word_list = diff_word