class Solution(object):
    def twoSum(self, nums, target):
        dic = {}

        for i,v in enumerate(nums) :
            if target-v in dic.keys() :
                return([dic[target-v],i]) 
            else : 
                dic[v] = i
        