def solution(N, stages):

    lst = []
    number = len(stages)

    for i in range(1,N+1) :
        count = stages.count(i)
        if count == 0 :
            fail = 0
        else :
            fail = count/number
        lst.append([i,fail])
        number -= count

    lst = sorted(lst, key=lambda x:-x[1])
    answer = []

    for j in lst:
        answer.append(j[0])

    return answer