class Solution(object):
    def containsDuplicate(self, nums):
        s = set()
        for num in nums :
            s.add(num)

        if len(s) == len(nums) :
            return False
        else : return True
