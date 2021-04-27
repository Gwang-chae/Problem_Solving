# 문제
# https://programmers.co.kr/learn/courses/30/lessons/17681

# IDEA
# 숫자들을 이진수로 변환
# n에 맞게 변환한 이진수를 맞춰줘야함

# 추가적으로 zfill(n) 함수로 str 형태 맨 앞에 인자 n만큼 '0'을 삽입 가능
# 또한, rjust(n, 'char') 함수의 경우, 설정한 'char'을 n번 맨 앞에 삽입 가능
def solution(n, arr1, arr2):
    arr_1, arr_2 = [], []
    for i in arr1:
        bin_i = bin(i)[2:]
        if len(bin_i) < n:
            while len(bin_i) != n:
                bin_i = '0' + bin_i
        arr_1.append(list(bin_i))
    
    for i in arr2:
        bin_i = bin(i)[2:]
        if len(bin_i) < n:
            while len(bin_i) != n:
                bin_i = '0' + bin_i
        arr_2.append(list(bin_i))
    
    answer = []
    for i,j in zip(arr_1, arr_2):
        key = ''
        for k in range(n):
            if i[k] == '1' or j[k] == '1':
                key += '#'
            else: key += ' '
        answer.append(key)
        
    return answer