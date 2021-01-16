# arr가 들어오면 가장 긴 문자열 체인을 return
# 만약 word1에 글자를 하나 더해 word2를 만들 수 있다면 word1을 word2의 이전 버전이라 할 수 있음
# a -> ba -> bca -> bdca
arr = ['a','b','ba','bca','bda','bdca']

def solution(arr):
    arr.sort(key=lambda x:len(x))
    word_count = {}
    for word in arr:
        word_count[word] = 1
        for i in range(len(word)):
            prev = word[:i] + word[i+1:]
            if prev in word_count:
                word_count[word] = word_count[prev] + 1
                break

    return max(word_count.values())

print(solution(arr))