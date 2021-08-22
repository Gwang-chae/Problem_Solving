# 문제
# https://leetcode.com/problems/two-sum/

# IDEA
# 이중 forloop를 돌며 가능한 조합 탐색
# 조합의 원소가 같을 경우, index() 시작점을 바꿔서 중복 인덱스 회피

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comb = []
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    comb.append(nums[i])
                    comb.append(nums[j])
                    break
                    
        if comb[0] != comb[1]:
            return [nums.index(comb[0]), nums.index(comb[1])]
        else:
            first = nums.index(comb[0])
            second = nums.index(comb[1], first+1)
            return [first, second]