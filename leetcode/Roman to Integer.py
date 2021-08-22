# 문제
# https://leetcode.com/problems/roman-to-integer/

# IDEA
# 각각의 로마숫자를 아라비아 숫자로 변환
# 뒤에 숫자가 더 크다면 앞에 있는 숫자를 빼준다.

class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        for i in range(len(s)-1):
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                answer -= roman_dict[s[i]]
            else: answer += roman_dict[s[i]]
        answer += roman_dict[s[-1]]
        return answer