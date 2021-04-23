# 문제
# https://programmers.co.kr/learn/courses/30/lessons/49191

# 순위를 알 수 있는 사람들의 수를 구하는 문제
# 순위를 알려면 나를 제외한 사람들과의 승패 관계를 알아야 함
# 이길 수 있는 사람과 없는 사람을 구분하고
# 그 안에서 또 관계에 맞게 엮어 줘야 함
# 승패 여부를 hash로 표현한 후, 그 하위 관계를 update

def solution(n, results):
    wins, loses = dict(), dict()
    # wins[i] : i가 이길 수 있는 사람들의 집합
    # loses[i] : i가 이길 수 없는 사람들의 집합
    for i in range(1, n+1):
        wins[i], loses[i] = set(), set()

    for i in range(1, n+1):
        # 경기 결과값 입력
        for winner, loser in results:
            if winner == i:
                wins[i].add(loser)
            if loser == i:
                loses[i].add(winner)

        # i를 이긴 사람들은 i가 이길 수 있는 사람들을 반드시 이김
        for w in loses[i]:
            wins[w].update(wins[i])

        # i에게 진 사람들은 i가 이길수 없는 사람들에게 반드시 짐
        for l in wins[i]:
            loses[l].update(loses[i])

    answer = 0
    # i가 이길 수 있는 사람들과 이길 수 없는 사람들의 수가
    # 자기 자신을 뺀 n-1개면 순위를 알 수 있음
    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n-1:
            answer += 1
    return answer
