from collections import deque

def solution(people, limit):
    people.sort()

    q = deque(people)
    boat = 0

    while q:
        # 가장 무거운 사람과 가장 가벼운 사람을 보트에 태워보고
        # limit을 초과하면 가장 무거운 사람만 태우고,
        # limit보다 작거나 같으면 두 명을 태우고, 양쪽을 pop
        if len(q) >= 2:
            if q[0] + q[-1] <= limit:
                q.pop()
                q.popleft()
                boat += 1
            elif q[0] + q[-1] > limit:
                q.pop()
                boat += 1
        # q에 한 명만 남을 경우
        # 문제 조건에 따르면 사람은 항상 limit보다 작기 때문에
        # if문은 생략 가능
        else:
            if q[0] <= limit:
                q.pop()
                boat += 1

    return boat
