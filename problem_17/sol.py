class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #digits = "233"
        map = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        
        out = []
        
        for digit in digits:
            index = int(digit)
            print index
            
            if not out:
                for alph in map[index-2]:
                    out.append(alph)
            else:
                tmp = []
                for i in xrange(len(out)):
                    for alph in map[index-2]:
                        tmp.append(out[i]+alph)
                out = tmp
        return out