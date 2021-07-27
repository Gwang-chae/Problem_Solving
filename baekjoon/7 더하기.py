# 문제
# https://www.acmicpc.net/problem/4900

# IDEA
# 문제에서 표현하는 7비트 숫자는 2진수 표현이라고 할 수 있음
# LED 숫자 기준 2진수 표현을 10진수 표현으로 변환해 dictionary를 생성하면 간단하게 풀 수 있음

def to_num(x:str) -> str:
    num = ''
    key = ''
    for idx, i in enumerate(x):
        key += i
        if idx % 3 == 2:
            num += code_dict[key]
            key = ''
    return num

def to_code(x:str) -> str:
    code = ''
    for key in x:
        code += num_dict[key]
    return code

code_dict = {'063': '0', '010': '1', '093': '2',
             '079': '3', '106': '4', '103': '5',
             '119': '6', '011': '7', '127': '8', '107': '9'}
num_dict = dict(map(reversed, code_dict.items()))

while True:
    formula = input()
    if formula == 'BYE': break
    a = formula.split('+')[0]
    b = formula.split('+')[-1][:-1]

    c_num = int(to_num(a)) + int(to_num(b))
    c = to_code(str(c_num))
    print(f'{a}+{b}={c}')
