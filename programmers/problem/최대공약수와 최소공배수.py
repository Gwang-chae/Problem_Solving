# 문제
# https://programmers.co.kr/learn/courses/30/lessons/12940

# IDEA
# 유클리드 호제법으로 최대공약수를 구한 후
# 최소공배수 = 두 수의 곱 / 최대공약수라는 공식을 통해 최소공배수 도출

# 유클리드 호제법 : a>b일 때 r = a%b라 하면, a와 b의 최대공약수는 b와 r의 최대공약수와 같음
# 이 성질에 따라 r' = b%r을 구하고, r'' = r%r'를 반복하면서
# 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수

# 추가적으로 math 패키지의 gcd를 통해 최대공약수를 쉽게 구할 수 있음
def get_gcd(n, m):
    a,b = max(n,m), min(n,m)
    while True:
        r = a%b
        if r == 0:
            break
        a = b
        b = r
    return b

def solution(n, m):
    gcd = get_gcd(n,m)
    lcm = n*m / gcd
    return [gcd, lcm]
