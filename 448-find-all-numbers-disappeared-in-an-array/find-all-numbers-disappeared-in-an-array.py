class Solution(object):
    def findDisappearedNumbers(self, nums):
        unq = set(nums)
        lst = []


        unq_lst = list(unq)
        for i in range(1,len(nums)+1) : 
            if i not in unq :
                lst.append(i)


        return lst
        