# 문제
# https://leetcode.com/problems/palindrome-number/

# IDEA
# 앞의 인덱스, 뒤의 인덱스를 비교해가며 Palindrome Number인지 확인

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x)-1, -1, -1):
            if x[len(x)-1 - i] != x[i]:
                return False
        return True