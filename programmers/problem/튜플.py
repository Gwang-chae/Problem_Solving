def solution(s):
    s = s.replace('{',"")
    s = s.split('},')
    s[-1] = s[-1][:-2]
    s = sorted(s, key=lambda x:len(x))

    for i in range(len(s)):
        s[i] = s[i].split(",")

    answer = []
    for i in range(len(s)):
        if i == 0 :
            first = int(s[i][0])
            answer.append(first)
        else :
            rest = [x for x in s[i] if x not in s[i-1]]
            rest = int(rest[0])
            answer.append(rest)

    return answer