class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        #print len(s)
        #s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        #wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        check = set()
        return self.backtrace(s,wordDict,len(s),check)
        
    def backtrace(self, s, wordDict, index, check):
        #print s[:index:]
        if s[:index:] in wordDict:
            #print s[:index:]
            return True
        elif s[:index:] in check:
            return False
        
        check.add(s[:index:])
        
        for i in xrange(index+1):
            if s[index-i:index:] in wordDict:
                #print s[index-i::]
                if self.backtrace(s,wordDict,index-i,check) == True:
                    return True
        return False