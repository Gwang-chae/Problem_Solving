from math import sqrt

def solution(brown, yellow):
    divisor = []
    for i in range(1, int(sqrt(yellow)+1)):
        if yellow%i == 0:
            divisor.append(i)

    divisor.sort()

    width = 0
    height = 0

    for j in divisor:
        if brown == (2*j + 2*(yellow//j) + 4):
            width += j + 2
            height += yellow//j + 2
            break

    if width < height:
        width,height = height, width

    answer = [width, height]
    return answer