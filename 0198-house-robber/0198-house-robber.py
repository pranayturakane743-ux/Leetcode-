class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        prev2, prev1 = 0, 0
        
        for num in nums:
            new_max = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = new_max
            
        return prev1