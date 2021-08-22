# 문제
# https://leetcode.com/problems/reverse-integer/

# IDEA
# 문제 정의에 맞게 구현만 하면 됐던 문제

class Solution:
    def reverse(self, x: int) -> int:
        if int(x) < 0:
            answer = '-'
            for i in str(x)[:0:-1]:
                answer += i
        else:
            answer = ''
            for i in str(x)[::-1]:
                answer += i
        
        if int(answer) < -(2**31) or int(answer) >= 2**31: return 0
        else: return int(answer)# x = str(x)