class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        smaller_values = []
        for num in nums : 
            substract_nums = [i-num for i in nums if i-num < 0]
            smaller_values.append(len(substract_nums))
        return smaller_values

