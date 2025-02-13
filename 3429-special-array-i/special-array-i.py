class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
            counter = 0
            stack = []
            for i in nums :
                
                
                if counter == 0 :
                    stack.append(i)
                    counter += 1
                    continue
                if i%2 == 0 :
                    if stack[len(stack) -1 ] % 2 == 0 : 
                        return False
                if i%2 != 0 : 
                    if stack[len(stack) - 1 ] % 2 != 0 : 

                        return False
                stack.append(i)
            return True

        