class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        my_string = "".join(map(str, digits))
        my_integar = int(my_string) + 1
        my_integar = [int(d) for d in str(my_integar)]

        return my_integar
        