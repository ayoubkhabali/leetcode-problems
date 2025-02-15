class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        for n in nums :
            if n >= k : continue
            else : counter+= 1

        return counter
        