class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        lastWord = words[-1]
        return len(lastWord)
        
