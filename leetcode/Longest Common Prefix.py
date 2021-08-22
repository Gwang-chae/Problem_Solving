# 문제
# https://leetcode.com/problems/longest-common-prefix/

# IDEA
# min()으로 가장 짧은 단어를 추출한 후, 나머지 단어들과 한글자씩 비교
# 만약 한 단어라도 현재 알파벳과 다르다면 공통이 아니므로
# 그 전 알파벳까지가 공통된 가장 긴 접두사

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        
        min_str = min(strs, key=len)
        for idx, alpha in enumerate(min_str):
            for word in strs:
                if word[idx] != alpha:
                    return min_str[:idx]
                
        return min_str