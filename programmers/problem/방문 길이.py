# 문제
# https://programmers.co.kr/learn/courses/30/lessons/49994

# IDEA
# 일반적인 구현 문제 
# 단, 방문하지 않은 선분의 길이를 구해야 하므로 출발 지점과 도착 지점을 동시에 고려해야 함.

def solution(dirs):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    d = {'U':0, 'D':1, 'L':2, 'R':3}
    visited = []
    now = (0,0)
    answer = 0
    
    for i in dirs:
        new = (now[0] + dx[d[i]], now[1] + dy[d[i]])
        if abs(new[0]) > 5 or abs(new[1]) > 5:
            continue
        else:
            if (now, new) not in visited:
                answer += 1
                visited.append((now, new))
                visited.append((new, now))
            now = new
    return answer