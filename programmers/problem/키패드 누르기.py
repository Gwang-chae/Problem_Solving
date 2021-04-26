# 문제
# https://programmers.co.kr/learn/courses/30/lessons/67256

# 손이 현재 놓인 위치에 따라 거리값을 구하는 함수를 생성
# 조건에 맞게 구현

def find_distance(number, hand_now):
    phone = {'1': (0,0), '2':(0,1), '3':(0,2),
             '4': (1,0), '5':(1,1), '6':(1,2),
             '7': (2,0), '8':(2,1), '9':(2,2),
             '*': (3,0), '0':(3,1), '#':(3,2)}
    number_x, number_y = phone[str(number)]
    hand_x, hand_y = phone[str(hand_now)]
    return abs(number_x - hand_x) + abs(number_y - hand_y)

def solution(numbers, hand):
    left_now = '*'
    right_now = '#'
    answer = ''
    
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            left_now = i
        elif i in [3,6,9]:
            answer += 'R'
            right_now = i
        else:
            left_dist = find_distance(i, left_now)
            right_dist = find_distance(i, right_now)
            if left_dist < right_dist:
                answer += 'L'
                left_now = i
            elif left_dist > right_dist:
                answer += 'R'
                right_now = i
            else:
                if hand == 'left':
                    answer += 'L'
                    left_now = i
                else:
                    answer += 'R'
                    right_now = i
                    
    return answer