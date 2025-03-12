class Solution(object):
    def numberOfSubstrings(self, s):
        N = len(s)
        d = {letter : 0 for letter in "abc"}
        is_valid = lambda : all(freq > 0 for freq in d.values())
        print(is_valid())
        l,res = 0, 0
        for r, letter in enumerate(s) :
            d[letter] += 1

            while is_valid() :
                res += N -r
                d[s[l]] -=1
                l+=1
        return res
        